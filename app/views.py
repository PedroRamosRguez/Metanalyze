
# Create your views here.
from django.http import HttpResponse,QueryDict
from django.shortcuts import render,render_to_response
import json
#from .forms import ContactForm
#en el index carga el json.. mirar para hacerlo desde funcion y tal...(seria facil solo seria importar output y listo)
def index(request):
  return render(request,'app/index.html')
def pruebita(request):
  return HttpResponse("esto es pruebitaaaa")

def pruebatemplate(request):
  if request.method == 'GET':
    print 'es un get...'
    print (request.GET.get('nejecuciones',None))
    #print (request.GET.get())
  elif request.method == 'POST':
    print (request.POST)
    alg = request.POST.getlist('algoritmo[]')
    #bucle para mostrar los algoritmos que se introdujeron...
    for i in alg:
      print ('algoritmo:')
      print i 
    print ('es un post...')
    #print (request.POST.get('nejecuciones'))
  return render(request,'app/pruebatemplate.html')