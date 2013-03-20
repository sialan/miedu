from django.db import models
from taggit.models import TaggedItemBase, TagBase, GenericTaggedItemBase

class Activity(TagBase):
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Award(TagBase):
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Certification(TagBase):
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Interest(TagBase):
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Language(TagBase):
    notes = models.TextField(blank=True, null=True)
    proficiency = models.CharField(max_length=34)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Skill(TagBase):
    notes = models.TextField(blank=True, null=True)
    proficiency = models.CharField(max_length=34)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)