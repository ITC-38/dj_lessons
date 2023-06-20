# from django.urls import path

from lesson4.convertors import register_all_ls4_converters
# from lesson4.views import making_queries


register_all_ls4_converters()
urlpatterns = [
    # path('<date:id>', making_queries)
]
