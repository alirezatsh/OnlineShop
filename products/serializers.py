from rest_framework import serializers
from .models import (Phone, PhoneImage , Tablet , 
                     TabletImage , SmartWatchImage , SmartWatch 
                     , AirPods , AirPodImage , Brand , Accessory  , AccessoryType , AccessoryImage , Color )
from django.db.models import Q


class TurnIdIntoString(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all())
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand'] = instance.brand.name if instance.brand else None
        representation['color'] = instance.color.name if instance.color else None
        
        return representation




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


class PhoneSerializer(TurnIdIntoString):
    images = PhoneImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_phones = serializers.SerializerMethodField()
    comparison = serializers.PrimaryKeyRelatedField(
        queryset=Phone.objects.all(),
        allow_null=True
        ,required=False

    )

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
            PhoneImage.objects.create(phone=instance, image=image)

        return instance

    def get_similar_phones(self, obj):
      if obj.name and len(obj.name.split()) > 0:   
        similar_phones = Phone.objects.filter(
            RAM=obj.RAM,
            InnerMemory=obj.InnerMemory,
            brand=obj.brand,
            price__gte=obj.price - 1000000,
            price__lte=obj.price + 1000000
        ).exclude(id=obj.id)[:5]  

        return SimilarPhoneSerializer(similar_phones, many=True).data

    def get_final_price(self, obj):
        if obj.discount and obj.discount > 0:
            return obj.price - obj.discount
        return obj.price  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        similar_phones_data = self.get_similar_phones(instance)
        representation['similar_phones'] = similar_phones_data
        
        if instance.comparison:
            comparison_data = PhoneSerializer(instance.comparison).data
            representation['comparison'] = comparison_data
        
        return representation
 


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


class TabletSerializer(TurnIdIntoString):
    images = TabletImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_tablets = serializers.SerializerMethodField() 
    comparison = serializers.PrimaryKeyRelatedField(
        queryset=Tablet.objects.all(),
        allow_null=True
        ,required=False
    )

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
        similar_tablets = Tablet.objects.filter(
            RAM=obj.RAM,
            InnerMemory=obj.InnerMemory,
            brand=obj.brand,
            price__gte=obj.price - 1000000,
            price__lte=obj.price + 1000000
        ).exclude(id=obj.id)[:5]  

        return SimilarTabletSerializer(similar_tablets, many=True).data

    def get_final_price(self, obj):
        if obj.discount and obj.discount > 0:
            return obj.price - obj.discount
        return obj.price  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        similar_tablets_data = self.get_similar_tablets(instance)
        representation['similar_tablets'] = similar_tablets_data
        
        if instance.comparison:
            comparison_data = TabletSerializer(instance.comparison).data
            representation['comparison'] = comparison_data
        
        return representation


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


class SmartWatchSerializer(TurnIdIntoString):
    images = SmartWatchImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_smartwatch = serializers.SerializerMethodField()
    comparison = serializers.PrimaryKeyRelatedField(
        queryset=SmartWatch.objects.all(),
        allow_null=True
        ,required=False

    )

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
            RAM=obj.RAM,
            InnerMemory=obj.InnerMemory,
            brand=obj.brand,
            price__gte=obj.price - 1000000,
            price__lte=obj.price + 1000000
        ).exclude(id=obj.id)[:5]  

        return SimilarSmartWatchSerializer(similar_smartwatch, many=True).data

    def get_final_price(self, obj):
        if obj.discount and obj.discount > 0:
            return obj.price - obj.discount
        return obj.price  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        similar_smartwatch_data = self.get_similar_smartwatch(instance)
        representation['similar_smartwatch'] = similar_smartwatch_data
        
        if instance.comparison:
            comparison_data = SmartWatchSerializer(instance.comparison).data
            representation['comparison'] = comparison_data
        
        return representation


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


class AirPodSerializer(TurnIdIntoString):
    images = AirPodImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_airpods = serializers.SerializerMethodField()
    comparison = serializers.PrimaryKeyRelatedField(
        queryset=AirPods.objects.all(),
        allow_null=True
        ,required=False

    )

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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.comparison:
            comparison_data = AirPodSerializer(instance.comparison).data
            representation['comparison'] = comparison_data
        return representation


        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'        
        
        
class AccessoryImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Accessory
        fields = ['image']

class SimilarAccessorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Accessory
        fields = ['name', 'image', 'price']

    def get_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None
        


