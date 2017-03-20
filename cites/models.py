from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

#########################################
class Citation(models.Model):
    """A work citing the author's publication."""
    title = models.CharField(max_length=1000)
    cited_date = models.DateTimeField('date of citation', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.title

#########################################
class Author(models.Model):
    """An author."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

#########################################
class ValidPubManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

#########################################
class Publication(models.Model):
    """An author's publication."""
    abbrev = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=1000)
    citations = models.ManyToManyField(Citation, through='PublicationCitation')
    authors = models.ManyToManyField(Author, through='PublicationAuthor')
    deleted = models.BooleanField(default=False)

    pub_date = models.DateTimeField('date published', default=timezone.now)
    created_date = models.DateTimeField('date created', default=timezone.now)
    last_modified_date = models.DateTimeField('date last modified', default=timezone.now)

    # managers for accessing the collection
    objects = ValidPubManager()
    also_deleted_objects = models.Manager()

    def __str__(self):
        return self.abbrev + ": " + self.title

#########################################
class PublicationCitation(models.Model):
    """Relation table binding publication with its citations."""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    citation = models.ForeignKey(Citation, on_delete=models.CASCADE)

#########################################
class PublicationAuthor(models.Model):
    """Relation table binding publication with its authors."""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
