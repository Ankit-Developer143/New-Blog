# Generated by Django 3.1.2 on 2020-11-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201111_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='highlight_line',
            field=models.CharField(blank=True, default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
