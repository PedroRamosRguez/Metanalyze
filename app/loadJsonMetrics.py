import json
import os
def jsonMetric(request):
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, 'config/metrics.json')
  with open(file_path) as fi:
    data = json.load(fi)
    parseJson = json.dumps(data, indent=4,sort_keys=True)
  outputMetric=[]  
  for item in range(len(data['metric'])):
   #print 'Current item :', str(data['test'][item]['value']) 
    metric= str(data['metric'][item]['value'])
    outputMetric.append(metric)
  return {'metric':outputMetric}