# Generated by Django 5.0.1 on 2024-03-17 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_inquiry_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 17)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 17)),
        ),
    ]
