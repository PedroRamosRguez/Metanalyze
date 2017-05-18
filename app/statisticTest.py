import scipy.stats as stats
import numpy as np
def shapiro(nAlgorithms,hypervolumeList):
	print 'entre..'
	print type(nAlgorithms)
	shapiroWilk = []
	for i in range(nAlgorithms):
		print i
		algorithmList = np.array(hypervolumeList[i])
		shapiroTest= stats.shapiro(algorithmList)
		pvalue = shapiroTest[1]
		shapiroWilk.append(pvalue)
	return shapiroWilk

def kruskalWallisTest(nAlgorithms,hypervolumeList):
	#stats.kruskal(algoritmo1, algoritmo2)
	print 'entre a kruskalwallis'
	i =0
	j= 1
	kruskal = []
	algorithmList= np.array(hypervolumeList[i])
	while j < nAlgorithms:
		algorithmCompare = np.array(hypervolumeList[j])
		kruskalTest = stats.kruskal(algorithmList, algorithmCompare)
		pvalue = kruskalTest[1]
		kruskal.append(pvalue)
		j +=1
	print kruskal
	return kruskal