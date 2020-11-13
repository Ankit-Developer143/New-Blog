# Generated by Django 3.1.2 on 2020-11-12 15:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201112_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
