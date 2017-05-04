import os,tarfile
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration
def parse(idConfiguration):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	print BASE_DIR
	dir = os.path.join(BASE_DIR, 'media/')
	print dir
	'''myapp = apps.get_app('app')
	for model in get_models(myapp):
		print (model)'''
	#prueba = Configuration.objects.get(id=82)
	#atributo = getattr(prueba,'nAlgorithms')
	#print 'esto es atributo: %s'%atributo
	print idConfiguration
	print type(idConfiguration)
	'''prueba = Configuration.objects.filter(id=idConfiguration)
	print prueba
	print prueba[0].id
	prueba2 = Algorithms.objects.filter(configuration=prueba[0].id)
	print prueba2[0].algorithm'''
	getAlgorithms = Algorithms.objects.filter(configuration__id=idConfiguration).values().distinct()
	print getAlgorithms
	fileList = []
	for i,item in enumerate(getAlgorithms):
		print item['fileName']
		#esto seria una lista de lista
		'''if re.search('^\w+\s*\d*.tar.gz$'):
			tar = tarfile.open(dir+str(item['fileName']),'r:gz')
			for member in tar.getmembers():
				fileList.append(member)
			#crea una lista ordenada por nombre de ficheros
			for name in fileList:
				pattern = re.search('\d+',os.path.splitext(name.name)[0])
				index = pattern.start()
				sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
			fileList= sortedByFilename'''
	#pruebaConfig = Configuration(instance=prueba)
	#print model.objects.filter('Algorithms')
	#print (myapp.models)
	
	#


	#tar = tarfile.open(dir+str('pruebita.tar.gz'),'r:gz')


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