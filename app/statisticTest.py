#retornar el estadistico y la comparacion se realiza con el estadistico si es mayor el de uno que el de otro 
#si el estadistico es mayor de un algoritmo con respecto a otro significa que ese algoritmo tiene mejor rendimiento
#y el pvalue debe ser < a 0.05 si no son iguales

import scipy.stats as stats
import numpy as np
def all_same(items):
	return all(x == items[0] for x in items)
def pvalueMinor(items):
			return all(x <0.05 for x in items)
def pvalueMajor(items):
	return all(x >=0.05 for x in items)

def shapiroWilkTest(nAlgorithms,hypervolumeList):
	shapiroWilk = []
	#print len(hypervolumeList)
	for i in range(nAlgorithms):
		#print i
		algorithmList = np.array(hypervolumeList[i])
		shapiroTest= stats.shapiro(algorithmList)
		#print shapiroTest
		shapiroWilk.append(shapiroTest)
	return shapiroWilk

def kruskalWallisTest(nAlgorithms,hypervolumeList):
	#stats.kruskal(algoritmo1, algoritmo2)
	print 'entre a kruskalwallis'
	i =0
	j= 1
	kruskal = []
	algorithm = np.array(hypervolumeList[i])
	print 'antes del while'
	while j < int(nAlgorithms):
		
		algorithmCompare = np.array(hypervolumeList[j])
		kruskalTest = stats.kruskal(algorithm, algorithmCompare)
		kruskal.append(kruskalTest)
		print kruskal
		j +=1
	return kruskal

def leveneTest(nAlgorithms,hypervolumeList):
	#stats.levene(algoritmo1,algoritmo2)
	print 'entre a levene test'
	i =0
	j= 1
	levene = []
	algorithm = np.array(hypervolumeList[i])
	while j < nAlgorithms:
		algorithmCompare = np.array(hypervolumeList[j])
		lvnTest = stats.levene(algorithm, algorithmCompare)
		levene.append(lvnTest)
		j +=1
	return levene

def anovaTest(nAlgorithms,hypervolumeList):
	print 'entre a anova...'
	#stats.f_oneway(algoritmo1,algoritmo2)
	i =0
	j= 1
	anova = []
	while j < nAlgorithms:
		algorithmCompare = np.array(hypervolumeList[j])
		anvaTest = stats.f_oneway(algorithmList[i], algorithmCompare)
		anova.append(anvaTest)
		j +=1
	return anova

def welchTest(nAlgorithms,hypervolumeList):
	#primero calcular las medias y varianzas...
	average =  []
	variance = []
	welch = []
	j=0
	k=1
	for i,value in enumerate(hypervolumeList):
		algorithm = np.array(hypervolumeList[i])
		average.append(algorithm.mean())
		variance.append(algorithm.var())
	equalAverage = all_same(average)
	if sameAverage == True :
		#misma media se hace el test de welch asi:
		#stats.ttest_ind(algoritmo1,algoritmo2)
		algorithm = np.array(hypervolumeList[j])
		while k < nAlgorithms:
			algorithmCompare = np.array(hypervolumeList[k])
			wlch = stats.ttest_ind(algorithm, algorithmCompare)
			welch.append(wlch)
			k +=1
	else:
		equalVariance = all_same(variance)
		if equalVariance == True:
			algorithm = np.array(hypervolumeList[j])
			while j < nAlgorithms:
				algorithmCompare = np.array(hypervolumeList[k])
				wlch = stats.ttest_ind(algorithm, algorithmCompare)
				welch.append(wlch)
				k +=1	
		else:
			algorithm = np.array(hypervolumeList[j])
			while k < nAlgorithms:
				algorithmCompare = np.array(hypervolumeList[k])
				wlch = stats.ttest_ind(algorithm, algorithmCompare,equal_var = False)
				welch.append(wlch)
				j +=1
	return welch


