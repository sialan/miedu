from django.db import models
from campaigns.models import Campaign
from multimedia.models import Multimedia
from filebrowser.fields import FileBrowseField


# Create your models here.
class Project(models.Model):
    campaign = models.ForeignKey('campaigns.Campaign')
    multimedia_updates = models.ManyToManyField('multimedia.Multimedia', blank=True, null=True)
    backers = models.ManyToManyField('accounts.Account', blank=True, null=True)

    title = models.CharField(max_length=34)
    headline = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    call_to_action = models.CharField(max_length=34, null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    main = models.BooleanField()
    dp_url = FileBrowseField("Image", max_length=200, extensions=[".jpg", ".png", ".gif"], blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    funding_amount = models.IntegerField()
    number_available = models.IntegerField(default=1)
    number_claimed = models.IntegerField(default=0)

class ProjectMilestone(models.Model):
    project = models.ForeignKey('projects.Project')
    subheading = models.CharField(max_length=50)
    media = models.ManyToManyField('multimedia.Multimedia', null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    milestone_date = models.DateTimeField()
    completed = models.BooleanField()