# Generated by Django 5.0.1 on 2024-03-19 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0011_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.sub_category'),
        ),
    ]
