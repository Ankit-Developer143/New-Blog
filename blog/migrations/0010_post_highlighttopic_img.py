# Generated by Django 3.1.2 on 2020-11-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201111_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Highlighttopic_img',
            field=models.ImageField(null=True, upload_to='Highlighttopic_img'),
        ),
    ]
