# Generated by Django 4.1.7 on 2023-04-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0012_fish_e_fish_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='E_fish_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
