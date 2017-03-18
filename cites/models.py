from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

#########################################
class Citing(models.Model):
    """A work citing the author's publication."""
    title = models.CharField(max_length=1000)
    cited_date = models.DateTimeField('date of citation', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.title

#########################################
class ValidPubManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

#########################################
class Publication(models.Model):
    """An author's publication."""
    title = models.CharField(max_length=1000)
    is_my = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)
    last_modified_date = models.DateTimeField('date last modified', default=timezone.now)
    citations = models.ManyToManyField(Citing, through='Citation')
    deleted = models.BooleanField(default=False)

    # managers for accessing the collection
    objects = ValidPubManager()
    also_deleted_objects = models.Manager()

    def __str__(self):
        return self.title

#########################################
class Citation(models.Model):
    """Relation table binding publication with its citations."""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    citing = models.ForeignKey(Citing, on_delete=models.CASCADE)
