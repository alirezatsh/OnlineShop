from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Phone, PhoneImage, Review , Tablet , TabletImage
from .serializers import (PhoneSerializer, PhoneImageSerializer, ReviewSerializer,
                          SimilarPhoneSerializer , TabletImageSerializer ,
                          TabletSerializer , SimilarTabletSerializer)
from django.db.models import Q

class PhoneViewSet(viewsets.ModelViewSet):
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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer







