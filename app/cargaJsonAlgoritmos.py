
import json
import os

#cargar json de algoritmos
def jsonAlgoritmo(request):
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, 'algoritmos.json')
  with open(file_path) as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
    print parseJson
  outputAlgoritmo=[]  
  for item in range(len(data['algoritmo'])):
   #print 'Current item :', str(data['test'][item]['value']) 
    tipoAlgoritmo= str(data['algoritmo'][item]['value'])
    print tipoAlgoritmo
    outputAlgoritmo.append(tipoAlgoritmo) 
  return {'algoritmo':outputAlgoritmo}