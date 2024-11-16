from django.contrib import admin
from .models import Phone, PhoneImage , Review

class PhoneImageInline(admin.TabularInline):
    model = PhoneImage
    extra = 1

class PhoneAdmin(admin.ModelAdmin):
    inlines = [PhoneImageInline]

admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneImage)
admin.site.register(Review)
