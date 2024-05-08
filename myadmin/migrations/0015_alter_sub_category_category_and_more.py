# Generated by Django 5.0.1 on 2024-03-19 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0014_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.category'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='sub_cat_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
