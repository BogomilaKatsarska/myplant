# Generated by Django 3.2.19 on 2023-06-28 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlantModel',
            new_name='Plant',
        ),
        migrations.RenameModel(
            old_name='Model',
            new_name='Profile',
        ),
    ]
