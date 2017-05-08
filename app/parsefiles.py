import os,tarfile,re,collections
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration
import numpy as np
import pandas as pd

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
	print 'esto es getconfiguration'
	print getConfiguration.nObjectives
	print (type(getConfiguration.nObjectives))
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
	for i,member in enumerate(files):
		#print 'estoy en el for de enumerate files'
		#print i
		#print member
		for j,file in enumerate(files[i]):
			#print 'estoy en el for de j'
			#print j
			#print 'esto es el nombre del fichero'
			#print file.name
			pattern = re.search('\d+',os.path.splitext(file.name)[0])
			index = pattern.start()
			sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
			print 'esto es sortedByfilename'
			print (sortedByFilename)
		files[i] = sortedByFilename
	print files
	print (len(files))
	dicAlg = collections.defaultdict(dict) #diccionario principal de algoritmos (dentro de el habra otro de ejecuciones con sus pasos)
	print dicAlg
	for i,member in enumerate(files):
		print i
		print member
		for j,file in enumerate(files[i]):
			print j
			print file
			f = tar.extractfile(file)
			dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
			for k,line in enumerate(f.readlines()):
				print 'estoy aqui..'
				print line
				#aqui lee el paso..
				if re.search('^[#]?\s*\w+\s*\d+\n',line):
					step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()
					
					if not step in dicAlg[str(i)][str(j)].keys():
						dicAlg[str(i)][str(j)][step]=[]
				#aqui lee las soluciones..
				else:
					Data =np.fromstring(line, dtype=float, sep=' ')
					indexObjectives = -int(getConfiguration.nObjectives)
#=============================================================================================================================
				#SI EL PASO ESTA ENTRE LAS CLAVES DEL DICCIONARIO, SE CREA UN ARRAY ON LAS SOLUCIONES Y SOLO SE COGE
				#LAS SOLUCIONES DE LOS OBJETIVOS DEPENDIENDO DEL NUMERO DE OBJETIVOS QUE SE HAYA INSERTADO.
#=============================================================================================================================
					if step in dicAlg[str(i)][str(j)].keys():
						print 'esto lee las soluciones'
						solution = []
						print dicAlg[str(i)][str(j)][step]
						while indexObjectives < 0:
							solution.append(Data[indexObjectives])
							indexObjectives +=1
						dicAlg[str(i)][str(j)][step].append(solution)
	print dicAlg
	#sortDictAlg = sorted(dicAlg.keys(),key=lambda x:str(x))
	'''for k,v in dicAlg.iteritems():
		'aqui sale el algoritmo y la v es el diccionario entero'
		print 'pruebasorted ejecuciones'
		print dicAlg[k].keys()
		#sorted(data, key=lambda item: (int(item.partition(' ')[0])
                               #if item[0].isdigit() else float('inf'), item))

		#sortDictAlg = sorted(dicAlg[k].keys(),key=lambda item: (int))
		for kk,vv in v.iteritems():
			print 'esto es kk y vv'
			print kk
			print vv'''
	print 'ESTO ES LO FINALLL ORDENADO...'
	#PREPARACION PARA EL CALCULO DE REFERENCIA DEL HIPERVOLUMEN...(PASARLO A UNA FUNCION)
	counter = 0
	coordinate = 0
	referencePoint = []
	while counter < int(getConfiguration.nObjectives):
		referencePoint.append(0)
		counter +=1
	maxStepValue = 0
	maxExecutionValue = 0
	print 'esto es referencePoint '
	print referencePoint
	for k,v in sorted(dicAlg.iteritems()):
		print 'ESTO ES K Y V'
		print k
		print v
		
		for kk,vv in sorted(v.iteritems()):
			print 'esto es kk y vv'
			print kk
			print vv
			
			for kkk,vvv in sorted(vv.iteritems()):
				print 'esto es kkk y vvv'
				#print 'aqui se calcula el punto de referencia...'
				print kkk
				print vvv
				for x,val in enumerate(vvv):
					'''print 'esoty en el for de enumerate vvv'
					print x
					print val
					print val[0]
					print len(val)'''
					counter = 0
					coordinate = 0
					while counter < len(val):
						'''print 'estoy en el whiile'
						print(val[counter])
						print (referencePoint[counter])'''
						if val[counter] > referencePoint[counter]:
							coordinate +=1
						counter +=1
					if coordinate == counter:
						referencePoint = val 
				'''maxStepValue = max(vvv)
				maxStepValue2 = max (vvv, key=tuple)
				print 'esto es maxvalue'
				print maxStepValue2
				if maxStepValue2 >referencePoint:
					referencePoint = maxStepValue2
					print 'max execution > que reference point se sustituye'
					print maxStepValue2'''
			

	print 'punto de referencia:'			
	print referencePoint
				#buscar los hipervolumenes y los puntos de referencia en vvv y crear un unico diccionario de diccionario por algoritmos de hipervolumenes

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