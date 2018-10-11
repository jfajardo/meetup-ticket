from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
