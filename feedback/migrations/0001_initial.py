# Generated by Django 4.2.1 on 2023-05-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_name', models.CharField(max_length=50, null=True)),
                ('image_url', models.CharField(max_length=225, null=True)),
                ('description', models.CharField(max_length=225, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
