# Generated by Django 5.1.2 on 2024-11-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_phone_discount_phone_final_price_alter_phone_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='final_price',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='price',
        ),
    ]
