from django.db import models
from accounts.models import Account
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = (
        ('UN', 'Unknown'),
        ('MM', 'Male-Male'),
        ('FF', 'Female-Female'),
        ('MF', 'Male-Female'),
        ('FM', 'Female-Male'),
    )
    TYPE_CHOICES = (
        ('UN', 'Unknown'),
        ('MM', 'Male-Male'),
        ('FF', 'Female-Female'),
        ('MF', 'Male-Female'),
        ('FM', 'Female-Male'),
    )
    title = models.CharField(max_length=60)
    category = models.CharField(max_length=2, default='UN', choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=2, default='UN', choices=TYPE_CHOICES)
    body = models.TextField()
    tagline = models.CharField(max_length=60, null=True, blank=True)
    tags = TaggableManager()
    link = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="blogs/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)

    def __unicode__(self):
        return unicode("%s: %s" % (self.title, self.body[:60]))

class BlogComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))