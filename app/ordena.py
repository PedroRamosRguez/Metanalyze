import re,os
def ordena(fileList):
	print 'entre y esta es la lista recibida...'
	print fileList
	for i,name in enumerate(fileList):
		pattern = re.search('\d+',os.path.splitext(name.name)[0])
		index = pattern.start()
		print (int(os.path.splitext(name.name)[0][index:]))
		sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
	print ' esto es lo que retorno...'
	print sortedByFilename
	return sortedByFilename
