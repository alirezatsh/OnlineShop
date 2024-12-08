from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PhoneViewSet, PhoneImageViewSet  , 
                    TabletImageViewSet , TabletViewSet , SmartwatchViewSet
                    , AirPodViewSet , BrandViewSet , AccessoryViewSet , ColorViewSet ,
                    AccessoryTypeViewSet , ProductSearchViewSet)

router = DefaultRouter()
router.register(r'phones', PhoneViewSet)
router.register(r'phone-images', PhoneImageViewSet)
router.register(r'tablets', TabletViewSet)
router.register(r'tablet-images', TabletImageViewSet)
router.register(r'smartwatch', SmartwatchViewSet, basename='smartwatch')
router.register(r'airpods' , AirPodViewSet , basename='airpod')
router.register(r'brands' , BrandViewSet)
router.register(r'accessories' , AccessoryViewSet , basename='accessory')
router.register(r'colors' , ColorViewSet , basename='colors')
router.register(r'accessorytype' , AccessoryTypeViewSet , basename='accessorytype')
router.register(r'', ProductSearchViewSet, basename='product-search')





urlpatterns = [
    path('', include(router.urls)),
    path('reviews/', include('ckeditor_uploader.urls')),  

]



