from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ls1/', include('lesson1.urls')),
    path('ls2/', include('lesson2.urls')),
]
