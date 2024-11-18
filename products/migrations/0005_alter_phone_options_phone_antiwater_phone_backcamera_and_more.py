# Generated by Django 5.1.2 on 2024-11-15 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_phone_description_remove_phone_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Phone', 'verbose_name_plural': 'Phones'},
        ),
        migrations.AddField(
            model_name='phone',
            name='AntiWater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='BackCamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='BatteryCapacity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='CameraQuality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ChargingPort',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='DimensionsWeights',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='FastCharging',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='FilmingBackCamera',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='FilmingFrontCamera',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='Flash',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='Frequency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='FrontCamera',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='GPS',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='GPU',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='HotSpot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='IncludedItems',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='InnerMemory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='InternetNetwork',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='LightOfScreen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='MacroCamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='NFC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='NumberOfProcessor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='NumberOfSimCard',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='OS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='OTG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='OtherFeatures',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='PixelDensity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ProductID',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='RAM',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='RefreshRate',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ReverseCharging',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='ScreenRatio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ScreenSaver',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ScreenToBody',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='Sensors',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='SizeOfScreen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='SupportedNetwork',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='TypeOfMemory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='TypeOfMemoryCard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='TypeOfScreen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='USBCharging',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='USBPort',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='UltraWideCamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='VoiceAssistant',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='WiFiNetwork',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='WideCamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='WideFrontCamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='WirelessCharging',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='battery',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='bluetooth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='cpu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='infrared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='jack',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='radio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='resistance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='resolution',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='speaker',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/', verbose_name='Attachment')),
                ('file_type', models.CharField(choices=[('Photo', 'Photo'), ('Video', 'Video')], max_length=10, verbose_name='File type')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='products.phone', verbose_name='Related Phone')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
    ]