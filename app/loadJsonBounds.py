#sirve para pasarle parametros a las templates calculados ejemplo.. pasarle un json
import json
import os
def jsonBound(request):
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, 'config/bounds.json')
  with open(file_path) as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
  outputBound=[]  
  for item in range(len(data['bound'])):
   #print 'Current item :', str(data['test'][item]['value']) 
    tipoBound= str(data['bound'][item]['value'])
    outputBound.append(tipoBound)
  return {'bound':outputBound}