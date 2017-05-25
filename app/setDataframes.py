import pandas as pd
import sys
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
