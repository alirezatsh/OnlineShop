from django.contrib import admin
from django.urls import path , include
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularSwaggerView , SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/' , SpectacularAPIView.as_view() , name='schema'),
    path('schema/swagger-ui/' , SpectacularSwaggerView.as_view(url_name='schema') , name='swagger-ui'),
    path(
        "schema/",
        get_schema_view(
            title="OnlineShop project", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
]

