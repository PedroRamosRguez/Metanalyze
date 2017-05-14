def dataset(data):
	data_scatter = []
	for i,v in enumerate(data):
		listValues = []
		for ii,vv in sorted(v.iteritems()):
			#print ii
			#print vv
			for iii,vvv in sorted(vv.iteritems()):
				#print iii
				#print vvv
				listValues.append({'x':str(iii),'y':str(vvv)})
				listValues.sort(key=lambda x:(int(x['x'])))
		data_scatter.append(listValues)
	return data_scatter

def datasetMinAvgMax(data):
	dataList=[]
	for i,v in enumerate(data):
	    #print i
	    #print v
	    print v.keys()
        listValues = []
        for ii,vv in sorted(v.iteritems()):
            #print ii
            #print vv
            print 'esto es ii'
            print ii
            listBound = []
            for iii,vvv in sorted(vv.iteritems()):
                #print iii
                #print vvv
                listBound.append({'x':str(iii),'y':str(vvv)})
                listBound.sort(key=lambda x:(int(x['x'])))
            listValues.append(listBound)
        dataList.append(listValues)
	return dataList