from django.db import models
from articles.models import Article
from taggit.managers import TaggableManager
from multimedia.models import Multimedia
from accounts.models import Account, Organization
from articles.models import Article
from filebrowser.fields import FileBrowseField

# Create your models here.
class Lesson(models.Model):
    articles = models.ManyToManyField('articles.Article', through='LessonArticle')
    about = models.TextField() 
    title = models.CharField(max_length=50)
    course_number = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    course_staff = models.ManyToManyField('accounts.Account')
    organization = models.ForeignKey('accounts.Organization', null=True, blank=True)
    partner_name = models.CharField(max_length=50, null=True, blank=True)
    partner_url = models.CharField(max_length=200, null=True, blank=True)
    partner_dp = dp = FileBrowseField("Image", max_length=200, directory="dp_images/", extensions=[".jpg", ".png", ".gif"], blank=True, null=True)
    credit_name = models.CharField(max_length=10, null=True, blank=True)
    credit_value = models.IntegerField(null=True, blank=True)
    image = FileBrowseField("Image", max_length=200, directory="dp_images/", extensions=[".jpg", ".png", ".gif"], blank=True, null=True)
    video_intro = models.ManyToManyField('multimedia.Multimedia', related_name='video_intro', null=True, blank=True)
    prerequisites = models.TextField(default="none")
    objectives = models.TextField()
    effort_value = models.IntegerField()
    effort_units = models.CharField(max_length=10)
    last_edited = models.DateTimeField(auto_now=True)

    resources = models.ManyToManyField('multimedia.Multimedia', related_name='resource', null=True, blank=True)
    tags = TaggableManager()

class LessonArticle(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    article = models.ForeignKey('articles.Article')

    suggested_order = models.IntegerField(null=True, blank=True)
    rationale = models.TextField(null=True, blank=True)
    importance = models.CharField(max_length=10, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    tags = TaggableManager()

class LessonComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    lesson = models.ForeignKey('lessons.Lesson')

    def __unicode__(self):
        return unicode("%s: %s" % (self.lesson, self.body[:60]))

class LessonFAQItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=100)
    answer = models.TextField()
    lesson = models.ForeignKey(Lesson)

    def __unicode__(self):
        return unicode("%s: %s" % (self.campaign, self.question[:60]))