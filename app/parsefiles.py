import os,tarfile,re
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
	#obtine los algoritmos filtrando por la configuracion que se le ha pasado...(genera un diccionario de algoritmos ya que pueden ser muchos.)
	getAlgorithms = Algorithms.objects.filter(configuration__id=idConfiguration).values().distinct()
	print getAlgorithms
	#obtine el modelo de configuracion con el id que se le pasa..
	getConfiguration = Configuration.objects.get(id=idConfiguration)
	files = []  #lista de nombre de ficheros tar de los algoritmos...
	
	for i,item in enumerate(getAlgorithms):
		files.append(str(item['fileName']))
	print files
	for i,fileName in enumerate(files):
		print i
		print fileName
		print type(fileName)
		fileList = []  #lista donde se guardara la lista de ficheros que tenga ese tarfile o zipfile. (ESTP SERA UNA LISTA DE LISTAS)
		#meter esto es una funcion
		if re.search(r'^\w+\s*\d*\.{1}tar\.{1}gz$',fileName):
			print 'el fichero es un tar.gz'
			tar = tarfile.open(dir+str(fileName),'r:gz')
			for member in tar.getmembers():
				fileList.append(member)
			files[i] = fileList 
		elif re.search(r'^\w+\s*\d*\.{1}tar$',fileName):
			print 'el fichero es un tar'
			tar = tarfile.open(dir+str(fileName))
			for member in tar.getmembers():
				fileList.append(member)
			files[i] = fileList		
		else:
			print 'el fichero es .zip'
	print files
	print (len(files))
	print (len(files[0]))
	print (len(files[1]))
	for i,member in enumerate(files):
		print 'estoy en el for de enumerate files'
		print i
		print member
		for j,file in enumerate(files[i]):
			print 'estoy en el for de j'
			print j
			print 'esto es el nombre del fichero'
			print file.name
			pattern = re.search('\d+',os.path.splitext(file.name)[0])
			index = pattern.start()
			sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
			print 'esto es sortedByfilename'
			print (sortedByFilename)
		files[i] = sortedByFilename
	print files
	print (len(files))
	print (len(files[0]))
	
	#algDict = dict()		#crea un diccionario de algoritmos.
	#executionDict = dict([x, algDict] for x in range(configuration.nExecutions)) #crea un numero de diccionarios igual a el numero de ejecuciones realizadas.
	#stepDict = dict([x, executionDict] for x in range(configuration.n))

			#aqui iria el abrir el fichero zip pero hay que usar el modulo zipfile
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