# Generated by Django 5.0.1 on 2024-03-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0027_remove_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_type',
            field=models.CharField(blank=True, default='Online', max_length=30, null=True),
        ),
    ]
