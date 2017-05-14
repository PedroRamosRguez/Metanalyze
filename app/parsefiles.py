import os,tarfile,re,collections
import numpy as np
import pandas as pd
import createModels as cModels
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration,ChartsModel
from hv import HyperVolume

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
		#if re.search(r'^\w+\s*\d*\.{1}tar\.{1}gz$',fileName):
		if re.search(r'^[\w+\s*]+\.{1}tar\.{1}gz$',fileName):
			print 'el fichero es un tar.gz'
			tar = tarfile.open(dir+str(fileName),'r:gz')
			for member in tar.getmembers():
				fileList.append(member)
			files[i] = fileList 
		elif re.search(r'^[\w+\s*]+\.{1}tar$',fileName):
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
			pattern = re.search('\d+$',os.path.splitext(file.name)[0])
			index = pattern.start()
			#print (int(os.path.splitext(name.name)[0][index]))
			#sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
			sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))#eliminado el dospuntos
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
				if re.search('^[#]?\s*\w+\s*\d+\n+',line):
					step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()
					
					if not step in dicAlg[str(i)][str(j)].keys():
						dicAlg[str(i)][str(j)][step]=[]
				#se detecta que el paso venga dado de la manera 200(200)\n,200 (200)\n y se elimina la parte del parentesis
				elif re.search('^\d+\s*\(\d+\)\n+',line):
					print 'esto lee el paso...'
					step = re.sub('\(\d+\)\n+','',str(line))
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
					if Data[0] == -1.0:
						print 'no debe leer esto..'
					if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
						print 'esto lee las soluciones'
						solution = []
						print dicAlg[str(i)][str(j)][step]
						print 'esto es index objetivos %s'%str(indexObjectives)
						print Data
						print type(Data)
						print Data[0]
						while indexObjectives < 0:
							print 'estoy en el while...'
							print solution
							print Data
							print Data[indexObjectives]
							solution.append(Data[indexObjectives])
							indexObjectives +=1
						print 'sali del while...'
						dicAlg[str(i)][str(j)][step].append(solution)

				print dicAlg
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
	dictHvAlg = collections.defaultdict(dict)
	#dicHvAlg = collections.defaultdict(dict)
	#dictHv = dict()		#diccionario con los valores de hipervolumenes por paso y ejecucion
	#dictHvAlg[0] = dict()
	print (dictHvAlg)
	for k,v in sorted(dicAlg.iteritems()):
		print 'ESTO ES K Y V del hipervolumen'
		print k
		print v
		dictHvAlg[str(k)] = dict()
		for kk,vv in sorted(v.iteritems()):
			print 'esto es kk y vv del hipervolumen'
			print kk
			print vv

			print dictHvAlg
			for kkk,vvv in sorted(vv.iteritems()):
				print 'esto es kkk y vvv del hipervolumen'
				print kkk
				print vvv
				if not kkk in dictHvAlg[str(k)].keys():
					dictHvAlg[k][kkk] = []
				hyperVolume = HyperVolume(referencePoint)
				dictHvAlg[k][kkk].append(hyperVolume.compute(vvv))
	print dictHvAlg
	#pasar como argumento al grafico los valores del diccionario...
	df = []
	for k,v in sorted(dictHvAlg.iteritems()):
		print k
		print v
		df.append(pd.DataFrame(v))
	print 'fuera del for de creacion de dataframes'
	print df
	print 'AHORA SERIA EL FOR DE DICTHVALG CON K Y V'
	chartList =[]
	for k,v in sorted(dictHvAlg.iteritems()):
		print 'ESTO ES K Y V'
		print k
		print v
		algList = []
		for step,val in sorted(v.iteritems()):
			print 'ESTO ES STEP Y VAL:'
			print step
			print val
			#stepList=[]
			for i,value in enumerate(val):
				print 'ESTO ES I Y VALUE'
				print i
				print value
				algList.append({'x':str(step),'y':str(value)})
			#print 'esto es step list y charlist'
			#print stepList
			#print chartList
		#algList.append(stepList)
		chartList.append(algList)
	#comprobar en la configuracion que bound selecciono...
	cModels.modelCharts(idConfiguration,chartList)
	df2 = []
	dfMin = []
	dfAvg = []
	dfMax = []
	for i,v in enumerate(df):
		print i
		print v
		df2.append(pd.DataFrame(v.min(),columns=['Min']))
		dfMin.append(pd.DataFrame(v.min(),columns=['Min']))
		df2[i]['Average']=v.mean()
		df2[i]['Max'] = v.max()
		#df2['Average']=df.mean()
		dfAvg.append(pd.DataFrame(v.mean(),columns=['Avg']))
		dfMax.append(pd.DataFrame(v.max(),columns=['Max']))
		#df2['Max']=df.max()
	'''df2 = pd.DataFrame(df.min(),columns=['Min'])
	df2['Average']=df.mean()
	df2['Max']=df.max()'''
	print 'print de los dataframes de min max y avg y el total...'
	print df2
	print dfMin
	print dfAvg
	print dfMax
	#pasar a diccionario cada dataframe
	#idConfiguration
	#cModels.modelMinAvgMaxCharts()
	modeList = []
	for i,v in enumerate(df2):
		#print v.to_dict()
		modeList.append(v.to_dict())
	print 'esto es la lista de dataframes...'
	print modeList
	print len(modeList)
	cModels.modelMinAvgMaxCharts(idConfiguration,modeList)
	modeList = []
	for i,v in enumerate(dfMin):
		#print v.to_dict()
		modeList.append(v.to_dict())
	cModels.modelMinCharts(idConfiguration,modeList)
	modeList = []
	for i,v in enumerate(dfAvg):
		#print v.to_dict()
		modeList.append(v.to_dict())
	cModels.modelAvgCharts(idConfiguration,modeList)

	modeList = []
	for i,v in enumerate(dfMax):
		#print v.to_dict()
		modeList.append(v.to_dict())
	cModels.modelMaxCharts(idConfiguration,modeList)
	#cModels.modelCharts(idConfiguration,objeto)

	#prueba.get_datasets(pruebita)

				#buscar los hipervolumennes y los puntos de referencia en vvv y crear un unico diccionario de diccionario por algoritmos de hipervolumenes

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