from rest_framework import viewsets, permissions, mixins
from .models import AboutUs, Installment
from .serializers import AboutUsSerializer, InstallmentSerializer

# class IsAdminUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff

class AboutUsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    # def get_permissions(self):
    #     if self.action in ['list', 'destroy']:
    #         return [permissions.IsAuthenticated(), IsAdminUser()]
    #     return [permissions.AllowAny()]

class InstallmentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer

    # def get_permissions(self):
    #     if self.action in ['list', 'destroy']:
    #         return [permissions.IsAuthenticated(), IsAdminUser()]
    #     return [permissions.AllowAny()]
