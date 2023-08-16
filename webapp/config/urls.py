from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="moyeo",
        default_version='v1',
        description="moyeo API 문서",
        contact=openapi.Contact(email="leahpar0401@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('products/', include('product.urls')),
    path('clubs/', include('club.urls')),
    path('sellers/', include('seller.urls')),
    path('notifications/', include('notification.urls')),
]

urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
