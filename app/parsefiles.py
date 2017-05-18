import os,tarfile,zipfile,re,collections
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
from statisticTest import shapiroWilkTest,kruskalWallisTest,leveneTest,anovaTest,welchTest,pvalueMajor,pvalueMinor
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
	#PREPARACION PARA EL CALCULO DE REFERENCIA DEL HIPERVOLUMEN...(PASARLO A UNA FUNCION)

	referencePoint = referencePointInit(int(getConfiguration.nAlgorithms),int(getConfiguration.nObjectives))
	print referencePoint
	referencePoint = referencePointCalculation(dicAlg,referencePoint)
	print 'punto de referencia:'			
	print referencePoint
	dictHvAlg = collections.defaultdict(dict)
	hyperVolumeList = []
	for k,v in sorted(dicAlg.iteritems()):
		dictHvAlg[str(k)] = dict()
		hypervolumeAlgorithmList = []
		for kk,vv in sorted(v.iteritems()):
			for kkk,vvv in sorted(vv.iteritems()):
				if not kkk in dictHvAlg[str(k)].keys():
					dictHvAlg[k][kkk] = []
				hyperVolume = HyperVolume(referencePoint[int(k)])
				hypervolumeAlgorithmList.append(hyperVolume.compute(vvv))
				dictHvAlg[k][kkk].append(hyperVolume.compute(vvv))
		hyperVolumeList.append(hypervolumeAlgorithmList)
	print dictHvAlg

	#REALIZACION DE LOS DATAFRAME CON PANDAS DE LOS HIPERVOLUMENES POR PASO Y POR ALGORITMO.
	df = mainDataFrame(dictHvAlg)
	print df
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
	if 'Shapiro-wilk' in tests:
		#retorna el pvalue 
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'se distribuyen normalmente'
		else:
			print 'no se distribuye normalmente se pasaria a kruskal'

	if 'Kruskal-Wallis' in tests:
		print 'entre en kruskal'
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueminor(shapiroWilk)
		if shapiroWilktest == True:
			print 'no se distribuye normalemente se realizara el test de kruskal-wallis'
			kruskalWallis = kruskalWallisTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			print kruskalWallis
			if kruskalWallis[0][1] <0.05:
				print 'las medianas son iguales'
			else:
				print 'las medianas no son iguales.'
		else:
			print 'se distribuyen normalmente'
	if 'Levene' in tests:
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'se distribuyen normalmente se pasa a hacer levene'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			if levene[0][1] >= 0.05:
				print 'existe homogeneidad en las varianzas se podria pasar a realizar ANOVA'
			else:
				print 'no existe homogeneidad entre las varianzas'
		else:
			print 'no se distribuye normalmente se pasaria a kruskal'
		
	if 'Anova' in tests:
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'se distribuyen normalmente se pasa a hacer levene'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			if levene[0][1] >= 0.05:
				print 'existe homogeneidad en las varianzas se podria pasar a realizar ANOVA'
				anova = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				if anova[0][1] < 0.05:
					print 'existen diferencias significativas'
				else:
					print 'no existen diferencias significativas...'
	if 'Welch' in tests:
		print 'hacer welch...'
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'se distribuyen normalmente se pasa a hacer levene'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			if levene[0][1] < 0.05:
				print 'no existe homogeneidad en las varianzas se realiza welch'
				welch = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				if welch[0][1] < 0.05:
					print 'se realiza anova...'
					anova = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
					if anova[0][1] < 0.05:
						print 'existen diferencias significativas'
					else:
						print 'no existen diferencias significativas...'
			else:
				print 'existe homogeneidad entre las varianzas'
		else:
			print 'no se distribuye normalmente se pasaria a kruskal'
	'''if 'Kruskal-Wallis' in tests:
		print 'entre en kruskal'
		shapiroWilk = shapiro(int(getConfiguration.nAlgorithms),hyperVolumeList)
		#si todos los pvalues son <0.05 se realiza el test de kruskal-wallis
		shapiroWilktest = pvalueMinor(shapiroWilk)
		print shapiroWilktest
		if shapiroWilktest == True:
			print 'entre al if kruskal=true'
			kruskalWallis =  kruskalWallisTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			print kruskalWallis
		else:
			print 'se tiene una distribucion normal por tanto no se puede realizar kruskal wallis'
	if 'Levene' in tests:
		print 'seleccionado levene'
		shapiroWilk = shapiro(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'entre en lvntst true'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			print levene
		else:
			print 'no se cumplre shapiroWilk'
			pass
	if 'Anova' in tests:
		print 'seleccionado Anova...'
		shapiroWilk = shapiro(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'entre en lvntst true'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			lvnTest = pvalueMajor(levene)
			if lvnTest == True:
				print 'p value >=0.05 se realizara anova...'
				anova = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			else:
				print 'probabilidad >0.05 por tannto se realiza welch para luego hacer anova...'
				welch = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				wlchtest = pvalueMinor(welch)
				if wlchtest == True :
					anova = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		print anova
	if 'Welch' in tests:
		shapiroWilk = shapiro(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)
		if shapiroWilktest == True:
			print 'entre en lvntst true'
			levene = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			lvnTest = pvalueMinor(levene)
			if lvnTest == True:
				welch = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		print welch

		#stats.kruskal(algoritmo1, algoritmo2)
	print shapiroWilk'''
	#REALIZAR LOS TEST ESTADISTICOS...
	'''ORDEN DE REALIZACION DE LOS TESTS...
		1. SHAPIRO WILK
			- . SI P<0.05 KRUSKAL-WALLIS
			- . SI P>0.05 LEVENE
		2.  SI LEVENE DA P>= 0.05 -> ANOVA
			SI LEVENE DA P <0.05 -> WELCH
		3. SI WELCH DA P <0.05 -> ANOVA
	POR TANTO SI EL USUARIO INTRODUCE ANOVA, HAY QUE REALIZAR TODOS LOS TEST ANTERIORES
	EN CASI DE QUE SELECCIONE LEVENE POR EJEMPLO, PUES SHAPIRO-WILK (P>=0.05) Y REALIZAR LEVENE'''


	

	
