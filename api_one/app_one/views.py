from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('this is api_one and app_one | 1-1' , status=200)