from django.db import models
from taggit.managers import TaggableManager
from exercises.models import Exercise
from multimedia.models import Multimedia


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=34)
    moderators = models.ManyToManyField('accounts.Account', related_name='article_moderator', null=True, blank=True)
    created_by = models.ForeignKey('accounts.Account', related_name='article_creator', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    heading = models.CharField(max_length=50)
    body = models.TextField()
    resources = models.ManyToManyField('multimedia.Multimedia', null=True, blank=True)
    endline = models.CharField(max_length=50, null=True, blank=True)
    summation = models.TextField(null=True, blank=True)
    exercises = models.ManyToManyField('exercises.Exercise', null=True, blank=True)
    tags = TaggableManager()
    main = models.BooleanField()

class Tab(models.Model):
    STYLE_CHOICES = (
        ('B', 'Bullet'),
        ('I', 'Image'),
        ('M', 'Multimedia'),
        ('T', 'Text'),
    )
    article = models.ForeignKey('articles.Article')
    subheading = models.CharField(max_length=50)
    style = models.CharField(max_length=2, default='B', choices=STYLE_CHOICES)
    media_resource = models.ManyToManyField('multimedia.Multimedia', null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    field_one = models.TextField(null=True, blank=True)
    field_two = models.TextField(null=True, blank=True)
    field_three = models.TextField(null=True, blank=True)

class ArticleComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Account', related_name="%(app_label)s_%(class)s_related", null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    article = models.ForeignKey('articles.Article')

    def __unicode__(self):
        return unicode("%s: %s" % (self.article, self.body[:60]))