# Generated by Django 3.1.2 on 2020-11-13 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20201113_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('publish',)},
        ),
    ]