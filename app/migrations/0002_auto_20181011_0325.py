# Generated by Django 2.1.2 on 2018-10-11 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='checking',
            new_name='check_in',
        ),
    ]
