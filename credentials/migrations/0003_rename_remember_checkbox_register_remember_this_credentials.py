# Generated by Django 3.2.4 on 2021-06-27 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_auto_20210627_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='remember_checkbox',
            new_name='remember_this_credentials',
        ),
    ]
