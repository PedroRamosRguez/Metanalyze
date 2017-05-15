import re,os
def sortFiles(fileList):
	print 'entre y esta es la lista recibida...'
	print fileList
	for i,name in enumerate(fileList):
		pattern = re.search('\d+$',os.path.splitext(name.name)[0])
		index = pattern.start()
		print 'esto es depues del index'
		sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
	print ' esto es lo que retorno...'
	
	return sortedByFilename
