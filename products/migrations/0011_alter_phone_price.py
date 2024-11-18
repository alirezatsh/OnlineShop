# Generated by Django 5.1.2 on 2024-11-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_phone_discount_phone_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]