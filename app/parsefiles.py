import os,tarfile
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration
def parse():
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	print BASE_DIR
	dir = os.path.join(BASE_DIR, 'media/')
	print dir
	'''myapp = apps.get_app('app')
	for model in get_models(myapp):
		print (model)'''
	myapp = apps.get_model(app_label='app',model_name='Algorithms')
	print myapp
	print Configuration
		#print model.objects.filter('Algorithms')
	#print (myapp.models)
	
	#tar = tarfile.open(dir+str('pruebita.tar.gz'),'r:gz')
	fileList = []
	'''dir = os.path.join(BASE_DIR, 'Documentos/pruebaficheros/')
	tar = tarfile.open(dir+str('pruebita.tar.gz'),'r:gz')
	fileList = []
	#crear lista de ficheros desordenados
	for member in tar.getmembers():
		fileList.append(member)
	#crea una lista ordenada por nombre de ficheros
	for name in fileList:
		pattern = re.search('\d+',os.path.splitext(name.name)[0])
		index = pattern.start()
		sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
	fileList= sortedByFilename'''