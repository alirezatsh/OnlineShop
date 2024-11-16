# Generated by Django 5.1.2 on 2024-11-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_phone_discount_phone_final_price_phone_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='phone',
            name='final_price',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
