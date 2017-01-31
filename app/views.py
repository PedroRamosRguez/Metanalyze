from django.shortcuts import render
import json
import os
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
#en el index carga el json.. mirar para hacerlo desde funcion y tal...(seria facil solo seria importar output y listo)
def index(request):
  return render(request,'app/index.html')
def pruebita(request):
  return HttpResponse("esto es pruebitaaaa")

def pruebatemplate(request):
  return render(request,'app/pruebatemplate.html')
  




