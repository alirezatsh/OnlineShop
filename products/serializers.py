from rest_framework import serializers
from .models import Phone, PhoneImage , Review
from django.db.models import Q


class PhoneImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = PhoneImage
        fields = ['image']

class PhoneSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    similar_phones = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = '__all__'

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]
    
    def get_similar_phones(self, obj):
        similar_phones = Phone.objects.filter(
            Q(name__icontains=obj.name.split()[0])  
        ).exclude(id=obj.id)[:5]
        return SimilarPhoneSerializer(similar_phones, many=True).data

    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
        
        


class SimilarPhoneSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = ['name', 'image', 'price' ]

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None



    
