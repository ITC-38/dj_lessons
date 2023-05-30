from django.urls import path

from lesson4.views import making_queries

urlpatterns = [
    path('', making_queries)
]
