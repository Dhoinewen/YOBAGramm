# Generated by Django 4.0.4 on 2022-05-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gramm', '0006_alter_tags_yoba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='yoba',
        ),
        migrations.AddField(
            model_name='tags',
            name='yobas',
            field=models.ManyToManyField(blank=True, related_name='tags', to='gramm.yoba'),
        ),
    ]