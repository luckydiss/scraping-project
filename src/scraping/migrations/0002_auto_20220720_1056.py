# Generated by Django 3.0.14 on 2022-07-20 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='plug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='plug',
            new_name='slug',
        ),
    ]