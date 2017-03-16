
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import json,os
from .forms import AlgorithmForm
from .models import Algorithms
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    #print (request.GET.get('nejecuciones',None))
    #print (request.GET.get())
  else:
    #print (form.fileName)
    print ('es un post de pruebatemplate...')
    print (request.POST)
    print (request.FILES)
    print (request.FILES.getlist('file'))
    #metodo para recorrer los archivos subidos y guardarlos en la carpeta media
    #este metodo y sus bucles son directamente de la documentacion
    for count, x in enumerate(request.FILES.getlist('file')):
      def process(f):
        with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
          for chunk in f.chunks():
            destination.write(chunk)
      process(x)
    return HttpResponse('archivos subidos...')
  return render(request,'app/pruebatemplate.html')

