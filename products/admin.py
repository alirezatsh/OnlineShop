from django.contrib import admin
from .models import Phone, PhoneImage , Review , Tablet , TabletImage , SmartWatch , SmartWatchImage

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

admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneImage)
admin.site.register(Tablet , TabletAdmin)
admin.site.register(TabletImage)
admin.site.register(SmartWatch, SmartWatchAdmin)
admin.site.register(SmartWatchImage)
admin.site.register(Review)

