
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.files import File
import os,ast
import createModels as cModels
import uploadFiles as uFiles
import parsefiles as parse
from .forms import AlgorithmForm
#libreria de graficos bokeh
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.models import Range1d
from bokeh.embed import components
#libreria de graficos charts
from charts import BubbleChart
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
      #mostrar algun error o algo..'''
    
  else:
    print 'es un get de pruebatemplate...'
    
    
  return render(request,'app/pruebatemplate.html')




























#PLOT USANDO BOKEH
def simple_chart(request):
  # create some data
  x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
  x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
  y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
  x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
  y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]

  # select the tools we want
  #TOOLS="pan,wheel_zoom,box_zoom,reset,save"
  TOOLS="save"
  # the red and blue graphs will share this data range
  xr1 = Range1d(start=0, end=30)
  yr1 = Range1d(start=0, end=30)

  # only the green will use this data range
  xr2 = Range1d(start=0, end=30)
  yr2 = Range1d(start=0, end=30)

  # build our figures
  p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
  p1.scatter(x1, y1, size=12, color="red", alpha=0.5)

  p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
  p2.scatter(x2, y2, size=12, color="blue", alpha=0.5)
  p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=300, plot_height=300)
  p3.scatter(x3, y3, size=12, color="green", alpha=0.5)

  # plots can be a single PlotObject, a list/tuple, or even a dictionary
  plots = {'Red': p1, 'Blue': p2, 'Green': p3}
  print 'esto es p1'
  print p1
  script, div = components(plots)
  return render(request, "app/simple_chart.html", {"the_script": script, "the_div": div})

#ejemplo de un grafico de la documentacion de jchart
def jchart(request):
  return render(request, 'app/jchart.html', {
      'bubble_chart': BubbleChart,
  })
   