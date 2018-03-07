import os,tarfile,zipfile,re,collections,subprocess
import createModels as cModels
from django.apps import apps
from django.db.models import get_app, get_models
from .models import Algorithms,Configuration,ChartsModel
from hv import HyperVolume
from sortFiles import sortFiles
from parse import parseFiles,parseZipFiles
from referencePoint import referencePointInit,referencePointCalculation
from setChartModels import setChart,setMinAvgMaxChart,setMinChart,setAvgChart,setMaxChart,setStatisticalDfTex,setStatisticalDfTxt,setStatisticalDfHtml
from setDataframes import mainDataFrame,minAvgMaxDataFrame,minDataFrame,avgDataFrame,maxDataFrame,statisticDataframetex,statisticDataframetxt,statisticDataframeHtml
from statisticTest import calculeMean,calculeMedian,shapiroWilkTest,kruskalWallisTest,leveneTest,anovaTest,welchTest,pvalueMajor,pvalueMinor
import pandas as pd
import scipy.stats as stats
def parse(idConfiguration):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	mediafolder = os.path.join(BASE_DIR, 'media/results/')
	dir = os.path.join(BASE_DIR, 'media/')
	#obtine los algoritmos filtrando por la configuracion que se le ha pasado...(genera un diccionario de algoritmos ya que pueden ser muchos.)
	getAlgorithms = Algorithms.objects.filter(configuration__id=idConfiguration).values().distinct()
	#obtine el modelo de configuracion con el id que se le pasa..
	getConfiguration = Configuration.objects.get(id=idConfiguration)

	files = []  #lista de nombre de ficheros tar de los algoritmos...
	
	for i,item in enumerate(getAlgorithms):
		files.append(str(item['fileName']))

	fileSorted = []
	dicAlg = collections.defaultdict(dict)
	for i,fileName in enumerate(files):
		fileList = []  #lista donde se guardara la lista de ficheros que tenga ese tarfile o zipfile. (ESTP SERA UNA LISTA DE LISTAS)
		if re.search(r'^[\w+\s*\d*]+\.{1}tar\.{1}gz$',fileName):
			#fichero tipo tar.gz
			tar = tarfile.open(dir+str(fileName),'r:gz')
			for member in tar.getmembers():
				fileList.append(member)
			
			sortedByFilename = sortFiles(fileList)
			fileSorted.append(sortedByFilename)
			for j,member in enumerate(fileSorted):
				dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)

		elif re.search(r'^[\w+\s*\d*]+\.{1}tar$',fileName):
			#fichero tipo tar
			tar = tarfile.open(dir+str(fileName))
			for member in tar.getmembers():
				fileList.append(member)
			
			sortedByFilename = sortFiles(fileList)
			fileSorted.append(sortedByFilename)
			
			for j,member in enumerate(fileSorted):
				dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)
		else:
			#fichero tipo zip
			zf = zipfile.ZipFile(dir+str(fileName),'r')
			fileList = zf.namelist()
			dictionary = parseZipFiles(zf,i,dicAlg,fileList,getConfiguration)
		fileSorted = []
		dicAlg = dictionary
		
	
	#PREPARACION PARA EL CALCULO DE REFERENCIA DEL HIPERVOLUMEN...(PASARLO A UNA FUNCION)
	referencePoint = referencePointInit(int(getConfiguration.nAlgorithms),int(getConfiguration.nObjectives))

	referencePoint = referencePointCalculation(dicAlg,referencePoint)
	
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
			
		hyperVolumeList.append(hypervolumeAlgorithmList)

	#REALIZACION DE LOS DATAFRAME CON PANDAS DE LOS HIPERVOLUMENES POR PASO Y POR ALGORITMO.
	df = mainDataFrame(dictHvAlg)

	#CREACION DEL MODELO DE GRAFICOS
	chartList = setChart(dictHvAlg)
	
	cModels.modelCharts(idConfiguration,chartList)
	#CREACION DE LOS DATAFRAMES DE MIN,AVG Y MAX
	
	dfMinAvgMax = minAvgMaxDataFrame(df)
	dfMin = minDataFrame(df)
	dfAvg = avgDataFrame(df)
	dfMax = maxDataFrame(df)
	
	setMinAvgMaxChart(dfMinAvgMax,idConfiguration)
	setMinChart(dfMin,idConfiguration)
	setAvgChart(dfAvg,idConfiguration)
	setMaxChart(dfMax,idConfiguration)
	#print 'esto es la lista de hypervolumelist'
	#algorithmModel.save()
	
	for i in range(int(getConfiguration.nAlgorithms)):
		Algorithms.objects.filter(id=int(getAlgorithms[i]['id'])).update(hypervolumeValues=hyperVolumeList[i])
	
	#obtener los nombres de los algoritmos para crear un df con las comparaciones...
	algorithm_names = []
	
	for i in range(int(getConfiguration.nAlgorithms)):
		algorithm_names.append(getAlgorithms[i]['algorithm'])

	if str(getConfiguration.statisticTest) == 'yes':
		#se realizara cada uno de los test...
		shapiroWilk = shapiroWilkTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
		shapiroWilktest = pvalueMajor(shapiroWilk)

		if shapiroWilktest == True:
			#se distribuyen normalmente
			value = leveneTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			lvnTest = pvalueMajor(value)
			if lvnTest == True:
				#se  realizaria anova...
				
				value = anovaTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
				
			else:
				#se realiza welch
				value = welchTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
			
		else:
			#no se distribuyen normalmente se realiza kruskal
			value = kruskalWallisTest(int(getConfiguration.nAlgorithms),hyperVolumeList)
	
		meanAlgorithms = calculeMean(hyperVolumeList)
		medianAlgorithms = calculeMedian(hyperVolumeList)
		algorithm_names = []
		getAlgorithms = Algorithms.objects.filter(configuration__id=getConfiguration.id).values().distinct()
		for i in range(int(getConfiguration.nAlgorithms)):
			algorithm_names.append(str(getAlgorithms[i]['algorithm']))


      	statisticDftex = statisticDataframetex(algorithm_names,value,meanAlgorithms,medianAlgorithms)
      	statisticDftxt = statisticDataframetxt(algorithm_names,value,meanAlgorithms,medianAlgorithms)
      	statisticDfhtml = statisticDataframeHtml(algorithm_names,value,meanAlgorithms,medianAlgorithms)
      	setStatisticalDfTex(statisticDftex,idConfiguration)
      	setStatisticalDfTxt(statisticDftxt,idConfiguration)
      	setStatisticalDfHtml(statisticDfhtml,idConfiguration)
      	filename = os.path.join(mediafolder,'statisticalResults.tex')
        template = r'''\documentclass[preview]{{standalone}}
                    \usepackage{{booktabs}}
                    \begin{{document}}
                    \begin{{tabular}}{{|c|c|c|}}
                    {}
                    \end{{tabular}}
                    \end{{document}}
                    '''
        with open(filename, 'wb') as f:
          f.write(template.format(statisticDftex.to_latex(escape=False)))
        subprocess.call(['pdflatex','-output-directory='+str(mediafolder),filename])
      	
      	txtfilename = os.path.join(mediafolder,'statisticalResults.txt')
      	statisticDftxt.to_csv(txtfilename, header=statisticDftxt.columns.values, index=True, sep=' ', mode='a')