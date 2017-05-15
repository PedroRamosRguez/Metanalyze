import os,tarfile,re,collections
import numpy as np
import pandas as pd
import createModels as cModels
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration,ChartsModel
from hv import HyperVolume
from ordena import ordena
from extrae import extrae
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
	print len(files)
	fileSorted = []
	dicAlg = collections.defaultdict(dict)
	for i,fileName in enumerate(files):
		fileList = []  #lista donde se guardara la lista de ficheros que tenga ese tarfile o zipfile. (ESTP SERA UNA LISTA DE LISTAS)
		#meter esto es una funcion
		#if re.search(r'^\w+\s*\d*\.{1}tar\.{1}gz$',fileName):
		if re.search(r'^[\w+\s*]+\.{1}tar\.{1}gz$',fileName):
			print 'el fichero es un tar.gz'
			tar = tarfile.open(dir+str(fileName),'r:gz')
			for member in tar.getmembers():
				fileList.append(member)
			'''for i,name in enumerate(fileList):
				pattern = re.search('\d+',os.path.splitext(name.name)[0])
				index = pattern.start()
				print (int(os.path.splitext(name.name)[0][index:]))
				sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))'''
			sortedByFilename = ordena(fileList)
			fileSorted.append(sortedByFilename)
			for j,member in enumerate(fileSorted):
				print 'esto es j y member'
				print j
				print member
				print 'len de member %d'%int(len(member))
				print tar
				dictionary = extrae(tar,i,dicAlg,member,getConfiguration)

		elif re.search(r'^[\w+\s*]+\.{1}tar$',fileName):
			print 'el fichero es un tar'
			tar = tarfile.open(dir+str(fileName))
			for member in tar.getmembers():
				fileList.append(member)
			sortedByFilename = ordena(fileList)
			fileSorted.append(sortedByFilename)
			
			for j,member in enumerate(fileSorted):
				print 'esto es i y member'
				print j
				print member
				print 'len de member %d'%int(len(member))
				print tar
				dictionary = extrae(tar,i,dicAlg,member,getConfiguration)
		else:
			print 'el fichero es .zip'
		fileSorted = []
		dicAlg = dictionary
		print 'print no peto la igualacion'
	print 'esto es dicalg fuera...'
	print dicAlg
	#print fileSorted
	#print (len(fileSorted))
	#print tar
	#dicAlg = collections.defaultdict(dict) #diccionario principal de algoritmos (dentro de el habra otro de ejecuciones con sus pasos)
	'''for i,member in enumerate(fileSorted):
		print 'esto es i y member'
		print i
		print member
		print 'len de member %d'%int(len(member))
		print tar
		extrae(i,dicAlg,member)
		for j,file in enumerate(member):
			print j
			print file
			f = tar.extractfile(file)
			print f.name
			dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
			print dicAlg.keys()
			print dicAlg
			for k,line in enumerate(f.readlines()):
				
				print 'esto es k:%d'%int(k)
				print 'esto es line:'
				print line
				if re.search('^[#]?\s*\w+\s*\d+\n+',line):
					print 'esto es el paso...'
					step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()
					if not step in dicAlg[str(i)][str(j)].keys():
						print 'la clave del paso no existe...'
						print 'esto es step:%s'%step
						print 'claves:'
						print dicAlg[str(i)][str(j)].keys()
						dicAlg[str(i)][str(j)][step]=[]
				#se detecta que el paso venga dado de la manera 200(200)\n,200 (200)\n y se elimina la parte del parentesis
				elif re.search('^\d+\s*\(\d+\)\n+',line):
					print 'esto lee el paso...'
					step = re.sub('\(\d+\)\n+','',str(line))
					if not step in dicAlg[str(i)][str(j)].keys():
						dicAlg[str(i)][str(j)][step]=[]
				#aqui lee las soluciones..
				else:
					print 'aqui lee las soluciones'
					Data =np.fromstring(line, dtype=float, sep=' ')
					print Data
					indexObjectives = -int(getConfiguration.nObjectives)
#=============================================================================================================================
				#SI EL PASO ESTA ENTRE LAS CLAVES DEL DICCIONARIO, SE CREA UN ARRAY ON LAS SOLUCIONES Y SOLO SE COGE
				#LAS SOLUCIONES DE LOS OBJETIVOS DEPENDIENDO DEL NUMERO DE OBJETIVOS QUE SE HAYA INSERTADO.
#=============================================================================================================================
					if Data[0] == -1.0:
						print 'no debe leer esto..'
					if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
						#print 'esto lee las soluciones'
						solution = []
						print dicAlg[str(i)][str(j)][step]
						#print 'esto es index objetivos %s'%str(indexObjectives)
						#print Data
						#print type(Data)
						#print Data[0]
						while indexObjectives < 0:
							print 'esto es el file...'
							print file
							#print 'estoy en el while...'
							#print solution
							#print Data
							#print Data[indexObjectives]
							solution.append(Data[indexObjectives])
							indexObjectives +=1
						print 'sali del while...'
						dicAlg[str(i)][str(j)][step].append(solution)
		print 'esto es i:%d'%i
		print 'esto es dicAlg'''
		#print dicAlg

	
	'''
	for i,member in enumerate(files):
		#print i
		print 'esto es member en el bucle de despues...'
		print member
		print type(member)
		for j,file in enumerate(member):
			print 'for del enumerate member'
			print j
			print file
			
			f = tar.extractfile(file)
			dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
			for k,line in enumerate(f.readlines()):
				#print 'estoy aqui..'
				#print line
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
					if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
						print 'esto lee las soluciones'
						solution = []
						#print dicAlg[str(i)][str(j)][step]
						#print 'esto es index objetivos %s'%str(indexObjectives)
						#print Data
						#print type(Data)
						#print Data[0]
						while indexObjectives < 0:
							#print 'estoy en el while...'
							#print solution
							#print Data
							#print Data[indexObjectives]
							solution.append(Data[indexObjectives])
							indexObjectives +=1
						#print 'sali del while...'
						dicAlg[str(i)][str(j)][step].append(solution)'''



		#print 'cambia i...'
		#print 'diccionario en el i actual: '
		#print dicAlg[]
		#print 'dicalg en el else...'
		#print 'esto es i= %d'%i
		#print dicAlg
	#print 'dicalg fuera...'
	#print dicAlg
	#print 'esto es dicalg0'
	#print dicAlg['0']
	#print 'y esto es dicalg1'
	#print dicAlg['1']
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




	'''print 'ESTO ES LO FINALLL ORDENADO...'
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
		print 'ESTO ES K Y V para el calculo del punto de referencia...'
		print k
		print v
		print 'claves del dicalg'
		print dicAlg.keys()
		for kk,vv in sorted(v.iteritems()):
			#print 'esto es kk y vv'
			#print kk
			#print vv
			
			for kkk,vvv in sorted(vv.iteritems()):
				#print 'esto es kkk y vvv'
				#print 'aqui se calcula el punto de referencia...'
				#print kkk
				#print vvv
				for x,val in enumerate(vvv):
					#print 'esoty en el for de enumerate vvv'
					#print x
					#print val
					#print val[0]
					#print len(val)
					counter = 0
					coordinate = 0
					while counter < len(val):
						#print 'estoy en el whiile'
						#print(val[counter])
						#print (referencePoint[counter])
						if val[counter] > referencePoint[counter]:
							coordinate +=1
						counter +=1
					if coordinate == counter:
						referencePoint = val 
			'''

	print 'punto de referencia:'			
	#print referencePoint
	dictHvAlg = collections.defaultdict(dict)
	#dicHvAlg = collections.defaultdict(dict)
	#dictHv = dict()		#diccionario con los valores de hipervolumenes por paso y ejecucion
	#dictHvAlg[0] = dict()



	'''for k,v in sorted(dicAlg.iteritems()):
		print 'ESTO ES K  del hipervolumen'
		print k
		print 'esto es el valor de k del hipervolumen'
		print dicAlg[str(k)].items()
		dictHvAlg[str(k)] = dict()
		for kk,vv in sorted(v.iteritems()):
			#print 'esto es kk y vv del hipervolumen'
			#print kk
			#print vv

			print dictHvAlg
			for kkk,vvv in sorted(vv.iteritems()):
				#print 'esto es kkk y vvv del hipervolumen'
				#print kkk
				#print vvv
				if not kkk in dictHvAlg[str(k)].keys():
					dictHvAlg[k][kkk] = []
				hyperVolume = HyperVolume(referencePoint)
				dictHvAlg[k][kkk].append(hyperVolume.compute(vvv))
	print dictHvAlg'''

	#pasar como argumento al grafico los valores del diccionario...
	df = []


	'''for k,v in sorted(dictHvAlg.iteritems()):
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
	#print 'esto es dicAHValg'
	#print dictHvAlg
	#comprobar en la configuracion que bound selecciono...
	cModels.modelCharts(idConfiguration,chartList)
	df2 = []
	dfMin = []
	dfAvg = []
	dfMax = []'''

	'''print 'esto es la lista de df...'
	print df
	print len(df)'''
	'''for i,v in enumerate(df):
		print i
		print v
		df2.append(pd.DataFrame(v.min(),columns=['Min']))
		dfMin.append(pd.DataFrame(v.min(),columns=['Min']))
		df2[i]['Average']=v.mean()
		df2[i]['Max'] = v.max()
		#df2['Average']=df.mean()
		dfAvg.append(pd.DataFrame(v.mean(),columns=['Avg']))
		dfMax.append(pd.DataFrame(v.max(),columns=['Max']))
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
	#cModels.modelCharts(idConfiguration,objeto)'''