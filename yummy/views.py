from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    load = loader.get_template("foodhtml1.html")
    return HttpResponse(load.render())
