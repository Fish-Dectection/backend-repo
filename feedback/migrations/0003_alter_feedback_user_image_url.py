# Generated by Django 4.2.1 on 2023-05-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rename_description_feedback_user_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_image_url',
            field=models.ImageField(default='media/default_image.jpg', upload_to=''),
        ),
    ]
