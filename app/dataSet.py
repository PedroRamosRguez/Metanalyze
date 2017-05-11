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
		data_scatter.append(listValues)
	return data_scatter