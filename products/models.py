from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from decimal import Decimal

class Review(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextUploadingField()
    
    def  __str__(self):
        return self.title
    
class Brand(models.Model):
    name = models.CharField(max_length=100 , blank=True , null=True)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=100 , blank=True , null=True)
    
    def __str__(self):
        return self.name

class BaseProduct(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    color = models.ForeignKey(Color , on_delete=models.CASCADE , blank=True , null=True)
    price = models.PositiveIntegerField(default=0) 
    discount = models.PositiveIntegerField(default=0)  
    FinalPrice = models.PositiveIntegerField(editable=False, null=True)
    review = models.ForeignKey(Review , on_delete=models.CASCADE , blank=True , null=True)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE , blank=True , null=True)
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
    cpu = models.CharField(max_length=100, blank=True, null=True)
    comparison = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null=True)
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
    ProductID = models.CharField(max_length=500, blank=True, null=True)
    ChargingPort = models.CharField(max_length=50, blank=True, null=True)
  

   

    def __str__(self):
        return self.name or "Unnamed Phone"

class PhoneImage(models.Model):
    phone = models.ForeignKey(Phone, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone_images/')

    def __str__(self):
        return f"Image of {self.phone.name}"
    
    
class Tablet(BaseProduct):
    cpu = models.CharField(max_length=100, blank=True, null=True)
    comparison = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null=True)
    InnerMemory = models.IntegerField( blank=True, null=True)
    RAM = models.IntegerField( blank=True, null=True)
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
    ProductID = models.CharField(max_length=500, blank=True, null=True)
   
   
    def __str__(self):
       return f'{self.id} - {self.name}'
   



