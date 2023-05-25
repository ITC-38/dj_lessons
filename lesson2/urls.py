from django.urls import path

from lesson2.views import models

urlpatterns = [
    path('models/', models)
]
