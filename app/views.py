
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json,os,ast
from .forms import AlgorithmForm
from .models import Algorithms,Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    print ('es un post de pruebatemplate...')
    print request.POST
    form = AlgorithmForm(request.POST)
    #convierte a array de diccionarios los valores que se obtienen.
    dictAlgorithms= ast.literal_eval(request.POST.get('algorithms'))
    if form.is_valid:
      print('formulario valido procedo a introducir datos en modelo')
    else:
      print('estoy en el else...')
      #mostrar algun error o algo..
    print (request.FILES)
    #hacer un try para que en caso de que no llegue file no haga nada...
    for count, x in enumerate(request.FILES.getlist('file')):
      def process(f):
        with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
          for chunk in f.chunks():
            destination.write(chunk)
      process(x)

    #para introducir el test o los tests que se realicen, se debe hacer un json.dumps()
    #configuration.nObjetives = request.POST.getlist('')
    return HttpResponse('archivos subidos...')
  return render(request,'app/pruebatemplate.html')

