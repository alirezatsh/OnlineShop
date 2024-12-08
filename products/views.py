from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import (Phone, PhoneImage , Tablet , TabletImage ,
                     SmartWatch , SmartWatchImage , AirPods , AirPodImage
                     , Brand , Accessory  , AccessoryType , AccessoryImage , Color)

from .serializers import (PhoneSerializer, PhoneImageSerializer, 
                          SimilarPhoneSerializer , TabletImageSerializer ,
                          TabletSerializer , SimilarTabletSerializer , SmartWatchImageSerializer 
                          , SmartWatchSerializer , SimilarSmartWatchSerializer , 
                          AirPodSerializer , AirPodImageSerializer , SimilarAirPodSerializer 
                          , BrandSerializer , AccessorySerializer , ColorSerializer , AccessoryImageSerializer 
                          , SimilarAccessorySerializer , AccessoryTypeSerializers)
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductSearchViewSet(viewsets.ViewSet):
    def list(self, request):
        search_query = self.request.query_params.get('search', None)

        if not search_query:
            return Response({"message": "No search query provided."}, status=400)

        phones = Phone.objects.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )
        tablets = Tablet.objects.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )
        smartwatches = SmartWatch.objects.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )
        airpods = AirPods.objects.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )
        accessories = Accessory.objects.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )

        all_products = []
        for product in phones:
            all_products.append(PhoneSerializer(product).data)
        for product in tablets:
            all_products.append(TabletSerializer(product).data)
        for product in smartwatches:
            all_products.append(SmartWatchSerializer(product).data)
        for product in airpods:
            all_products.append(AirPodSerializer(product).data)
        for product in accessories:
            all_products.append(AccessorySerializer(product).data)

        if not all_products:
            return Response({"message": "No products found."}, status=404)

        return Response(all_products)



class FilterByBrandMixin:
    @action(detail=False, methods=['get'], url_path='brand/(?P<brand_id>\d+)')
    def by_brand(self, request, brand_id=None):
        try:
            queryset = self.get_queryset().filter(brand_id=brand_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"error": "Brand not found"}, status=404)
        
        
class ProductFilter(FilterByBrandMixin , viewsets.ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['price', 'discount', 'id'] 


class PhoneViewSet(ProductFilter):
    queryset = Phone.objects.select_related('brand', 'color')
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


class TabletViewSet(ProductFilter):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        try:
            tablet = self.get_object()

            similar_tablets = Tablet.objects.filter(
                RAM=tablet.RAM,
                InnerMemory=tablet.InnerMemory,
                brand=tablet.brand
            ).exclude(id=tablet.id)

            if not similar_tablets.exists():
                return Response({"error": "No similar tablets found."}, status=404)

            serializer = TabletSerializer(similar_tablets, many=True)
            return Response({
                'tablet': TabletSerializer(tablet).data,
                'similar_products': serializer.data
            })

        except Tablet.DoesNotExist:
            return Response({"error": "Tablet not found"}, status=404)

class TabletImageViewSet(viewsets.ModelViewSet):
    queryset = TabletImage.objects.all()
    serializer_class = TabletImageSerializer
    
    
class SmartwatchViewSet(ProductFilter):
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
        


class AirPodViewSet(ProductFilter):
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
        


    
    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer



class AccessoryViewSet(ProductFilter):
    queryset = Accessory.objects.select_related('ProductType')
    serializer_class = AccessorySerializer

    @action(detail=False, methods=['get'], url_path='by-type/(?P<type_id>[^/.]+)')
    def filter_by_type(self, request, type_id=None):
        filtered_accessories = self.queryset.filter(ProductType__id=type_id)
        serializer = self.get_serializer(filtered_accessories, many=True)
        return Response(serializer.data)
    
    
class AccessoryImageViewSet(viewsets.ModelViewSet):
    queryset = AccessoryImage.objects.all()
    serializer_class = AccessoryImageSerializer
    
    
class AccessoryTypeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = AccessoryType.objects.all()
    serializer_class = AccessoryTypeSerializers
