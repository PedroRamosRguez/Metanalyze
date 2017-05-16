import pandas as pd
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

def sortAvgDictToDataframe(dic):
	sortedbyKeys = sorted(dic, key = lambda tup:tup[1],reverse=True)
	df = pd.DataFrame(sortedbyKeys)
	df.columns=['0','Average']
	df = df.drop('0', 1)
	return df
def sortMaxDictToDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: tup[1],reverse=True)
	df = pd.DataFrame(sortedbyKeys)
	df.columns = ['0','Max']
	df = df.drop('0', 1)
	return df


def sortMinDictToDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: tup[1],reverse=True)
	df = pd.DataFrame(sortedbyKeys)
	df.columns = ['0','Min']
	df = df.drop('0',1)
	return df
