# Generated by Django 5.0.1 on 2024-03-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0028_alter_payment_pay_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_type',
            field=models.CharField(default='', max_length=30),
        ),
    ]
