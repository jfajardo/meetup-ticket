from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from qr_code import urls as qr_code_urls

urlpatterns = [
    path('', include('app.urls')),
    path('admin01/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('qr_code/', include(qr_code_urls, namespace="qr_code")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
