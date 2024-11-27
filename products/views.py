from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import (Phone, PhoneImage, Review , Tablet , TabletImage ,
                     SmartWatch , SmartWatchImage , AirPods , AirPodImage
                     , Brand , Accessory  , AccessoryType)

from .serializers import (PhoneSerializer, PhoneImageSerializer, ReviewSerializer,
                          SimilarPhoneSerializer , TabletImageSerializer ,
                          TabletSerializer , SimilarTabletSerializer , SmartWatchImageSerializer 
                          , SmartWatchSerializer , SimilarSmartWatchSerializer , 
                          AirPodSerializer , AirPodImageSerializer , SimilarAirPodSerializer , BrandSerializer , AccessorySerializer)
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
    
    
class TabletViewSet(FilterByBrandMixin , viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            tablet = self.get_object()
            similar_tablets = Tablet.objects.filter(
                Q(name__icontains=tablet.name.split()[0])
            ).exclude(id=tablet.id)[:5]

            serializer = SimilarTabletSerializer(similar_tablets, many=True)
            return Response(serializer.data)
        except tablet.DoesNotExist:
            return Response({"error": "tablet not found"}, status=404)



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




class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

    @action(detail=False, methods=['get'], url_path='by-type/(?P<type_id>[^/.]+)')
    def by_type(self, request, type_id=None):
        try:
            accessories = Accessory.objects.filter(ProductType_id=type_id)
            if not accessories.exists():
                return Response({'error': 'No accessories found for this type'}, status=404)
            serializer = self.get_serializer(accessories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def create(self, request, *args, **kwargs):
        try:
            accessory_type = request.data.get('ProductType')

            if not accessory_type:
                return Response({'error': 'ProductType is required'}, status=status.HTTP_400_BAD_REQUEST)

            allowed_fields_map = {
                'پاوربانک': {'name', 'color', 'capacity'},
                'قاب گوشی': {'name'},
                'شارژر': {'name', 'compatibility'},
            }

            allowed_fields = allowed_fields_map.get(accessory_type, {'name'})

            request_data = request.data.copy()

            # حذف ProductType از داده‌ها قبل از بررسی
            request_data.pop('ProductType', None)

            # بررسی فیلدهای غیرمجاز
            invalid_fields = set(request_data.keys()) - allowed_fields
            if invalid_fields:
                return Response({
                    'error': f"Invalid fields for {accessory_type}: {', '.join(invalid_fields)}"
                }, status=status.HTTP_400_BAD_REQUEST)

            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
