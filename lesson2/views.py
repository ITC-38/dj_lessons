from django.http import HttpRequest, HttpResponse


def models(request: HttpRequest):
    return HttpResponse('models')
