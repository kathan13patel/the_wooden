# Generated by Django 5.0.1 on 2024-04-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0030_alter_payment_options_alter_feedback_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='order',
            name='pay_type',
            field=models.CharField(default='', max_length=30),
        ),
    ]
