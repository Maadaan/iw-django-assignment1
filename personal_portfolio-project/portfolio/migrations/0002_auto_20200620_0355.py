# Generated by Django 2.2.10 on 2020-06-20 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titleman',
            new_name='title',
        ),
    ]
