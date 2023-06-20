from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    sponsor = 'Станьте нашим спонсором'
    return render(
        request,
        'lesson5/index.html',
        context={
            'sponsor': sponsor,
            'text': ['something', 'else', 1, 324, 23, 32],
            'title': 'Главная страница'
        }
    )