class AccessorySerializer(TurnIdIntoString):
    ProductType = serializers.PrimaryKeyRelatedField(queryset=AccessoryType.objects.all())
    images = AccessoryImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    similar_accessories = serializers.SerializerMethodField()
    comparison = serializers.PrimaryKeyRelatedField(
        queryset=Accessory.objects.all(),
        allow_null=True
        ,required=False

    )

    class Meta:
        model = Accessory
        fields = '__all__'

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 images.")
        return value

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        accessory = Accessory.objects.create(**validated_data)

        for image in uploaded_images:
            AccessoryImage.objects.create(accessory=accessory, image=image)

        return accessory

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for image in uploaded_images:
            AccessoryImage.objects.create(accessory=instance, image=image)

        return instance
    
    def get_similar_accessories(self, obj):
        similar_accessories = Accessory.objects.filter(
            Q(name__icontains=obj.name.split()[0])
        ).exclude(id=obj.id)[:5]
        return SimilarAccessorySerializer(similar_accessories, many=True).data


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ProductType'] = instance.ProductType.name if instance.ProductType else None
        product_type = instance.ProductType.name.lower() if instance.ProductType else ''
        
        if product_type == 'powerbonk':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' ,
                              'brand' , 'capacity' , 'compatibility' , 'InputPort' , 'NumberOfOutputPorts' , 
                              'TotalOutputPower', 'DimensionsWeights' , 'BodyMaterial' , 'LEDIndicator' , 
                              'FastCharging' , 'WirelessCharging' , 'TechnicalSpecifications' , 'IncludedItems' ,
                              'ControlsKeys' , 'resistance' , 'ConnectedCable' , 'SimultaneousCharging' , 
                              'InputCurrentIntensity' , 'InputVoltage' , 'OutputCurrentIntensity' , 'OutputVoltage' , 
                              'OtherFeatures' , 'battery' , 'capacityInWH' , 'NominalCapacity' , 'ProductID' ]
            
        elif product_type == 'headphone':
            allowed_fields = ['id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand',
                              'bluetooth' , 'NFC' , 'CableLength' , 'MultipleConnection' , 'microphone' ,
                              'InterfaceType' , 'jack' , 'ResponseFrequency' , 'Impedance' , 'DriverDiameter' , 
                              'VoiceControl' , 'ANC' , 'sensitivity' , 'USBPort' , 'buttons' , 'type' , 'VoiceAssistant' ,
                              'SuitableFor' , 'SpecialFeatures' , 'PowerSource' , 'DimensionsWeights' , 'ProductID',
                              'compatibility' , 'resistance' , 'IncludedItems' , 'BodyMaterial' , 'OtherFeatures'
                              ]
            
        elif product_type == 'speaker':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' ,
                              'screen' , 'RemoteControl' , 'AUXGate' , 'ConnectOtherSpeakers' , 'BatteryEfficiency' ,
                              'ChargingTime' , 'MemoryCardSupport' , 'SideMicrophone' , 'DanceOfLight' , 'NumberOfSubWoofers' ,
                              'SubWooferDimensions' , 'MicrophoneInput' , 'HeadphoneOutput' , 'PerformanceRange' , 'ConversationMicrophone'
                              , 'BatteryCapacity' , 'radio' , 'AudioTechnologies' , 'ports' , 'InputPower' , 'OutputPower' , 'ControlsKeys' , 'OtherFeatures'
                              'ConnectionType' , 'bluetooth' , 'PowerSource' , 'DimensionsWeights' , 'IncludedItems' ,
                              'BodyMaterial' , 'resistance' , 'USBPort' , 'sensitivity' , 'battery' , 'ProductID' , 'VoiceAssistant'
                              ]
            
        elif product_type == 'keyboard':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' ,
                              'ConnectionType' , 'NumberOfKeys' , 'CompatibleOs' , 'NumberOfKeystrokes' , 'lighting' , 'TypeOfKeyboard' , 'WristSupport' , 'TypeOfSwitch' , 
                              'ColorOfSwitch' , 'AntiGhosting' , 'NumberOfBatteries' , 'KeyboardBoard' , 'DimensionsWeights' ,
                              'PowerSource' , 'ProductID' , 'OtherFeatures' , 
                              ]
            
        elif product_type == 'flash':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'TransferSpeed' , 'InterfaceTechnology' , 'StandardSpeed' , 'DimensionsWeights' , 
                              'resistance' , 'capacity' , 'ProductID' , 'OtherFeatures' , 'PowerSource' , 
                              ]
            
        elif product_type == 'aux':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'CableLength' , 'CableMaterial' , 'TypeOfCable' , 'CommunicationPorts' ,
                              'NumberOfOutputGate' , 'SuitableFor' , 'OtherFeatures' , ''
                              ]
            
        elif product_type == 'memorycard':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'ReadingSpeed' , 'temperature' , 'WritingSpeed' , 'capacity' , 'DimensionsWeights' , 'resistance' , 'ProductID' , ''
                              ]
            
        elif product_type == 'charger':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'IncludeCable' , 'ChargingPower' , 'NumberOfOutputPorts' , 'ChargingFeatures' , 'PartNumber' ,
                              'OutputVoltage' , 'SuitableFor' , 'InputVoltage' , 'ProductID' , 'OtherFeatures' , 'InputCurrentIntensity' , 'OutputCurrentIntensity'
                              ]
            
        elif product_type == 'chargingcable':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'InterfaceType' , 'CableLength' , 'SuitableFor' , 'OtherFeatures' , 'compatibility' , 'FastCharging' , 'CableMaterial'
                              ]
            
        elif product_type == 'phonecase':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'material' , 'structure' , 'CoverLevel' , 'SuitableFor' , 'SpecialFeatures' , '' , '' , ''
                              ]
            
        elif product_type == 'watchband':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'LockType' , 'size' , 'SuitableFor' , 'BodyMaterial' , 'OtherFeatures' , 
                              ]
            
        elif product_type == 'watchcover':
            allowed_fields = [ 'id' , 'name', 'color', 'ProductType' , 'price' , 'discount' , 'FinalPrice' , 'review' ,'uploaded_images' , 'images' , 'comparison' , 'brand' , 
                              'SuitableFor' , 'OtherFeatures' 
                              ]
            
        else:
            allowed_fields = ['id', 'name', 'ProductType']
        
        return {key: representation[key] for key in allowed_fields if key in representation}


class AccessoryTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccessoryType
        fields = '__all__'