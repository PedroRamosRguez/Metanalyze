
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File
import json,os,ast
from .forms import AlgorithmForm
from .models import Algorithms,Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
  form = AlgorithmForm()
  return render(request,'app/index.html',{'form': form})

def pruebatemplate(request):
  if request.method == 'GET':
    print 'es un get de pruebatemplate...'
    #print (request.GET.get('nejecuciones',None))
    #print (request.GET.get())
  else:
    #print (form.fileName)
    print ('es un post de pruebatemplate...')
    #print request.POST
    #print (request.FILES)
    form = AlgorithmForm(request.POST)
    #convierte a array de diccionarios los valores que se obtienen.
    dictAlgorithms= ast.literal_eval(request.POST.get('algorithms'))
    #array para guardar el nombre de los ficheros que se suban para insertarlos al modelo.
    fileNames = []
    if form.is_valid:
      print('formulario valido se procede a insertar al modelo')
      #sube los ficheros a la carpeta media
      #hacer un try para que en caso de que no llegue file no haga nada...
      for count, x in enumerate(request.FILES.getlist('file')):
        def process(f):
          with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
            for chunk in f.chunks():
              destination.write(chunk)
        fileNames.append(x)
        process(x)
      #PONER LA CREACION DEL MODELO DE CONFIGURACION EN UN METODO
      config = Configuration.objects.create()
      config.nAlgorithms = form.cleaned_data['nAlgorithms']
      config.nObjectives = form.cleaned_data['nObjectives']
      config.nExecutions = form.cleaned_data['nExecutions']
      config.step = form.cleaned_data['step']
      config.stopCondition = form.cleaned_data['stopCondition']
      config.dataOutput = form.cleaned_data['dataOutput']
      config.bound = request.POST['bound']
      config.test = request.POST['test']
      config.metric = request.POST['metric']
      config.save()
      
      #config.metric = request.POST['metric']
      #algorithmModel.nAlgorithms = form.cleaned_data['nAlgorithms']
      for i,item in enumerate(dictAlgorithms):
        #PONER LA CREACION DEL MODELO DE LOS ALGORITMOS EN UN METODO
        algorithmModel = Algorithms.objects.create()
        algorithmModel.algorithm = item['algorithmName']
        algorithmModel.idAlgorithm = item['id']
        algorithmModel.fileName = fileNames[i]
        algorithmModel.nVariablesAlgorithm = item['nVariables']
        algorithmModel.save()
    else:
      print('estoy en el else...')
      #mostrar un render de error 500
      #mostrar algun error o algo..
    
    return HttpResponse('archivos subidos...')
  return render(request,'app/pruebatemplate.html')

