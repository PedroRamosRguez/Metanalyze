
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
    form = AlgorithmForm(request.POST)
    #convierte a array de diccionarios los valores que se obtienen.
    dictAlgorithms= ast.literal_eval(request.POST.get('algorithms'))
    print (request.FILES)
    #array para guardar el nombre de los ficheros que se suban para insertarlos al modelo.
    fileNames = []
    #sube los ficheros a la carpeta media
    #hacer un try para que en caso de que no llegue file no haga nada...
    for count, x in enumerate(request.FILES.getlist('file')):
      def process(f):
        with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
          for chunk in f.chunks():
            destination.write(chunk)
      filesNames.append = x
      process(x)
    if form.is_valid:
      print('formulario valido se procede a insertar al modelo')
      algorithmModel = Algorithms
      config = Configuration
      print(form.is_valid())
      print(form.cleaned_data)
      #para introducir el test o los tests que se realicen, se debe hacer un json.dumps()
      #TODO
      '''
        hacer un bucle que dependiendo del numero de algoritmos que se inserte (form.cleaned_data[nAlgorithms])
        crear un objeto del modelo e insertar los datos al modelo. Tener en cuenta que los algoritmos tambien hay
        que recorrerlos (TENERLO EN CUENTA)
        para el fichero usar la posicion alctual en el vector de nombre de fichero que se creo anteriormente
        al subir los ficheros a la carpeta media
        al final de cada iteracion poner algorithmModel.save() y eso es como insertar un elemento en una
        base de datos
      '''
      '''
        Para crear el modelo de configuracion estandar es solo insertar a ese modelo los valores del 
        form.cleaned_data[xxxx]
        Al final poner configModel.save()  para guardar la confifuracion estandar para los algoritmos.
      '''
      '''
        Todo el tema de los modelos se hace para que cuando se vayan a tratar los datos, sea mas facil
        acceder a los datos y no tener que realizar conversiones de diccionario a lista, etc.
      '''
      

    else:
      print('estoy en el else...')
      #mostrar algun error o algo..
    
    return HttpResponse('archivos subidos...')
  return render(request,'app/pruebatemplate.html')

