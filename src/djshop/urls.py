"""
URL configuration for djshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

admin_urls = [
    path('api/admin/users/',
         include(('djshop.auths.users.urls.admin', 'djshop.auths.users'), namespace='users-admin')),

    path('api/admin/catalog/', include(('djshop.apps.catalog.urls.admin', 'djshop.apps.catalog'), namespace='catalog-admin'))
]

front_urls =[
    path('api/front/users/',
         include(('djshop.auths.users.urls.front', 'djshop.auths.users'), namespace='users-front')),
    path('api/front/catalog/', include(('djshop.apps.catalog.urls.front', 'djshop.apps.catalog'), namespace='catalog-front'))
]


doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path("admin/", admin.site.urls),
] + front_urls + admin_urls + doc_patterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title= "DjShop"
admin.site.index_title= "DjShop"
admin.site.site_header= "DjShop"






