# Generated by Django 5.0.1 on 2024-03-18 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_feedback_date_alter_inquiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 18)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 18)),
        ),
    ]
