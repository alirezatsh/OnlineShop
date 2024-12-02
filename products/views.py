from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import (Phone, PhoneImage, Review , Tablet , TabletImage ,
                     SmartWatch , SmartWatchImage , AirPods , AirPodImage
                     , Brand , Accessory  , AccessoryType , Color)

from .serializers import (PhoneSerializer, PhoneImageSerializer, ReviewSerializer,
                          SimilarPhoneSerializer , TabletImageSerializer ,
                          TabletSerializer , SimilarTabletSerializer , SmartWatchImageSerializer 
                          , SmartWatchSerializer , SimilarSmartWatchSerializer , 
                          AirPodSerializer , AirPodImageSerializer , SimilarAirPodSerializer 
                          , BrandSerializer , AccessorySerializer , ColorSerializer)
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class FilterByBrandMixin:
    @action(detail=False, methods=['get'], url_path='brand/(?P<brand_id>\d+)')
    def by_brand(self, request, brand_id=None):
        try:
            queryset = self.get_queryset().filter(brand_id=brand_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"error": "Brand not found"}, status=404)


class PhoneViewSet(FilterByBrandMixin , viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            phone = self.get_object()
            similar_phones = Phone.objects.filter(
                Q(name__icontains=phone.name.split()[0])
            ).exclude(id=phone.id)[:5]

            serializer = SimilarPhoneSerializer(similar_phones, many=True)
            return Response(serializer.data)
        except Phone.DoesNotExist:
            return Response({"error": "Phone not found"}, status=404)



class PhoneImageViewSet(viewsets.ModelViewSet):
    queryset = PhoneImage.objects.all()
    serializer_class = PhoneImageSerializer
    
    
class TabletViewSet(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            # گرفتن محصول فعلی بر اساس pk
            tablet = self.get_object()

            # فیلتر کردن محصولات مشابه بر اساس سه شرط
            similar_tablets = Tablet.objects.filter(
                Q(RAM=tablet.RAM) &  # رم باید یکسان باشد
                Q(InnerMemory=tablet.InnerMemory) &  # حافظه باید یکسان باشد
                Q(brand=tablet.brand)  # برند باید یکسان باشد
            ).exclude(id=tablet.id)  # محصول فعلی را حذف کن

            if not similar_tablets.exists():
                return Response({"error": "No similar tablets found."}, status=404)

            serializer = TabletSerializer(similar_tablets, many=True)
            return Response(serializer.data)

        except Tablet.DoesNotExist:
            return Response({"error": "Tablet not found"}, status=404)

class TabletImageViewSet(viewsets.ModelViewSet):
    queryset = TabletImage.objects.all()
    serializer_class = TabletImageSerializer
    
    
class SmartwatchViewSet(FilterByBrandMixin , viewsets.ModelViewSet):
    queryset = SmartWatch.objects.all()
    serializer_class = SmartWatchSerializer

    @action(detail=False, methods=['get'], url_path='fake')
    def fake_smartwatches(self, request):
        queryset = self.get_queryset().filter(IsFake=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='original')
    def original_smartwatches(self, request):
        queryset = self.get_queryset().filter(IsFake=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            smartwatch = self.get_object()
            similar_products = SmartWatch.objects.filter(
                Q(name__icontains=smartwatch.name.split()[0])
            ).exclude(id=smartwatch.id)[:5]
            serializer = SimilarSmartWatchSerializer(similar_products, many=True)
            return Response(serializer.data)
        except SmartWatch.DoesNotExist:
            return Response({"error": "Smartwatch not found"}, status=404)
        


class AirPodViewSet(FilterByBrandMixin ,  viewsets.ModelViewSet):
    queryset = AirPods.objects.all()
    serializer_class = AirPodSerializer
    
    @action(detail=False, methods=['get'], url_path='fake')
    def fake_airpods(self, request):
        queryset = self.get_queryset().filter(IsFake=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='original')
    def original_airpods(self, request):
        queryset = self.get_queryset().filter(IsFake=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            airpod = self.get_object()
            similar_products = AirPods.objects.filter(
                Q(name__icontains=airpod.name.split()[0])
            ).exclude(id=airpod.id)[:5]
            serializer = SimilarAirPodSerializer(similar_products, many=True)
            return Response(serializer.data)
        except AirPods.DoesNotExist:
            return Response({"error": "AirPod not found"}, status=404)
        


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer



class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

    @action(detail=False, methods=['get'], url_path='by-type/(?P<type_id>[^/.]+)')
    def filter_by_type(self, request, type_id=None):
        filtered_accessories = self.queryset.filter(ProductType_id=type_id)
        serializer = self.get_serializer(filtered_accessories, many=True)
        return Response(serializer.data)