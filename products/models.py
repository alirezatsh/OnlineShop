from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from decimal import Decimal

class Review(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextUploadingField()

class BaseProduct(models.Model):
    price = models.PositiveIntegerField(default=0) 
    discount = models.PositiveIntegerField(default=0)  
    FinalPrice = models.PositiveIntegerField(editable=False, null=True)
    review = models.ForeignKey(Review , on_delete=models.CASCADE , blank=True , null=True)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if 0 <= self.discount <= 100:
            discount_factor = Decimal(1) - (Decimal(self.discount) / 100)
            self.FinalPrice = self.price * discount_factor
        else:
            self.FinalPrice = self.price
        super().save(*args, **kwargs)


    
class Phone(BaseProduct):
    name = models.CharField(max_length=100, blank=True, null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    InnerMemory = models.CharField(max_length=50, blank=True, null=True)
    RAM = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    BackCamera = models.CharField(max_length=100, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    Frequency = models.CharField(max_length=100, blank=True, null=True)
    NumberOfProcessor = models.CharField(max_length=50, blank=True, null=True)
    GPU = models.CharField(max_length=50, blank=True, null=True)
    NumberOfSimCard = models.CharField(max_length=50, blank=True, null=True)
    CameraQuality = models.CharField(max_length=100, blank=True, null=True)
    OS = models.CharField(max_length=100, blank=True, null=True)
    DimensionsWeights = models.CharField(max_length=100, blank=True, null=True)
    IncludedItems = models.CharField(max_length=100, blank=True, null=True)
    TypeOfMemoryCard = models.CharField(max_length=100, blank=True, null=True)
    TypeOfMemory = models.CharField(max_length=50, blank=True, null=True)
    TypeOfScreen = models.CharField(max_length=50, blank=True, null=True)
    SizeOfScreen = models.CharField(max_length=50, blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    LightOfScreen = models.CharField(max_length=100, blank=True, null=True)
    ScreenToBody = models.CharField(max_length=50, blank=True, null=True)
    ScreenRatio = models.CharField(max_length=50, blank=True, null=True)
    PixelDensity = models.CharField(max_length=50, blank=True, null=True)
    RefreshRate = models.CharField(max_length=100 , blank=True, null=True)
    ScreenSaver = models.CharField(max_length=50, blank=True, null=True)
    WideCamera = models.CharField(max_length=100, blank=True, null=True)
    UltraWideCamera = models.CharField(max_length=100, blank=True, null=True)
    MacroCamera = models.CharField(max_length=100, blank=True, null=True)
    FilmingBackCamera = models.CharField(max_length=50, blank=True, null=True)
    Flash = models.CharField(max_length=50, blank=True, null=True)
    FrontCamera = models.CharField(max_length=50, blank=True, null=True)
    WideFrontCamera = models.CharField(max_length=100, blank=True, null=True)
    FilmingFrontCamera = models.CharField(max_length=50, blank=True, null=True)
    OtherFeatures = models.CharField(max_length=500, blank=True, null=True)
    InternetNetwork = models.CharField(max_length=50, blank=True, null=True)
    SupportedNetwork = models.CharField(max_length=100, blank=True, null=True)
    USBPort = models.CharField(max_length=50, blank=True, null=True)
    OTG = models.BooleanField(default=False)
    USBCharging = models.BooleanField(default=False)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    jack = models.BooleanField(default=False)
    WiFiNetwork = models.CharField(max_length=100, blank=True, null=True)
    HotSpot = models.BooleanField(default=False)
    NFC = models.BooleanField(default=False)
    GPS = models.CharField(max_length=50, blank=True, null=True)
    infrared = models.BooleanField(default=False)
    speaker = models.CharField(max_length=50, blank=True, null=True)
    Sensors = models.CharField(max_length=150, blank=True, null=True)
    resistance = models.CharField(max_length=100, blank=True, null=True)
    radio = models.BooleanField(default=False)
    BatteryCapacity = models.CharField(max_length=100, blank=True, null=True)
    FastCharging = models.CharField(max_length=100, blank=True, null=True)
    AntiWater = models.BooleanField(default=False)
    VoiceAssistant = models.CharField(max_length=50, blank=True, null=True)
    WirelessCharging = models.BooleanField(default=False)
    ReverseCharging = models.BooleanField(default=False)
    ProductID = models.CharField(max_length=150, blank=True, null=True)
    ChargingPort = models.CharField(max_length=50, blank=True, null=True)
  

   

    def __str__(self):
        return self.name or "Unnamed Phone"

class PhoneImage(models.Model):
    phone = models.ForeignKey(Phone, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone_images/')

    def __str__(self):
        return f"Image of {self.phone.name}"
    
    
class Tablet(BaseProduct):
    name = models.CharField(max_length=100, blank=True, null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    InnerMemory = models.CharField(max_length=50, blank=True, null=True)
    RAM = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    CameraQuality = models.CharField(max_length=200, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    NumberOfProcessor = models.CharField(max_length=50, blank=True, null=True)
    GPU = models.CharField(max_length=50, blank=True, null=True)
    DimensionsWeights = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    TypeOfOs = models.CharField(max_length=50, blank=True, null=True)
    NumberOfSimCard = models.CharField(max_length=50, blank=True, null=True)
    TypeOfScreen = models.CharField(max_length=50, blank=True , null=True)
    SizeOfScreen = models.CharField(max_length=50 , blank=True , null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    MultiTouch = models.CharField(max_length=50 , blank=True , null=True)
    ScreenFeatures = models.CharField(max_length=100 , blank=True , null=True)
    ScreenStandard = models.CharField(max_length=50 , blank=True , null=True)
    PixelDensity = models.CharField(max_length=50, blank=True, null=True)
    FilmingQuality = models.CharField(max_length=100 , blank=True , null=True)
    FrontCamera = models.CharField(max_length=50 , blank=True , null=True)
    BackCamera = models.CharField(max_length=50 , blank=True , null=True)
    USBPort = models.CharField(max_length=150, blank=True, null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    SoundPlug = models.BooleanField(default=False )
    WiFiNetwork = models.CharField(max_length=100, blank=True, null=True)
    HotSpot = models.BooleanField(default=False)
    HDMI = models.CharField(max_length=100, blank=True, null=True)
    Sensors = models.CharField(max_length=150, blank=True, null=True)
    OtherFeatures = models.CharField(max_length=500, blank=True, null=True)
    BatteryCapacity = models.CharField(max_length=100, blank=True, null=True)
    replaceable = models.BooleanField(default=False )
    ConversationAbility = models.BooleanField(default=False)
    IncludedItems = models.CharField(max_length=100, blank=True, null=True)
    pen = models.BooleanField(default=False)
    SIMCardSupport = models.BooleanField(default=False)
    BodyMaterial = models.CharField(max_length=50 , blank=True , null=True)
    SuitableFor = models.CharField(max_length=50 , blank=True , null=True)
    ScreenToBody = models.CharField(max_length=50, blank=True, null=True)
    ScreenRatio = models.CharField(max_length=50, blank=True, null=True)
    RefreshRate = models.CharField(max_length=100 , blank=True, null=True)
    ScreenSaver = models.CharField(max_length=100, blank=True, null=True)
    WideCamera = models.CharField(max_length=50 , blank=True , null=True)
    UltraWideCAmera = models.CharField(max_length=50 , blank=True , null=True)
    DepthSensor = models.CharField(max_length=50 , blank=True , null=True) 
    LightOfScreen = models.CharField(max_length=100, blank=True, null=True)
    TypeOfMemoryCard = models.CharField(max_length=50 , blank=True , null=True)
    CameraHardware = models.CharField(max_length=150 , blank=True , null=True) 
    FrontCameraFeatures = models.CharField(max_length=150 , blank=True , null=True)
    Flash = models.CharField(max_length=50, blank=True, null=True)
    OTG = models.BooleanField(default=False)
    USBCharging = models.BooleanField(default=False)
    NFC = models.BooleanField(default=False)
    GPS = models.CharField(max_length=50, blank=True, null=True)
    radio = models.BooleanField(default=False)
    FastCharging = models.CharField(max_length=100, blank=True, null=True)
    WirelessCharging = models.BooleanField(default=False)
    DigitalZoom = models.CharField(max_length=50 , blank=True , null=True)
    resistance = models.CharField(max_length=100, blank=True, null=True)
    ChargingPort = models.CharField(max_length=50, blank=True, null=True)
    ProductID = models.CharField(max_length=150, blank=True, null=True)
   
   
    def __str__(self):
       return f'{self.id} - {self.name}'
   



class TabletImage(models.Model):
    tablet = models.ForeignKey(Tablet, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tablet_images/')

    def __str__(self):
        return f"Image of {self.tablet.name}"






    

    


