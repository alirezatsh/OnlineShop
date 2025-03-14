# Generated by Django 5.1.2 on 2024-11-21 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_smartwatch_isfake'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirPods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('FinalPrice', models.PositiveIntegerField(editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('IsFake', models.BooleanField(default=False)),
                ('resistance', models.CharField(blank=True, max_length=100, null=True)),
                ('connectionType', models.CharField(blank=True, max_length=50, null=True)),
                ('bluetooth', models.CharField(blank=True, max_length=100, null=True)),
                ('ANC', models.BooleanField(default=False)),
                ('BodyMaterial', models.CharField(blank=True, max_length=50, null=True)),
                ('LEDIndicator', models.BooleanField(default=False)),
                ('PlaceHeadphones', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('InterfaceType', models.CharField(blank=True, max_length=50, null=True)),
                ('microphone', models.BooleanField(default=False)),
                ('MicrophoneInfo', models.CharField(blank=True, max_length=300, null=True)),
                ('VoiceAssistant', models.BooleanField(default=False)),
                ('ResponseFrequency', models.CharField(blank=True, max_length=50, null=True)),
                ('DriverDiameter', models.CharField(blank=True, max_length=50, null=True)),
                ('PerformanceRange', models.CharField(blank=True, max_length=50, null=True)),
                ('OtherFeatures', models.CharField(blank=True, max_length=500, null=True)),
                ('BatteryCapacity', models.CharField(blank=True, max_length=100, null=True)),
                ('BatteryAgeMusic', models.CharField(blank=True, max_length=300, null=True)),
                ('BatteryAgeStandBy', models.CharField(blank=True, max_length=300, null=True)),
                ('BatteryAgeConversation', models.CharField(blank=True, max_length=300, null=True)),
                ('ChargingTime', models.CharField(blank=True, max_length=100, null=True)),
                ('DimensionsWeights', models.CharField(blank=True, max_length=100, null=True)),
                ('buttons', models.CharField(blank=True, max_length=300, null=True)),
                ('VoiceControl', models.BooleanField(default=False)),
                ('AcousticType', models.CharField(blank=True, max_length=100, null=True)),
                ('SpecialFeatures', models.CharField(blank=True, max_length=300, null=True)),
                ('battery', models.CharField(blank=True, max_length=50, null=True)),
                ('BatteryEfficiency', models.CharField(blank=True, max_length=100, null=True)),
                ('ProductID', models.CharField(blank=True, max_length=150, null=True)),
                ('compatibility', models.CharField(blank=True, max_length=50, null=True)),
                ('MultipleConnection', models.BooleanField(default=False)),
                ('jack', models.BooleanField(default=False)),
                ('Impedance', models.CharField(blank=True, max_length=50, null=True)),
                ('MagnetType', models.CharField(blank=True, max_length=50, null=True)),
                ('IncludedItems', models.CharField(blank=True, max_length=100, null=True)),
                ('USBPort', models.CharField(blank=True, max_length=50, null=True)),
                ('sensitivity', models.CharField(blank=True, max_length=50, null=True)),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.review')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AirPodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='airpod_images/')),
                ('airpod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.airpods')),
            ],
        ),
    ]
