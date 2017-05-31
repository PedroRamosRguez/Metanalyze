import os,tarfile,zipfile,re,collections,sys
import createModels as cModels
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration,ChartsModel
from hv import HyperVolume
from sortFiles import sortFiles
from parse import parseFiles,parseZipFiles
from referencePoint import referencePointInit,referencePointCalculation
from setChartModels import setChart,setMinAvgMaxChart,setMinChart,setAvgChart,setMaxChart
from setDataframes import mainDataFrame,minAvgMaxDataFrame,minDataFrame,avgDataFrame,maxDataFrame
from statisticTest import calculeMean,calculeMedian,shapiroWilkTest,kruskalWallisTest,leveneTest,anovaTest,welchTest,pvalueMajor,pvalueMinor
import numpy as np
import pandas as pd
import scipy.stats as stats
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
			sortedByFilename = sortFiles(fileList)
			fileSorted.append(sortedByFilename)
			for j,member in enumerate(fileSorted):
				dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)

		elif re.search(r'^[\w+\s*]+\.{1}tar$',fileName):
			print 'el fichero es un tar'
			tar = tarfile.open(dir+str(fileName))
			for member in tar.getmembers():
				fileList.append(member)
			sortedByFilename = sortFiles(fileList)
			fileSorted.append(sortedByFilename)
			
			for j,member in enumerate(fileSorted):
				dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)
		else:
			print 'el fichero es .zip'
			zf = zipfile.ZipFile(dir+str(fileName),'r')
			fileList = zf.namelist()
			dictionary = parseZipFiles(zf,i,dicAlg,fileList,getConfiguration)
		fileSorted = []
		dicAlg = dictionary
		print 'print no peto la igualacion'
	print 'esto es dicalg fuera...'
	print dicAlg
	#normalizar dicAlg
	#PREPARACION PARA EL CALCULO DE REFERENCIA DEL HIPERVOLUMEN...(PASARLO A UNA FUNCION)
	referencePoint = referencePointInit(int(getConfiguration.nAlgorithms),int(getConfiguration.nObjectives))

	referencePoint = referencePointCalculation(dicAlg,referencePoint)
	print 'punto de referencia:'

	print referencePoint
	#sys.exit('parada...')	
	dictHvAlg = collections.defaultdict(dict)
	hyperVolumeList = []
	for k,v in sorted(dicAlg.iteritems()):
		dictHvAlg[str(k)] = dict()
		hypervolumeAlgorithmList = []
		for kk,vv in sorted(v.iteritems()):
			for kkk,vvv in sorted(vv.iteritems()):
				if not kkk in dictHvAlg[str(k)].keys():
					dictHvAlg[k][kkk] = []
				hyperVolume = HyperVolume(referencePoint)
				hypervolumeAlgorithmList.append(hyperVolume.compute(vvv))
				dictHvAlg[k][kkk].append(hyperVolume.compute(vvv))
				print vv
				print vvv
				print referencePoint
				print dictHvAlg[k][kkk]
		#hyperVolumeList.append(hypervolumeAlgorithmList)
	print dictHvAlg
	print referencePoint
	print dictHvAlg['0']['8200']
	#normalizacion...
	listMin = []
	listMax = []
	for k,v in sorted(dictHvAlg.iteritems()):
		minAlgorithm = []
		maxAlgorithm = []
		for kk,vv in sorted(v.iteritems()):
			minAlgorithm.append(min(vv))
			maxAlgorithm.append(max(vv))
		listMin.append(minAlgorithm)
		listMax.append(maxAlgorithm)
	print listMin
	print listMax
	minValue = []
	maxValue = []
	for i,value in enumerate(listMin):
		minValue.append(min(listMin[i]))
		maxValue.append(max(listMax[i]))

	for k,v in sorted(dictHvAlg.iteritems()):
		hypervolumeAlgorithmList = []
		for kk,vv in sorted(v.iteritems()):
			newHvValue = []
			for i,value in enumerate(vv):
				num = float(value - minValue[int(k)])
				denom = float(maxValue[int(k)] - minValue[int(k)])
				newValue = float(num/denom)
				#si el problema es de maximizar se debe multiplicar por menos 1
				newValue = 1- newValue
				newHvValue.append(newValue)
				hypervolumeAlgorithmList.append(newValue)
			#sys.exit('parada')
			dictHvAlg[str(k)][str(kk)] = newHvValue
			#print dictHvAlg[str(k)][str(kk)]
		hyperVolumeList.append(hypervolumeAlgorithmList)
	print 'esto es dicthvalg despues ..'
	print dictHvAlg
	#sys.exit("PARADA...")
	#REALIZACION DE LOS DATAFRAME CON PANDAS DE LOS HIPERVOLUMENES POR PASO Y POR ALGORITMO.
	df = mainDataFrame(dictHvAlg)

	#CREACION DEL MODELO DE GRAFICOS
	chartList = setChart(dictHvAlg)
	
	cModels.modelCharts(idConfiguration,chartList)
	#CREACION DE LOS DATAFRAMES DE MIN,AVG Y MAX
	print 'llegue aqui..'
	dfMinAvgMax = minAvgMaxDataFrame(df)
	dfMin = minDataFrame(df)
	dfAvg = avgDataFrame(df)
	dfMax = maxDataFrame(df)
	print 'print de los dataframes de min max y avg y el total...'
	print dfMinAvgMax
	setMinAvgMaxChart(dfMinAvgMax,idConfiguration)
	setMinChart(dfMin,idConfiguration)
	setAvgChart(dfAvg,idConfiguration)
	setMaxChart(dfMax,idConfiguration)
	#print 'esto es la lista de hypervolumelist'
	#algorithmModel.save()
	print hyperVolumeList
	for i in range(int(getConfiguration.nAlgorithms)):
		Algorithms.objects.filter(id=int(getAlgorithms[i]['id'])).update(hypervolumeValues=hyperVolumeList[i])
	
	#obtener los nombres de los algoritmos para crear un df con las comparaciones...
	algorithm_names = []
	tests = getConfiguration.test
	print tests
	print len(tests)
	for i in range(int(getConfiguration.nAlgorithms)):
		algorithm_names.append(getAlgorithms[i]['algorithm'])


	print getConfiguration.anova
	if str(getConfiguration.anova) == 'si':
		#se realizara cada uno de los test...
		print 'entre al if...'
		#una prueba con dos arrays que si siguen una distribucion normal
		x = stats.norm.rvs(loc=5, scale=3, size=100)
		y = stats.norm.rvs(loc=5, scale=3, size=100)
		z = stats.norm.rvs(loc=5, scale=3, size=100)
		hyperVolumeList2 =[]
		algoritmo1 = []
		algoritmo2 = []
		algoritmo3 = []
		for i,v in enumerate(x):
			algoritmo1.append(v)
		hyperVolumeList2.append(algoritmo1)
		for i,v in enumerate(y):
			algoritmo2.append(v)
		hyperVolumeList2.append(algoritmo2)
		'''for i,v in enumerate(z):
			algoritmo3.append(v)
		hyperVolumeList2.append(algoritmo3)
		print hyperVolumeList2
		print len(hyperVolumeList2)'''
		
		#retorna el pvalue 
		#shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList2)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		print shapiroWilk
		print shapiroWilktest
		
		if shapiroWilktest == True:
			print 'se distribuyen normalmente'
			#levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			value = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList2)
			lvnTest = pvalueMajor(value)
			if lvnTest == True:
				#se  realizaria anova...
				#anova = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				value = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList2)
				print 'esto es value:'
				print value
			else:
				#welch = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				value = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList2)
			#sys.exit('parada...')
		else:
			print 'no se distribuye normalmente se pasaria a kruskal'
			#value = kruskalWallisTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			value = kruskalWallisTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			print 'esto es value:'
			print value
			#hacer media de cada uno de los algoritmos
			#hacer la mediana de cada uno de los algoritmos..
		#meanAlgorithms = calculeMean(hyperVolumeList)
		meanAlgorithms = calculeMean(hyperVolumeList2)
		#medianAlgorithms = calculeMedian(hyperVolumeList)
		medianAlgorithms = calculeMedian(hyperVolumeList2)
		print 'media y mediana'
		print meanAlgorithms
		print medianAlgorithms
		print 'esto es value'
		print value
		algorithm_names = []
		getAlgorithms = Algorithms.objects.filter(configuration__id=getConfiguration.id).values().distinct()
		for i in range(int(getConfiguration.nAlgorithms)):
			algorithm_names.append(str(getAlgorithms[i]['algorithm']))
      	statisticDftex = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
      	statisticDftxt = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
      	for i,v in enumerate(value):
      		j=i+1
      		if(v[1] < 0.05):

      			if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
      				print 'poner un asterisco en la tabla'
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
      				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
      			elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
      				print 'imprimir asterisco en la tabla'
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
      				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
      			elif medianAlgorithms[i] < medianAlgorithms[j]:
      				print 'flecha arriba algoritmo1 mejor que el 2'
      				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'+')
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],u'\u2191')
      				tatisticDftex.set_value(algorithm_names[j],algorithm_names[i],u'\u2193')
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
      				statisticDftex.set_value(algorithm_names[j],algorithm_names[j],u'\u2194')
      			elif medianAlgorithms[i] > medianAlgorithms[j]:
      				print 'flecha abajo, el algoritmo1 es peor que el 2'
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],u'\u2193')
      				statisticDftex.set_value(algorithm_names[j],algorithm_names[i],u'\u2191')
      				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'-')
      				statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
      				statisticDftex.set_value(algorithm_names[j],algorithm_names[j],u'\u2194')
      		else:
      			print 'no existen diferencias'
      			statisticDftex.set_value(algorithm_names[i],algorithm_names[j],u'\u2194')
      			statisticDftex.set_value(algorithm_names[j],algorithm_names[i],u'\u2194')
      			statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'=')
      			statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'=')
      	print statisticDftex
      	print statisticDftxt