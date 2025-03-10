# Generated by Django 5.1.2 on 2024-11-15 20:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_phoneimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='RefreshRate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
