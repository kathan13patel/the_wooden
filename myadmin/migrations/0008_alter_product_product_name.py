# Generated by Django 5.0.1 on 2024-03-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0007_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
    ]