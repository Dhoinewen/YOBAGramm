from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from mysite import settings
from rest_framework import routers

from gramm.views import YobaAPIList, YobaAPIUpdateDestroy


# router = routers.SimpleRouter()
# router.register(r'yoba', YobaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('main/', YobaAPIList.as_view()),
    path('main/<int:pk>', YobaAPIUpdateDestroy.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
