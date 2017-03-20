from django.contrib import admin

from .models import Publication, Citation

# Register your models here.
admin.site.register(Publication)
admin.site.register(Citation)
