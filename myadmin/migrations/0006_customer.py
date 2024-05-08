# Generated by Django 5.0.1 on 2024-03-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_rename_discription_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
