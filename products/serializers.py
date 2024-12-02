from rest_framework import serializers
from .models import (Phone, PhoneImage , Review , Tablet , 
                     TabletImage , SmartWatchImage , SmartWatch 
                     , AirPods , AirPodImage , Brand , Accessory  , AccessoryType , Color)
from django.db.models import Q


class PhoneImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = PhoneImage
        fields = ['image']

class SimilarPhoneSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = ['name', 'image', 'price']

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None


class PhoneSerializer(serializers.ModelSerializer):
    images = PhoneImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_phones = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = '__all__'

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 images.")
        return value

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        phone = Phone.objects.create(**validated_data)

        for image in uploaded_images:
            PhoneImage.objects.create(phone=phone, image=image)

        return phone

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for image in uploaded_images:
            TabletImage.objects.create(tablet=instance, image=image)

        return instance

    def get_similar_phones(self, obj):
        similar_phones = Phone.objects.filter(
            Q(name__icontains=obj.name.split()[0])
        ).exclude(id=obj.id)[:5]
        return SimilarPhoneSerializer(similar_phones, many=True).data


class TabletImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = TabletImage
        fields = ['image']


class SimilarTabletSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Tablet
        fields = ['name', 'image', 'price']

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None


class TabletSerializer(serializers.ModelSerializer):
    images = TabletImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_tablets = serializers.SerializerMethodField()

    class Meta:
        model = Tablet
        fields = '__all__'

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 images.")
        return value

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        tablet = Tablet.objects.create(**validated_data)

        for image in uploaded_images:
            TabletImage.objects.create(tablet=tablet, image=image)

        return tablet

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for image in uploaded_images:
            TabletImage.objects.create(tablet=instance, image=image)

        return instance

    def get_similar_tablets(self, obj):
        # پیدا کردن محصولات مشابه
        similar_tablets = Tablet.objects.filter(
            RAM=obj.RAM,
            InnerMemory=obj.InnerMemory,
            brand=obj.brand,
            price__gte=obj.price - 1000000,
            price__lte=obj.price + 1000000
        ).exclude(id=obj.id)[:5] 

        return TabletSerializer(similar_tablets, many=True).data

    def get_final_price(self, obj):
        if obj.discount and obj.discount > 0:
            return obj.price - obj.discount
        return obj.price  


    





class SmartWatchImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = SmartWatch
        fields = ['image']

class SimilarSmartWatchSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SmartWatch
        fields = ['name', 'image', 'price']

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None


class SmartWatchSerializer(serializers.ModelSerializer):
    images = SmartWatchImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_smartwatch = serializers.SerializerMethodField()

    class Meta:
        model = SmartWatch
        fields = '__all__'

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 images.")
        return value

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        smartwatch = SmartWatch.objects.create(**validated_data)

        for image in uploaded_images:
            SmartWatchImage.objects.create(smartwatch=smartwatch, image=image)

        return smartwatch

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for image in uploaded_images:
            SmartWatchImage.objects.create(smartwatch=instance, image=image)

        return instance

    def get_similar_smartwatch(self, obj):
        similar_smartwatch = SmartWatch.objects.filter(
            Q(name__icontains=obj.name.split()[0])
        ).exclude(id=obj.id)[:5]
        return SimilarSmartWatchSerializer(similar_smartwatch, many=True).data


class AirPodImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = AirPods
        fields = ['image']

class SimilarAirPodSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AirPods
        fields = ['name', 'image', 'price']

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None


class AirPodSerializer(serializers.ModelSerializer):
    images = AirPodImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_airpods = serializers.SerializerMethodField()

    class Meta:
        model = AirPods
        fields = '__all__'

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 images.")
        return value

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        airpod = AirPods.objects.create(**validated_data)

        for image in uploaded_images:
            AirPodImage.objects.create(airpod=airpod, image=image)

        return airpod

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for image in uploaded_images:
            AirPodImage.objects.create(airpod=instance, image=image)

        return instance

    def get_similar_airpods(self, obj):
        similar_airpods = AirPods.objects.filter(
            Q(name__icontains=obj.name.split()[0])
        ).exclude(id=obj.id)[:5]
        return SimilarAirPodSerializer(similar_airpods, many=True).data



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'        
        


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product_type = instance.ProductType.name.lower()
        
        if product_type == 'پاوربانک':
            allowed_fields = ['id', 'name', 'color', 'ProductType']
        elif product_type == 'شارژر':
            allowed_fields = ['id', 'name', 'capacity' , 'ProductType']
        elif product_type == 'فلش':
            allowed_fields = ['id', 'name', 'battery', 'ProductType']
        else:
            allowed_fields = ['id', 'name', 'ProductType']

        return {key: representation[key] for key in allowed_fields}
