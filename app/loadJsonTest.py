#sirve para pasarle parametros a las templates calculados ejemplo.. pasarle un json
import json
import os
def jsonTest(request):
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, 'config/tests.json')
  with open(file_path) as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
  outputTest=[]  
  for item in range(len(data['test'])):
   #print 'Current item :', str(data['test'][item]['value']) 
    tipoTest= str(data['test'][item]['value'])
    outputTest.append(tipoTest)
  return {'test':outputTest}