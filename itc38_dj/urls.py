from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('personal/', admin.site.urls),
    # path('ls1/', include('lesson1.urls')),
    # path('ls2/', include('lesson2.urls')),
    # path('ls4/', include('lesson4.urls')),
    path('ls5/', include('lesson5.urls')),
]


if settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
