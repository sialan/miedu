from django.db import models
from accounts.models import Account
from multimedia.models import Multimedia
from taggit.managers import TaggableManager

# Create your models here.
class Campaign(models.Model):
    account = models.ForeignKey('accounts.Account', related_name='campaign', blank=True, null=True)
    multimedia = models.ManyToManyField('multimedia.Multimedia')
    backers = models.CommaSeparatedIntegerField(max_length=10000, blank=True, null=True)
    
    active = models.BooleanField()
    completed = models.BooleanField()
    consummated = models.BooleanField()

    currently_featured = models.BooleanField()
    feature_score = models.IntegerField(null=True, blank=True)

    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=50)
    description = models.TextField()

    endline = models.CharField(max_length=50)
    summary = models.TextField()
    call_to_action = models.CharField(max_length=50, null=True, blank=True)

    minimum_pledge = models.IntegerField(default=1)
    number_backers = models.IntegerField(default=0)

    goal = models.IntegerField()
    amount_pledged = models.IntegerField(default=0)

    city = models.CharField(max_length=34)
    state = models.CharField(max_length=34, null=True, blank=True)
    country = models.CharField(max_length=50)

    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return unicode("%s: %s" % (self.account, self.title))

class ContentBlock(models.Model):
    STYLE_CHOICES = (
        ('B', 'Bullet'),
        ('I', 'Image'),
        ('M', 'Multimedia'),
        ('T', 'Text'),
    )
    campaign = models.ForeignKey('campaigns.Campaign')
    subheading = models.CharField(max_length=50)
    style = models.CharField(max_length=2, default='B', choices=STYLE_CHOICES)
    media = models.ManyToManyField('multimedia.Multimedia', null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    field_one = models.TextField(null=True, blank=True)
    field_two = models.TextField(null=True, blank=True)
    field_three = models.TextField(null=True, blank=True)

class CampaignComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    campaign = models.ForeignKey('campaigns.Campaign')

    def __unicode__(self):
        return unicode("%s: %s" % (self.campaign, self.body[:60]))

class CampaignFAQItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=100)
    answer = models.TextField()
    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return unicode("%s: %s" % (self.campaign, self.question[:60]))