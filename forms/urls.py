from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutUsViewSet, InstallmentViewSet

router = DefaultRouter()
router.register('about-us', AboutUsViewSet, basename='about_us')
router.register('installment', InstallmentViewSet, basename='installment')

urlpatterns = [
    path('', include(router.urls)),
]
