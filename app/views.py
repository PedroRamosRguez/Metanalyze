
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from pprint import pprint
import json,os,ast
from .forms import AlgorithmForm
from .models import Algorithms,Configuration
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
    print request.POST.get('algoritmos')
    #print type(request.POST.get('algoritmos'))
    #print (request.POST['algoritmos'][0])
    #print (request.POST)
    print (request.FILES)
    #los prints van aqui...
    #hacer un try para que en caso de que no llegue file no haga nada...
    for count, x in enumerate(request.FILES.getlist('file')):
      def process(f):
        with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
          for chunk in f.chunks():
            destination.write(chunk)
      process(x)
    #print ('estoy antes de configuration')
    #print(configuration)
    #para introducir el test o los tests que se realicen, se debe hacer un json.dumps()
    #configuration.nObjetives = request.POST.getlist('')
    return HttpResponse('archivos subidos...')
  return render(request,'app/pruebatemplate.html')

