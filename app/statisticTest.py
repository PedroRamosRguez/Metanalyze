import scipy.stats as stats
import numpy as np
def all_same(items):
	return all(x == items[0] for x in items)

def pvalueMinor(items):
	return all(x <0.05 for x in items)

def pvalueMajor(items):
	print 'estoy en pvaluemajor'
	return all(x[1] >=0.05 for x in items)

def calculeMean(hyperVolumeList):
	meanAlgorithms = []
	for i,v in enumerate(hyperVolumeList):
		npAlgorithm = np.array(v)
		#print npAlgorithm
		meanAlgorithms.append(npAlgorithm.mean())
	return meanAlgorithms

def calculeVariance(hyperVolumeList):
	varianceAlgorithms = []
	for i,v in enumerate(hyperVolumeList):
		npAlgorithm = np.array(v)
		#print npAlgorithm
		varianceAlgorithms.append(npAlgorithm.var())
	return varianceAlgorithms

def calculeMedian(hyperVolumeList):
	medianAlgorithms = []
	for i,v in enumerate(hyperVolumeList):
		npAlgorithm = np.array(v)
		#print npAlgorithm
		medianAlgorithms.append(np.median(npAlgorithm))
	return medianAlgorithms
		
def shapiroWilkTest(nAlgorithms,hyperVolumeList):
	shapiroWilk = []
	#print len(hyperVolumeList)
	for i in range(nAlgorithms):
		#print i
		algorithmList = np.array(hyperVolumeList[i])
		shapiroTest= stats.shapiro(algorithmList)
		#print shapiroTest
		shapiroWilk.append(shapiroTest)
	return shapiroWilk

def kruskalWallisTest(nAlgorithms,hyperVolumeList):
	#stats.kruskal(algoritmo1, algoritmo2)
	print 'entre a kruskalwallis'
	
	kruskal = []
	for i in range(nAlgorithms):
		algorithm = np.array(hyperVolumeList[i])
		j =i+1
		while j < nAlgorithms:
			algorithmCompare = np.array(hyperVolumeList[j])
			kruskalTest = stats.kruskal(algorithm, algorithmCompare)
			kruskal.append(kruskalTest)
			print kruskal
			j +=1
	return kruskal

def leveneTest(nAlgorithms,hyperVolumeList):
	levene = []
	for i in range(nAlgorithms):
		algorithm = np.array(hyperVolumeList[i])
		j = i+1
		while j < nAlgorithms:
			algorithmCompare = np.array(hyperVolumeList[j])
			lvnTest = stats.levene(algorithm, algorithmCompare)
			levene.append(lvnTest)
			j +=1
	return levene

def anovaTest(nAlgorithms,hyperVolumeList):
	anova = []
	for i in range(nAlgorithms):
		algorithm = np.array(hyperVolumeList[i])
		j=i+1
		while j < nAlgorithms:
			algorithmCompare = np.array(hyperVolumeList[j])
			anvaTest = stats.f_oneway(algorithm, algorithmCompare)
			anova.append(anvaTest)
			j +=1
			print 'esto es anova'
			print anova
	return anova

def welchTest(nAlgorithms,hyperVolumeList):
	#primero calcular las medias y varianzas...
	mean =  calculeMean(hyperVolumeList)	#calcular medias
	variance = calculeVariance(hyperVolumeList)	#calcular varianzas
	welch = []
	equalAverage = all_same(mean)
	if sameAverage == True :
		for i,v in range(nAlgorithms):
			algorithm = np.array(hyperVolumeList[i])
			j =i+1
			while j < nAlgorithms:
				algorithmCompare = np.array(hyperVolumeList[j])
				welchTest = stats.ttest_ind(algorithm, algorithmCompare)
				welch.append(welchTest)
				j +=1
	else:
		equalVariance = all_same(variance)
		if equalVariance == True:
			for i,v in range(nAlgorithms):
				algorithm = np.array(hyperVolumeList[i])
				j =i+1
				while j < nAlgorithms:
					algorithmCompare = np.array(hyperVolumeList[j])
					welchTest = stats.ttest_ind(algorithm, algorithmCompare)
					welch.append(welchTest)
					j +=1
		else:
			for i,v in range(nAlgorithms):
				algorithm = np.array(hyperVolumeList[i])
				j =i+1
				while j < nAlgorithms:
					algorithmCompare = np.array(hyperVolumeList[j])
					welchTest = stats.ttest_ind(algorithm, algorithmCompare,equal_var =False)
					welch.append(welchTest)
					j +=1
	return welch


