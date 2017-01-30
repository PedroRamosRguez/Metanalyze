from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request,'app/index.html')

def pruebita(request):
  return HttpResponse("esto es pruebitaaaa")

def pruebatemplate(request):
  return render(request,'app/pruebatemplate.html')  