from django.contrib import admin
from django.urls import path , include
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularSwaggerView , SpectacularAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def no_access(request):
    return HttpResponse("you don't have access to this page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/' , include('products.urls')),
    path('accounts/' , include('accounts.urls')),
    path('forms/' , include('forms.urls')),
    path('no-access/', no_access),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)