# Generated by Django 2.2.12 on 2020-04-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0036_auto_20200329_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockerimage',
            name='friendly_name',
            field=models.CharField(blank=True, default=None, help_text='Will be shown to the user.', max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dockerimagesetupcommand',
            name='name',
            field=models.CharField(help_text="A short name describing what the command does. If the command is OS/language-specific, please use prefixes like this for consistency:'[OS:Alpine] Fix timezone setup', '[Lang:Python] Install virtualenv with Pip'", max_length=50),
        ),
    ]
