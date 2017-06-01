def dataset(data):
	data_scatter = []
	for i,v in enumerate(data):
		listValues = []
		for ii,vv in sorted(v.iteritems()):
			for iii,vvv in sorted(vv.iteritems()):
				listValues.append({'x':str(iii),'y':str(vvv)})
				listValues.sort(key=lambda x:(int(x['x'])))
		data_scatter.append(listValues)
	return data_scatter

def datasetMinAvgMax(data):
	dataList=[]
	for i,v in enumerate(data):
		listValues = []
		for ii,vv in sorted(v.iteritems()):
			listBound = []
			for iii,vvv in sorted(vv.iteritems()):
				listBound.append({'x':str(iii),'y':str(vvv)})
				listBound.sort(key=lambda x:(int(x['x'])))
			listValues.append(listBound)
		dataList.append(listValues)
	#print dataList
	return dataList
