from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'is_homepage': True}
    return render(request,
                  'tracker/index/index.html', context)


