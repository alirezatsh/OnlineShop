# Generated by Django 5.1.2 on 2024-11-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_phone_price_alter_tablet_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='OtherFeatures',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='OtherFeatures',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