class TabletImage(models.Model):
    tablet = models.ForeignKey(Tablet, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tablet_images/')

    def __str__(self):
        return f"Image of {self.tablet.name}"




class SmartWatch(BaseProduct):
    IsFake = models.BooleanField(default=False)
    comparison = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null=True)
    compatibility = models.CharField(max_length=50 , blank=True , null=True)
    BatteryCapacity = models.CharField(max_length=50 , blank=True , null=True)
    FarsiSupport = models.BooleanField(default=False)
    conversation = models.BooleanField(default=False)
    BatteryEfficiency = models.CharField(max_length=100 , blank=True , null=True)
    UserGroup = models.CharField(max_length=50 , blank=True , null=True)
    DimensionsWeights = models.CharField(max_length=100, blank=True, null=True)
    BodyMaterial = models.CharField(max_length=50 , blank=True , null=True)
    Sensors = models.CharField(max_length=150, blank=True, null=True)
    resistance = models.CharField(max_length=100, blank=True, null=True)
    ReplaceStrap = models.BooleanField(default=False)
    StrapMaterial = models.CharField(max_length=50 , blank=True , null=True)
    WatchFace = models.BooleanField(default=False)
    speaker = models.BooleanField(default=False)
    microphone = models.BooleanField(default=False)
    StrapLock = models.CharField(max_length=50 , blank=True , null=True)
    ScreenType = models.CharField(max_length=50 , blank=True , null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    ImageResolution = models.CharField(max_length=50 , blank=True , null=True)
    ScreenShape = models.CharField(max_length=50 , blank=True , null=True)
    ScreenSize = models.CharField(max_length=50 , blank=True , null=True)
    GPS = models.BooleanField(default=False)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    BatteryCapacity = models.CharField(max_length=100, blank=True, null=True)
    ChargingTime = models.CharField(max_length=50 , blank=True , null=True)
    OtherFeatures = models.CharField(max_length=500, blank=True, null=True)
    OS = models.CharField(max_length=100, blank=True, null=True)
    NFC = models.BooleanField(default=False)
    WiFiNetwork = models.CharField(max_length=100, blank=True, null=True)
    SIMCardSupport = models.BooleanField(default=False)
    ChargingSource = models.CharField(max_length=50 , blank=True , null=True)
    vibration = models.BooleanField(default=False)
    ProductID = models.CharField(max_length=500, blank=True, null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)
    InnerMemory = models.CharField(max_length=50, blank=True, null=True)
    RAM = models.CharField(max_length=50, blank=True, null=True)
    WatchStyle = models.CharField(max_length=50 , blank=True , null=True)
    LightOfScreen = models.CharField(max_length=100, blank=True, null=True)
    ScreenOn = models.BooleanField(default=False)
    SuitableFor = models.CharField(max_length=50 , blank=True , null=True)
    TypeOfMemoryCard = models.CharField(max_length=50 , blank=True , null=True)
    InstallSoftware = models.BooleanField(default=False)
    IncludedItems = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
       return f'{self.id} - {self.name}'
   



class SmartWatchImage(models.Model):
    smartwatch = models.ForeignKey(SmartWatch, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='smartwatch_images/')

    def __str__(self):
        return f"Image of {self.smartwatch.name}"
    
    
class AirPods(BaseProduct):
    IsFake = models.BooleanField(default=False)
    comparison = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null=True)
    resistance = models.CharField(max_length=100, blank=True, null=True)
    ConnectionType = models.CharField(max_length=50 , blank=True , null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    ANC = models.BooleanField(default=False)
    BodyMaterial = models.CharField(max_length=50 , blank=True , null=True)
    LEDIndicator = models.BooleanField(default=False)
    PlaceHeadphones = models.CharField(max_length=50 , blank=True , null=True)
    type = models.CharField(max_length=50 , blank=True , null=True)
    InterfaceType = models.CharField(max_length=50 , blank=True , null=True)
    microphone = models.BooleanField(default=False)
    MicrophoneInfo = models.CharField(max_length=300 , blank=True , null=True)
    VoiceAssistant = models.BooleanField(default=False)
    ResponseFrequency = models.CharField(max_length=50 , blank=True , null=True)
    DriverDiameter = models.CharField(max_length=50 , blank=True , null=True)
    PerformanceRange = models.CharField(max_length=50 , blank=True , null=True)
    OtherFeatures = models.CharField(max_length=500, blank=True, null=True)
    BatteryCapacity = models.CharField(max_length=100, blank=True, null=True)
    BatteryAgeMusic = models.CharField(max_length=300 , blank=True , null=True)
    BatteryAgeStandBy = models.CharField(max_length=300 , blank=True , null=True)
    BatteryAgeConversation = models.CharField(max_length=300 , blank=True , null=True)
    ChargingTime = models.CharField(max_length=100 , blank=True , null=True)
    DimensionsWeights = models.CharField(max_length=100, blank=True, null=True)
    buttons = models.CharField(max_length=300 , blank=True , null=True)
    VoiceControl = models.BooleanField(default=False)
    AcousticType = models.CharField(max_length=100 , blank=True , null=True)
    SpecialFeatures = models.CharField(max_length=300 , blank=True , null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    BatteryEfficiency = models.CharField(max_length=100 , blank=True , null=True)
    ProductID = models.CharField(max_length=500, blank=True, null=True)
    compatibility = models.CharField(max_length=50 , blank=True , null=True)
    MultipleConnection = models.BooleanField(default=False) 
    jack = models.BooleanField(default=False)
    Impedance = models.CharField(max_length=50 , blank=True , null=True)
    MagnetType = models.CharField(max_length=50 , blank=True , null=True)
    IncludedItems = models.CharField(max_length=100, blank=True, null=True)
    USBPort = models.CharField(max_length=50, blank=True, null=True)
    sensitivity = models.CharField(max_length=50 , blank=True, null=True)
    
    
    def __str__(self):
       return f'{self.id} - {self.name}'
   



class AirPodImage(models.Model):
    airpod = models.ForeignKey(AirPods, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='airpod_images/')

    def __str__(self):
        return f"Image of {self.airpod.name}"
    
    
class AccessoryType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
    
class Accessory(BaseProduct):
    #PowerBonk
    comparison = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null=True)
    ProductType = models.ForeignKey(AccessoryType, on_delete=models.CASCADE, related_name='accessories' , blank=True , null=True)
    capacity = models.CharField(max_length=100 , blank=True , null=True)
    compatibility = models.CharField(max_length=50 , blank=True , null=True)
    InputPort = models.CharField(max_length=100 , blank=True , null=True)
    NumberOfOutputPorts = models.CharField(max_length=50 , blank=True , null=True)
    TotalOutputPower = models.CharField(max_length=50 , blank=True , null=True)
    DimensionsWeights = models.CharField(max_length=100, blank=True, null=True)
    BodyMaterial = models.CharField(max_length=50 , blank=True , null=True)
    LEDIndicator = models.BooleanField(default=False)
    FastCharging = models.CharField(max_length=100, blank=True, null=True)
    WirelessCharging = models.BooleanField(default=False)
    TechnicalSpecifications = models.CharField(max_length=1000 , blank=True , null=True)
    IncludedItems = models.CharField(max_length=100, blank=True, null=True)
    ControlsKeys = models.CharField(max_length=100 , blank=True , null=True)
    resistance = models.CharField(max_length=100, blank=True, null=True)
    ConnectedCable = models.CharField(max_length=50 , blank=True , null=True)
    SimultaneousCharging = models.CharField(max_length=100 , blank=True , null=True)
    InputCurrentIntensity = models.CharField(max_length=50 , blank=True , null=True)
    InputVoltage = models.CharField(max_length=50 , blank=True , null=True)
    OutputCurrentIntensity = models.CharField(max_length=50 , blank=True , null=True)
    OutputVoltage = models.CharField(max_length=50 , blank=True , null=True)
    OtherFeatures = models.CharField(max_length=500, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    capacityInWH = models.CharField(max_length=50 , blank=True , null=True)    
    NominalCapacity = models.CharField(max_length=50 , blank=True , null=True)
    ProductID = models.CharField(max_length=500, blank=True, null=True)
    
    #HandsFree
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    NFC = models.BooleanField(default=False)
    CableLength = models.CharField(max_length=50 , blank=True , null=True)
    MultipleConnection = models.BooleanField(default=False) 
    microphone = models.BooleanField(default=False)
    InterfaceType = models.CharField(max_length=50 , blank=True , null=True)
    jack = models.BooleanField(default=False)
    ResponseFrequency = models.CharField(max_length=50 , blank=True , null=True)
    Impedance = models.CharField(max_length=50 , blank=True , null=True)
    DriverDiameter = models.CharField(max_length=50 , blank=True , null=True)
    VoiceControl = models.BooleanField(default=False)
    ANC = models.BooleanField(default=False)
    sensitivity = models.CharField(max_length=50 , blank=True, null=True)
    USBPort = models.CharField(max_length=50, blank=True, null=True)
    buttons = models.CharField(max_length=300 , blank=True , null=True)
    type = models.CharField(max_length=50 , blank=True , null=True)
    VoiceAssistant = models.CharField(max_length=50, blank=True, null=True)
    SuitableFor = models.CharField(max_length=50 , blank=True , null=True)
    SpecialFeatures = models.CharField(max_length=300 , blank=True , null=True)
    PowerSource = models.CharField(max_length=50 , blank=True , null=True)
    
    
    #speaker
    screen = models.BooleanField(default=False)
    RemoteControl = models.BooleanField(default=False)
    AUXGate = models.BooleanField(default=False)
    ConnectOtherSpeakers = models.BooleanField(default=False)
    BatteryEfficiency = models.CharField(max_length=100 , blank=True , null=True)
    ChargingTime = models.CharField(max_length=50 , blank=True , null=True)
    MemoryCardSupport = models.BooleanField(default=False)
    SideMicrophone = models.BooleanField(default=False)
    DanceOfLight = models.BooleanField(default=False)
    NumberOfSubWoofers = models.CharField(max_length=50 , blank=True , null=True)
    SubWooferDimensions = models.CharField(max_length=50 , blank=True , null=True)
    MicrophoneInput = models.BooleanField(default=False)
    HeadphoneOutput = models.BooleanField(default=False)
    PerformanceRange = models.CharField(max_length=50 , blank=True , null=True)
    ConversationMicrophone = models.BooleanField(default=False)
    BatteryCapacity = models.CharField(max_length=100, blank=True, null=True)
    radio = models.BooleanField(default=False)
    AudioTechnologies = models.CharField(max_length=200 , blank=True , null=True)
    ports = models.CharField(max_length=100 , blank=True , null=True)
    InputPower = models.CharField(max_length=50 , blank=True , null=True)
    OutputPower = models.CharField(max_length=50 , blank=True , null=True)
    ControlsKeys = models.CharField(max_length=100 , blank=True , null=True)
    
    #keyboard
    ConnectionType = models.CharField(max_length=50 , blank=True , null=True)
    NumberOfKeys = models.CharField(max_length=50 , blank=True , null=True)
    CompatibleOs = models.CharField(max_length=50 , blank=True , null=True)
    NumberOfKeystrokes = models.CharField(max_length=50 , blank=True , null=True)
    lighting = models.CharField(max_length=100 , blank=True , null=True)
    TypeOfKeyboard = models.CharField(max_length=50 , blank=True , null=True)
    WristSupport = models.BooleanField(default=False)
    TypeOfSwitch = models.CharField(max_length=50 , blank=True , null=True)
    ColorOfSwitch = models.CharField(max_length=50 , blank=True , null=True)
    AntiGhosting = models.BooleanField(default=False)
    NumberOfBatteries = models.CharField(max_length=50 , blank=True , null=True) 
    KeyboardBoard = models.CharField(max_length=50 , blank=True , null=True)

    #flash
    TransferSpeed = models.CharField(max_length=100 , blank=True , null=True)
    InterfaceTechnology = models.CharField(max_length=100 , blank=True , null=True)
    StandardSpeed = models.CharField(max_length=100 , blank=True , null=True)
    
    #AUX
    CableLength = models.CharField(max_length=50 , blank=True , null=True)
    CableMaterial = models.CharField(max_length=50 , blank=True , null=True)
    TypeOfCable = models.CharField(max_length=50 , blank=True , null=True)
    CommunicationPorts = models.CharField(max_length=50 , blank=True , null=True)
    NumberOfOutputGate = models.CharField(max_length=50 , blank=True , null=True)
    
    
    #MemoryCard
    ReadingSpeed = models.CharField(max_length=100 , blank=True , null=True)
    temperature = models.CharField(max_length=100 , blank=True , null=True)
    WritingSpeed = models.CharField(max_length=100 , blank=True , null=True)
    
    
    #Charger
    IncludeCable = models.BooleanField(default=False)
    ChargingPower = models.CharField(max_length=100 , blank=True , null=True)
    NumberOfOutputPorts = models.CharField(max_length=100 , blank=True , null=True)
    ChargingFeatures = models.CharField(max_length=100 , blank=True , null=True)
    PartNumber = models.CharField(max_length=100 , blank=True , null=True)
    
    
    #ChargingCable
    

    #PhoneCase
    material = models.CharField(max_length=50 ,blank=True , null=True)
    structure = models.CharField(max_length=100 , blank=True , null=True)
    CoverLevel = models.CharField(max_length=150 , blank=True , null=True)
    
    

    #WatchBand
    LockType = models.CharField(max_length=50 , blank=True , null=True)
    size = models.CharField(max_length=50 , blank=True , null=True)
    
    
    #WatchCover
    


    def __str__(self):
        return f'{self.id} - {self.name}'
    
    
    
class AccessoryImage(models.Model):
    accessory = models.ForeignKey(Accessory, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accessory_images/')

    def __str__(self):
        return f"Image of {self.accessory.name}"
    
    
    
    