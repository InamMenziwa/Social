# Generated by Django 5.0.4 on 2024-04-12 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='proto',
            new_name='photo',
        ),
    ]
