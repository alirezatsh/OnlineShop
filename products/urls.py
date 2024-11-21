from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet, PhoneImageViewSet , ReviewViewSet , TabletImageViewSet , TabletViewSet , SmartwatchViewSet

router = DefaultRouter()
router.register(r'phones', PhoneViewSet)
router.register(r'phone-images', PhoneImageViewSet)
router.register(r'tablets', TabletViewSet)
router.register(r'tablet-images', TabletImageViewSet)
router.register(r'reviews', ReviewViewSet , basename='review')
router.register(r'smartwatch', SmartwatchViewSet, basename='smartwatch')



urlpatterns = [
    path('', include(router.urls)),
    path('reviews/', include('ckeditor_uploader.urls')),  

]



