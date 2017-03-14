
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import json
from .forms import AlgorithmForm
from .models import Algorithms
#from .forms import ContactForm
#en el index carga el json.. mirar para hacerlo desde funcion y tal...(seria facil solo seria importar output y listo)
def index(request):
  form = AlgorithmForm()
  return render(request,'app/index.html',{'form': form})
def pruebita(request):
  return HttpResponse("esto es pruebitaaaa")

def pruebatemplate(request):
  if request.method == 'GET':
    print 'es un get de pruebatemplate...'
    print (request.GET.get('nejecuciones',None))
    #print (request.GET.get())
  else:
    if request.is_ajax:
      print ('es un post de pruebatemplate...')
      print (request.POST)
      print (request.POST.getlist('parametros'))
      #alg = request.POST.getlist('csrfmiddlewaretoken')
    '''alg = request.POST.getlist('algoritmo[]')
    #bucle para mostrar los algoritmos que se introdujeron...
    for i in alg:
      print ('algoritmo:')
      print i 
    print ('es un post...')'''
    #print (request.POST.get('nejecuciones'))
  return render(request,'app/pruebatemplate.html')

