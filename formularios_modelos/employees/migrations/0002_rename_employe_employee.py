# Generated by Django 4.2 on 2023-04-26 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employe',
            new_name='Employee',
        ),
    ]
