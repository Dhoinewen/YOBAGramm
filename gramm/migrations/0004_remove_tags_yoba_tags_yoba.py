# Generated by Django 4.0.4 on 2022-05-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gramm', '0003_alter_tags_yoba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='yoba',
        ),
        migrations.AddField(
            model_name='tags',
            name='yoba',
            field=models.ManyToManyField(to='gramm.yoba'),
        ),
    ]