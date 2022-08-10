from django.http import HttpResponse


def index(request):
    return HttpResponse("ORM page here.")
