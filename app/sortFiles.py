import re,os
def sortFiles(fileList):
	for i,name in enumerate(fileList):
		pattern = re.search('\d+$',os.path.splitext(name.name)[0])
		index = pattern.start()
		sortedByFilename = sorted(fileList,key=lambda name:int(os.path.splitext(name.name)[0][index:]))
	return sortedByFilename
