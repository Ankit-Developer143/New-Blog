# Generated by Django 3.1.2 on 2020-11-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20201111_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]