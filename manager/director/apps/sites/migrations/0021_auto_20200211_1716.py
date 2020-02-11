# Generated by Django 2.2.10 on 2020-02-11 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0020_auto_20200210_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='dockerimage',
            name='friendly_name',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='dockerimage',
            name='is_user_visible',
            field=models.BooleanField(default=False),
        ),
    ]
