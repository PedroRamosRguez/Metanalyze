
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.files import File
from collections import OrderedDict
import os,ast
import createModels as cModels
import uploadFiles as uFiles
import parsefiles as parse
import pandas as pd
from .forms import AlgorithmForm
from .models import  Algorithms,Configuration,ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
#libreria de graficos charts
from charts import MinChart,AvgChart,MaxChart,MinAvgMaxChart
from setDataframes import sortAvgDataframe,sortMaxDataframe,sortMinDataframe
#from .models import Algorithms,Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
  form = AlgorithmForm()
  return render(request,'app/index.html',{'form': form})

def results(request):
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
    dataModel = MinAvgMaxChartModel.objects.filter().latest('id')
    getConfiguration = Configuration.objects.filter().latest('id')
    algorithm_names = []
    getAlgorithms = Algorithms.objects.filter(configuration__id=getConfiguration.id).values().distinct()
    
    for i in range(int(getConfiguration.nAlgorithms)):
      algorithm_names.append(getAlgorithms[i]['algorithm'])
    if 'table' in str(getConfiguration.dataOutput):
      data = dataModel.listValues
      df = []
      for i,v in enumerate(data):
        #condicion de mirar en la lista de bounds escogidos...(si esta avg se hace)
        dataFrame = pd.DataFrame()
        if 'Average' in str(getConfiguration.bound):
          dfAverage = sortAvgDataframe(data[i]['Average'].items())
          dataFrame['Average'] = dfAverage
        if 'Max' in str(getConfiguration.bound):
          dfMax = sortMaxDataframe(data[i]['Max'].items())
          dataFrame['Max'] = dfMax 
        if 'Min' in str(getConfiguration.bound):
          dfMin = sortMinDataframe(data[i]['Min'].items())
          dataFrame['Min'] = dfMin
        df.append(dataFrame)
      html_table =[]
      for i,v in enumerate(df):
        html_df = df[i].to_html(index=False)
        html_table.append(html_df)
      algorithmTable = zip(algorithm_names,html_table,)
    dicOutput = {}
    if len(getConfiguration.bound) == 3:
      dicOutput['minavgmax_chart'] = MinAvgMaxChart
    if 'Min' in str(getConfiguration.bound):
      dicOutput['min_chart'] = MinChart
    if 'Average' in str(getConfiguration.bound):
      dicOutput['avg_chart'] = AvgChart
    if 'Max' in str(getConfiguration.bound):
      dicOutput['max_chart'] = MaxChart
    if str(getConfiguration.dataOutput) =='plot':
      print 'la salida es plot'
      return render(request, 'app/results.html',dicOutput)
    elif str(getConfiguration.dataOutput) == 'table':
      print 'la salida es tabla..'
      return render(request,'app/results.html',{'algorithmTable':algorithmTable}) 
    else:
      print 'la salida es plot y tabla'
      dicOutput['algorithmTable'] = algorithmTable
      return render(request, 'app/results.html',dicOutput)
  return render(request,'app/results.html') 