# Generated by Django 5.0.1 on 2024-03-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
