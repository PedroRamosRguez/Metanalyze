from django.shortcuts import render
import json
import os
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, 'config.json')
  with open(file_path) as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
  output=[]
  for item in range(len(data['test'])):
   #print 'Current item :', str(data['test'][item]['value']) 
   tipoTest= str(data['test'][item]['value'])
   output.append(tipoTest)
  #output =['1hola que tela','2 yokooooo']
  return render(request,'app/index.html',{'d':output})
def pruebita(request):
  return HttpResponse("esto es pruebitaaaa")

def pruebatemplate(request):
  output =['1','2']
  return render(request,'app/pruebatemplate.html',{'d':output})














def foo_view(request):
  script_dir = os.path.dirname(__file__)
  #print script_dir
  file_path = os.path.join(script_dir, 'config.json')
  #print file_path
  with open(file_path) as fi:
    data = json.loads(fi.read)
  output=[]
  for item in range(len(data['test'])):
   #print 'Current item :', str(data['test'][item]['value']) 
   tipoTest= str(data['test'][item]['value'])
   output.append('<option value=%s>%s</option>'%(tipoTest,tipoTest)) 
  #print "antes del return"
  #print output 
  #print output.__class__.__name__ 
  #return output    
  return render_to_response (request,'app/main.html',{'data': output})
    #parseJson = json.dumps(data, indent=4,sort_keys=True)
    #print (parseJson.__class__.__name__)
  #print parseJson
  '''output=[]
  for item in range(len(data['test'])):
   #print 'Current item :', str(data['test'][item]['value']) 
    tipoTest= str(data['test'][item]['value'])
    output.append('<option value=%s>%s</option>'%(tipoTest,tipoTest)) '''
  #print "antes del return"
  #print output 
  #print output.__class__.__name__ 
  #return output '''
  #d = {'one':'itemone', 'two':'itemtwo', 'three':'itemthree'}
  #d = {"test": [{"value": "Anova"},{"value": "Saphiro-wilk"},{"value": "Levene"},{"value": "Welch"},{"value": "Kruskal-Wallis"}]}
  #d = {'a':{'c':2, 'd':4 }, 'b': {'c':'value', 'd': 3}}
  #return render(request,'app/index.html',d)
  #return render_to_response('app/main.html', {'resources':resources})
  #return render (request,'app/main.html',{'results': data})
  '''
    decoded_json = json.loads('config.json')
    return render('app/main.html',{'results':decoded_json['Result']})'''

'''import json
import os
from pprint import pprint
def selection():
  script_dir = os.path.dirname(__file__)
  #print script_dir
  file_path = os.path.join(script_dir, 'data.json')
  #print file_path
  with open(file_path, 'r') as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
    #print (parseJson.__class__.__name__)
  #print parseJson
  output=[]
  for item in range(len(data['test'])):
   #print 'Current item :', str(data['test'][item]['value']) 
   tipoTest= str(data['test'][item]['value'])
   output.append('<option value=%s>%s</option>'%(tipoTest,tipoTest)) 
  #print "antes del return"
  #print output 
  print output.__class__.__name__ 
  return output  '''  