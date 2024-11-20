from django.contrib import admin
from .models import Phone, PhoneImage , Review , Tablet , TabletImage

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

admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneImage)
admin.site.register(Review)
admin.site.register(Tablet , TabletAdmin)
admin.site.register(TabletImage)
