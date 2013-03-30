from django.db import models
from lessons.models import Lesson
from taggit.managers import TaggableManager
from filebrowser.fields import FileBrowseField


# Create your models here.
class Plan(models.Model):
    CATEGORY_CHOICES = (
        ('S', 'Single'),
        ('A', 'Attached'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('C', "It's complicated"),
    )
    SUBCATEGORY_CHOICES = (
        ('S', 'Single'),
        ('M', 'Medical'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('C', "It's complicated"),
    )
    LEVEL_CHOICES = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('S', 'Senior'),
        ('U', 'Undergraduate'),
        ('A', 'Advanced'),
        ('G', "Graduate"),
    )
    lessons = models.ManyToManyField('lessons.Lesson', through='LessonPlan')
    category = models.CharField(max_length=2, default='C', choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=2, default='C', choices=SUBCATEGORY_CHOICES)
    title = models.CharField(max_length=50)
    plan_dp = FileBrowseField("Image", max_length=200, extensions=[".jpg", ".png", ".gif"], blank=True, null=True)
    description = models.TextField()
    goal = models.TextField()
    level = models.CharField(max_length=2, default='B', choices=LEVEL_CHOICES)
    last_edited = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

class LessonPlan(models.Model):
    plan = models.ForeignKey('plans.Plan')
    lessons = models.ForeignKey('lessons.Lesson')

    suggested_order = models.IntegerField(null=True, blank=True)
    rationale = models.TextField(null=True, blank=True)
    importance = models.CharField(max_length=10, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    tags = TaggableManager()