from django.contrib import admin
from .models import (Phone, PhoneImage  , Tablet , 
                     TabletImage , SmartWatch , SmartWatchImage
                     , AirPods , AirPodImage , Brand , Accessory , AccessoryType , Color)

class PhoneImageInline(admin.TabularInline):
    model = PhoneImage
    extra = 1

class PhoneAdmin(admin.ModelAdmin):
    inlines = [PhoneImageInline]
    
class TabletImageInline(admin.TabularInline):
    model = TabletImage
    extra = 1
    
class TabletAdmin(admin.ModelAdmin):
    inlines = [ TabletImageInline ]
    
class SmartWatchImageInline(admin.TabularInline):
    model = SmartWatchImage
    extra = 1
    
class SmartWatchAdmin(admin.ModelAdmin):
    inlines = [SmartWatchImageInline]
    
class AirPodImageInline(admin.TabularInline):
    model = AirPodImage
    extra = 1
    
class AirPodAdmin(admin.ModelAdmin):
    inlines = [AirPodImageInline]

admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneImage)
admin.site.register(Tablet , TabletAdmin)
admin.site.register(TabletImage)
admin.site.register(SmartWatch, SmartWatchAdmin)
admin.site.register(SmartWatchImage)
admin.site.register(AirPods , AirPodAdmin)
admin.site.register(AirPodImage)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(AccessoryType)
admin.site.register(Accessory)

