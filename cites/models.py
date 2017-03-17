from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

#########################################
class Citing(models.Model):
    title = models.CharField(max_length=1000)
    cited_date = models.DateTimeField('date of citation', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.title

#########################################
class Publication(models.Model):
    title = models.CharField(max_length=1000)
    is_my = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)
    last_modified_date = models.DateTimeField('date last modified', default=timezone.now)
    citations = models.ManyToManyField(Citing, through='Citation')

    def __str__(self):
        return self.title

#########################################
class Citation(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    citing = models.ForeignKey(Citing, on_delete=models.CASCADE)
    cited_date = models.DateTimeField('date of citation', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)


