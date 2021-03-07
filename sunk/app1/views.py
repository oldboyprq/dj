from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("a good man")
def num(request,num):
    return HttpResponse("The num is %s"%num)