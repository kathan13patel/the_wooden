# Generated by Django 5.0.1 on 2024-03-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]
