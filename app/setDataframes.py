import pandas as pd
import sympy
from collections import OrderedDict
def mainDataFrame(dictHvAlg):
	df = []
	for k,v in sorted(dictHvAlg.iteritems()):
		df.append(pd.DataFrame(v))
  	return df

def minAvgMaxDataFrame(df):
	dfMinAvgMax = []
	for i,v in enumerate(df):
		dfMinAvgMax.append(pd.DataFrame(v.min(),columns=['Min']))
		dfMinAvgMax[i]['Average']=v.mean()
		dfMinAvgMax[i]['Max'] = v.max()
	return dfMinAvgMax

def minDataFrame(df):
	dfMin = []
	for i,v in enumerate(df):
		dfMin.append(pd.DataFrame(v.min(),columns=['Min']))
	return dfMin

def avgDataFrame(df):
	dfAvg = []
	for i,v in enumerate(df):
		dfAvg.append(pd.DataFrame(v.mean(),columns=['Avg']))
	return dfAvg

def maxDataFrame(df):
	dfMax = []
	for i,v in enumerate(df):
		dfMax.append(pd.DataFrame(v.max(),columns=['Max']))
	return dfMax

def sortAvgDataframe(dic):
	sortedbyKeys = sorted(dic, key = lambda tup:int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns=['Step','Average']
	return df
def sortMaxDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns = ['Step','Max']	
	return df


def sortMinDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns = ['Step','Min']
	return df
#crea el dataframe de resultados estadisticos para ficheros latex
def statisticDataframetex(algorithm_names,value,meanAlgorithms,medianAlgorithms):
	statisticDftex = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
	for i,v in enumerate(value):
  		j=i+1
  		statisticDftex.set_value(algorithm_names[i],algorithm_names[i],'$\leftrightarrow$')
  		statisticDftex.set_value(algorithm_names[j],algorithm_names[j],'$\leftrightarrow$')
  		if(v[1] < 0.05):
  			#statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
  			if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
  				#caso especial se inserta un asterisco
  				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
  				statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'*')
  			elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
  				#caso especial se inserta un asterisco
  				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
  				statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'*')
  			elif medianAlgorithms[i] < medianAlgorithms[j]:
  				#algoritmo1 mejor que algoritmo2
  				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\uparrow$')
  				statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\downarrow$')
  			elif medianAlgorithms[i] > medianAlgorithms[j]:
  				#algoritmo1 peor que algoritmo2
  				statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\downarrow$')
  				statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\uparrow$')
  		else:
  			#no existen diferencias
  			statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\leftrightarrow$')
  			statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\leftrightarrow$')
  	return statisticDftex

#crea el dataframe de resultados estadisticos para ficheros txt
def statisticDataframetxt(algorithm_names,value,meanAlgorithms,medianAlgorithms):
	statisticDftxt = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
	for i,v in enumerate(value):
  		j=i+1
  		statisticDftxt.set_value(algorithm_names[i],algorithm_names[i],'=')
  		statisticDftxt.set_value(algorithm_names[j],algorithm_names[j],'=')
  		if(v[1] < 0.05):
  			#statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
  			if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
  				#caso especial se inserta un asterisco
  				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
  				statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'*')
  			elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
  				#caso especial se inserta un asterisco
  				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
  				statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'*')
  			elif medianAlgorithms[i] < medianAlgorithms[j]:
  				#algoritmo1 mejor que algoritmo2
  				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'+')
  				statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'-')
  			elif medianAlgorithms[i] > medianAlgorithms[j]:
  				#algoritmo1 peor que algoritmo2
  				statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'-')
  				statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'+')
  		else:
  			#no existen diferencias
  			statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'=')
  			statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'=')
  	return statisticDftxt

def statisticDataframeHtml(algorithm_names,value,meanAlgorithms,medianAlgorithms):
  statisticDfhtml = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
  for i,v in enumerate(value):
      j=i+1
      statisticDfhtml.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
      statisticDfhtml.set_value(algorithm_names[j],algorithm_names[j],u'\u2194')
      if(v[1] < 0.05):
        if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif medianAlgorithms[i] < medianAlgorithms[j]:
          #algoritmo1 mejor que algoritmo2
          statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2191')
          statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2193')
        elif medianAlgorithms[i] > medianAlgorithms[j]:
          #algoritmo1 peor que algoritmo2
          statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2193')
          statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2191')
      else:
        #no existen diferencias
        statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2194')
        statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2194')
  return statisticDfhtml