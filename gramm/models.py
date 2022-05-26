from django.db import models


class Yoba(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=24, db_index=True)
    yobas = models.ManyToManyField(Yoba, blank=True, related_name='tags')

    def __str__(self):
        return self.name