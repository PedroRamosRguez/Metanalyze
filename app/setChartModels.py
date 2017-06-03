import createModels as cModels
def setChart(dictHvAlg):
	chartList =[]
	for k,v in sorted(dictHvAlg.iteritems()):
		algList = []
		for step,val in sorted(v.iteritems()):
			for i,value in enumerate(val):
				algList.append({'x':str(step),'y':str(value)})
		chartList.append(algList)
	return chartList

def setMinAvgMaxChart(dfMinAvgMax,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMinAvgMax):
		modeList.append(v.to_dict())
	cModels.modelMinAvgMaxCharts(idConfiguration,modeList)

def setMinChart(dfMin,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMin):
		modeList.append(v.to_dict())
	cModels.modelMinCharts(idConfiguration,modeList)

def setAvgChart(dfAvg,idConfiguration):
	modeList = []
	for i,v in enumerate(dfAvg):
		modeList.append(v.to_dict())
	cModels.modelAvgCharts(idConfiguration,modeList)

def setMaxChart(dfMax,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMax):
		modeList.append(v.to_dict())
	cModels.modelMaxCharts(idConfiguration,modeList)

def setStatisticalDfTex(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfTex(idConfiguration,modeList)

def setStatisticalDfTxt(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfTxt(idConfiguration,modeList)

def setStatisticalDfHtml(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfHtml(idConfiguration,modeList)