
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.servers.basehttp import FileWrapper
from django.core.files import File
from collections import OrderedDict
import os,ast,tarfile,sys
import createModels as cModels
import uploadFiles as uFiles
import parsefiles as parse
import pandas as pd
import subprocess
from .forms import AlgorithmForm
from .models import  Algorithms,Configuration,ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel,StatisticDataframeTex,StatisticDataframeTxt
#libreria de graficos charts
from charts import MinChart,AvgChart,MaxChart,MinAvgMaxChart
from setDataframes import sortAvgDataframe,sortMaxDataframe,sortMinDataframe
#from .models import Algorithms,Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mediafolder = os.path.join(BASE_DIR, 'media/results/')

def index(request):
  form = AlgorithmForm()
  print mediafolder
  return render(request,'app/index.html',{'form': form})
def about(request):
  return render(request,'app/about.html')
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
      
      for count, x in enumerate(request.FILES.getlist('file')):
        fileNames.append(x)
        uFiles.process(BASE_DIR,x)
      #llama al metodo de crear el modelo de configuracion
      idConfiguration = cModels.modelConfiguration(form,request)
      #config.metric = request.POST['metric']
      #algorithmModel.nAlgorithms = form.cleaned_data['nAlgorithms']
      for i,item in enumerate(dictAlgorithms):
        #llama al metodo para crear 
        cModels.modelAlgorithm(item,fileNames[i],idConfiguration)

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
      statisticDfTex = StatisticDataframeTex.objects.filter().latest('id')
      statisticDfTxt = StatisticDataframeTxt.objects.filter().latest('id')
      dataStatisticDftex = statisticDfTex.listValues
      dataStatisticDftxt = statisticDfTxt.listValues
      statisticalDfTex = pd.DataFrame.from_dict(dataStatisticDftex[0])
      statisticalDfTxt = pd.DataFrame.from_dict(dataStatisticDftxt[0])
      statiscalDfTexTable = statisticalDfTex.to_html()
      statiscalDfTxtTable = statisticalDfTxt.to_html()
      df = []
      #print data
      
      list1 = [int(x) for x in data[0]['Average'].keys()]
      list1.sort()
      for i,value in enumerate(list1):
        list1[i] = str(value)
      

      for i,v in enumerate(data):
        #condicion de mirar en la lista de bounds escogidos...(si esta avg se hace)

        dataFrame = pd.DataFrame()
        
        if 'Average' in str(getConfiguration.bound):
          dfAverage = sortAvgDataframe(data[i]['Average'].items())
          dataFrame['0'] = dfAverage['Step']
          dataFrame['Average'] = dfAverage['Average']
          dataFrame.set_index('0')
          dataFrame = dataFrame.drop('0',1)
        if 'Max' in str(getConfiguration.bound):
          dfMax = sortMaxDataframe(data[i]['Max'].items())
          dataFrame['0'] = dfMax['Step']
          dataFrame['Max'] = dfMax['Max']
          dataFrame.set_index('0')
          dataFrame = dataFrame.drop('0',1)
        if 'Min' in str(getConfiguration.bound):
          dfMin = sortMinDataframe(data[i]['Min'].items())
          dataFrame['0'] = dfMin['Step']
          dataFrame['Min'] = dfMin['Min']
          dataFrame.set_index('0')
          dataFrame = dataFrame.drop('0',1)
        df.append(dataFrame)
      html_table =[]
      txt_df = []

      for i,v in enumerate(df):
        html_df = df[i].to_html()
        columns = df[i].columns.values
        stringFormat = str(algorithm_names[i])+'Results'+'\n'
        for index,row in df[i].iterrows():
          stringFormat = str(index)+' '
          for j,v in enumerate(columns):
            stringFormat = stringFormat + str(row[str(v)])+' '
          stringFormat = stringFormat + '\n'
          with open(os.path.join(mediafolder,str(algorithm_names[i])+'.txt'), 'a') as myfile:
            myfile.write(str(stringFormat))




        filename = os.path.join(mediafolder,str(algorithm_names[i])+'results'+'.tex')
        template = r'''\documentclass[preview]{{standalone}}
                    \usepackage{{booktabs}}
                    \begin{{document}}
                    \begin{{tabular}}{{|c|c|c|c|c|}}
                    {}
                    \end{{tabular}}
                    \end{{document}}
                    '''
        with open(filename, 'wb') as f:
          f.write(template.format(df[i].to_latex()))
        subprocess.call(['pdflatex','-output-directory='+str(mediafolder),filename])
        html_table.append(html_df)
      tFile = tarfile.open(str(mediafolder)+"/files.tar", 'w')
      tFile.add(str(mediafolder),arcname='results')
      #eliminar todos menos el tar...
      #os.delete(join(str(mediafolder),r'^results\s*\w*.\w*'))
      algorithmTable = zip(algorithm_names,html_table)
      statisticTableTex = statiscalDfTexTable
      statisticTableTxt = statiscalDfTxtTable
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
      #salida de datos plot
      return render(request, 'app/results.html',dicOutput)
    elif str(getConfiguration.dataOutput) == 'table':
      #salida de datos table
      print statiscalDfTexTable
      return render(request,'app/results.html',{'algorithmTable':algorithmTable,'statiscalDfTexTable':statiscalDfTexTable,'statiscalDfTxtTable':statiscalDfTxtTable}) 
    else:
      #salida de datos plot y table
      dicOutput['algorithmTable'] = algorithmTable
      dicOutput['statiscalDfTexTable'] = statiscalDfTexTable
      return render(request, 'app/results.html',dicOutput)

  return render(request,'app/results.html') 


def download(request):

    
    filename = os.path.join(mediafolder,'files.tar')# Select your file here.                                
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, 'application/x-tar')
    response['Content-Length'] = os.path.getsize(filename)
    return response