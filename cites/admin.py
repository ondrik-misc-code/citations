from django.contrib import admin

from .models import Author, Citation, Publication

# Register your models here.
admin.site.register(Author)
admin.site.register(Citation)
admin.site.register(Publication)
