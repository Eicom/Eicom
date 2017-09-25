from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('start.urls', namespace='start')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
