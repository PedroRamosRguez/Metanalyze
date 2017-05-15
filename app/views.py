
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.files import File
import os,ast
import createModels as cModels
import uploadFiles as uFiles
import parsefiles as parse
from .forms import AlgorithmForm
#libreria de graficos charts
from charts import MinChart,AvgChart,MaxChart,MinAvgMaxChart

#from .models import Algorithms,Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
  form = AlgorithmForm()
  return render(request,'app/index.html',{'form': form})

def pruebatemplate(request):
 
  #variable para obtener el id de configuracion de los algoritmos
  if request.method == 'POST':
    print 'es un post de pruebatemplate..'
    form = AlgorithmForm(request.POST)
    #convierte a array de diccionarios los valores que se obtienen.
    dictAlgorithms= ast.literal_eval(request.POST.get('algorithms'))
    #array para guardar el nombre de los ficheros que se suban para insertarlos al modelo.
    fileNames = []
    if form.is_valid():
      print('formulario valido se procede a insertar al modelo')
      #print(form.is_valid())
      #print(form.cleaned_data)
      #hacer un try para que en caso de que no llegue file no haga nada...
      for count, x in enumerate(request.FILES.getlist('file')):
        fileNames.append(x)
        uFiles.process(BASE_DIR,x)
      #llama al metodo de crear el modelo de configuracion
      global idConfiguration
      idConfiguration = cModels.modelConfiguration(form,request)
      print 'esto es idconfiguration'
      print idConfiguration
      #config.metric = request.POST['metric']
      #algorithmModel.nAlgorithms = form.cleaned_data['nAlgorithms']
      for i,item in enumerate(dictAlgorithms):
        print i
        print item
        #llama al metodo para crear 
        cModels.modelAlgorithm(item,fileNames[i],idConfiguration)
        #PONER LA CREACION DEL MODELO DE LOS ALGORITMOS EN UN METODO
      #return HttpResponse('archivos subidos...')

      parse.parse(idConfiguration)
      
      return HttpResponse('archivos subidos...')
    else:
      print('estoy en el else...')
      #mostrar un render de error 500
      #mostrar algun error o algo..
  else:
    print 'es un get de pruebatemplate...'
    '''return render(request, 'app/jchart.html', {
      #'bubble_chart': BubbleChart,'polar_chart':PolarChart,'scatter_chart':ScatterLineChart,'time_chart':TimeSeriesChart,
      'minavgmax_chart':MinAvgMaxChart,'min_chart':MinChart,'avg_chart':AvgChart,'max_chart':MaxChart
    })'''
  return render(request,'app/pruebatemplate.html') 