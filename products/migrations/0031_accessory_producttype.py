# Generated by Django 5.1.2 on 2024-11-27 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_accessorytype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='ProductType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='products.accessorytype'),
        ),
    ]
