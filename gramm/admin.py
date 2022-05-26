from django.contrib import admin

# Register your models here.

from .models import Yoba, Tags

admin.site.register(Yoba)
admin.site.register(Tags)
