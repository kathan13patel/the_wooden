# Generated by Django 5.0.1 on 2024-04-17 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0023_remove_sub_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myadmin.category'),
        ),
    ]