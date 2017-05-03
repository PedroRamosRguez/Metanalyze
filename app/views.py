
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.files import File
import json,os,ast
import createModels as cModels
import uploadFiles as uFiles
from .forms import AlgorithmForm
#from .models import Algorithms,Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
  
  if request.method == 'POST':
    print 'es un post de index..'
    form = AlgorithmForm(request.POST)
    #convierte a array de diccionarios los valores que se obtienen.
    dictAlgorithms= ast.literal_eval(request.POST.get('algorithms'))
    #array para guardar el nombre de los ficheros que se suban para insertarlos al modelo.
    fileNames = []
    if form.is_valid():
      print('formulario valido se procede a insertar al modelo')
      #print(form.is_valid())
      #print(form.cleaned_data)
      #sube los ficheros a la carpeta media
      #hacer un try para que en caso de que no llegue file no haga nada...
      for count, x in enumerate(request.FILES.getlist('file')):
        fileNames.append(x)
        uFiles.process(BASE_DIR,x)
      #llama al metodo de crear el modelo de configuracion
      cModels.modelConfiguration(form,request)
      #config.metric = request.POST['metric']
      #algorithmModel.nAlgorithms = form.cleaned_data['nAlgorithms']
      for i,item in enumerate(dictAlgorithms):
        #print i
        #print item
        #llama al metodo para crear 
        cModels.modelAlgorithm(item,fileNames[i])
        #PONER LA CREACION DEL MODELO DE LOS ALGORITMOS EN UN METODO
      #return HttpResponse('archivos subidos...')
      return HttpResponseRedirect('/pruebatemplate/')
    else:
      print('estoy en el else...')
      #mostrar un render de error 500
      #mostrar algun error o algo..'''
    
  else:
    #print 'es un get de index'
    form = AlgorithmForm()
  return render(request,'app/index.html',{'form': form})

def pruebatemplate(request):
  if request.method == 'GET':
    print 'es un get de pruebatemplate...'
    #hacer lo de obtener los graficos y las tablas...
    #print (request.GET.get('nejecuciones',None))
    #print (request.GET.get())
  else:
    print 'seria un post de pruebatemplate'
    
  return render(request,'app/pruebatemplate.html')

