from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, Group
)
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, TagBase, GenericTaggedItemBase
from tags.models import *
from filebrowser.fields import FileBrowseField

class AccountManager(BaseUserManager):
    pass

class Account(AbstractUser):
    RELATIONSHIP_CHOICES = (
        ('O', 'Other'),
        ('A', 'Accounting'),
        ('AA', 'Airlines/Aviation'),
        ('ADR', 'Alternative Dispute Resolution'),

    )
    INDUSTRY_CHOICES = (
        ('S', 'Single'),
        ('O', 'Other'),
        ('A', 'Analyst'),
        ('BA', 'Business Analyst'),
        ('BTA', 'Business Technology Analyst'),
        ('S', 'Student'),
        ('F', "Founder/Co-Founder"),

    )
    FUNCTION_CHOICES = (
        ('A', 'Accounting'),
        ('B', 'Business'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('C', "It's complicated"),
    )
    active = models.BooleanField()
    date_of_birth = models.DateField(blank=True, null=True)
    marital_status = models.CharField(max_length=1, default='S', choices=RELATIONSHIP_CHOICES)
    kids = models.IntegerField(default=0)

    dp = FileBrowseField("Image", max_length=200, extensions=[".jpg", ".png", ".gif"], blank=True, null=True)

    educations = models.ManyToManyField('accounts.Organization', through='Education', related_name='mi_education')
    experiences = models.ManyToManyField('accounts.Organization', through='Experience', related_name='mi_experience')

    activities = TaggableManager(through='TaggedActivity')
    awards = TaggableManager(through='TaggedAward')
    certifications =  TaggableManager(through='TaggedCertification')
    interests = TaggableManager(through='TaggedInterest')
    languages = TaggableManager(through='TaggedLanguage')
    skills = TaggableManager(through='TaggedSkill')

    origin_country = models.CharField(max_length=50, blank=True, null=True)
    origin_city = models.CharField(max_length=50, blank=True, null=True)
    current_country = models.CharField(max_length=50, blank=True, null=True)
    current_city = models.CharField(max_length=50, blank=True, null=True)

    industry = models.CharField(max_length=4, default='O', choices=INDUSTRY_CHOICES)
    function = models.CharField(max_length=4, default='O', choices=FUNCTION_CHOICES)
    objective = models.TextField()
    headline = models.TextField()
    unread = models.IntegerField(blank=True, null=True)

    supporters = models.ManyToManyField('self', through='Supporter', symmetrical=False, blank=True, null=True)
    purchases = models.ManyToManyField('campaigns.Campaign', through='transactions.Transaction', related_name='purchase', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.first_name + self.last_name)

class OrganizationManager(models.Manager):
    """
    Lets us do querysets limited to families that have 
    currently enrolled students, e.g.:
        Family.has_students.all() 
    """
    def get_query_set(self):
        return super(OrganizationManager, self).get_query_set().filter(student__enrolled=True).distinct()


class Organization(Group):
    notes = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    dp = FileBrowseField("Image", max_length=200, directory="dp_images/", extensions=[".jpg", ".png", ".gif"], blank=True, null=True)
    tags = TaggableManager()

    # Two managers for this model - the first is default 
    # (so all families appear in the admin).
    # The second is only invoked when we call 
    # Family.has_students.all()  
    objects = models.Manager()
    check_org = OrganizationManager()

    def __unicode__(self):
        return u'%s' % (self.name)

class Education(models.Model):
    account = models.ForeignKey('Account')
    organization = models.ForeignKey('Organization')

    certification = models.CharField(max_length=50, blank=True, null=True)
    concentration = models.CharField(max_length=50)
    courses = TaggableManager()
    notes = models.TextField(blank=True, null=True)
    grade = models.CharField(max_length=34, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()


class Experience(models.Model):
    account = models.ForeignKey('Account')
    organization = models.ForeignKey('Organization')
    
    tasks = TaggableManager()
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Supporter(models.Model):
    RELATIONSHIP_CHOICES = (
        ('UN', 'Unknown'),
        ('MM', 'Male-Male'),
        ('FF', 'Female-Female'),
        ('MF', 'Male-Female'),
        ('FM', 'Female-Male'),
    )
    account = models.ForeignKey('Account', related_name='account_root')
    supporter = models.ForeignKey('Account', related_name='account_node')
    
    active = models.BooleanField()
    completed = models.BooleanField()
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    last_viewed = models.DateTimeField(auto_now=True)
    amount_supported = models.IntegerField(blank=True, null=True)
    campaign_field = models.CharField(max_length=200)
    relationship = models.CharField(max_length=2, default='UN', choices=RELATIONSHIP_CHOICES)

class TaggedActivity(GenericTaggedItemBase):
    tag = models.ForeignKey(Activity, related_name="activity_detail")

class TaggedAward(GenericTaggedItemBase):
    tag = models.ForeignKey(Award, related_name="award_detail")

class TaggedCertification(GenericTaggedItemBase):
    tag = models.ForeignKey(Certification, related_name="certification_detail")

class TaggedInterest(GenericTaggedItemBase):
    tag = models.ForeignKey(Interest, related_name="interest_detail")

class TaggedLanguage(GenericTaggedItemBase):
    tag = models.ForeignKey(Language, related_name="language_detail")

class TaggedSkill(GenericTaggedItemBase):
    tag = models.ForeignKey(Skill, related_name="skill_detail")
