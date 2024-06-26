# Generated by Django 5.0.1 on 2024-03-23 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_alter_feedback_date_alter_inquiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.profile')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
