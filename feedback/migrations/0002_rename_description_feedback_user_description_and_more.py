# Generated by Django 4.2.1 on 2023-05-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='description',
            new_name='user_description',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fish_name',
            new_name='user_fish_name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='image_url',
            new_name='user_image_url',
        ),
    ]