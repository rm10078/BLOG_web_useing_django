# Generated by Django 4.0.5 on 2022-07-02 08:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='n_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='n_title', unique=True),
        ),
    ]