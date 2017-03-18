from django.contrib import admin

from .models import Publication, Citing

# Register your models here.
admin.site.register(Publication)
admin.site.register(Citing)
