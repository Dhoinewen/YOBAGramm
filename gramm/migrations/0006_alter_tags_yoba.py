# Generated by Django 4.0.4 on 2022-05-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gramm', '0005_alter_tags_yoba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='yoba',
            field=models.ManyToManyField(blank=True, to='gramm.yoba'),
        ),
    ]