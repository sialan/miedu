from django.db import models
from taggit.managers import TaggableManager
from accounts.models import Account, Organization
from filebrowser.fields import FileBrowseField

# Create your models here.
class Multimedia(models.Model):
    # TODO: Add category campaigns
    organization = models.ForeignKey('accounts.Organization', null=True, blank=True)
    owner = models.CharField(max_length=50, null=True, blank=True)
    owner_url = models.CharField(max_length=200, null=True, blank=True)
    
    resource = FileBrowseField(max_length=200, blank=True, null=True)
    uploaded_by = models.ForeignKey('accounts.Account', null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    
    category = models.CharField(max_length=10, null=True, blank=True)
    subcategory = models.CharField(max_length=10, null=True, blank=True)
    level = models.CharField(max_length=10, null=True, blank=True)

    title = models.CharField(max_length=50)
    description = models.TextField()
    caption_overlay = models.CharField(max_length=200, null=True, blank=True)

    tags = TaggableManager()

    def __unicode__(self):
        return u'%s' % (self.title)

class MultimediaComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    multimedia = models.ForeignKey('multimedia.Multimedia')

    def __unicode__(self):
        return unicode("%s: %s" % (self.multimedia, self.body[:60]))