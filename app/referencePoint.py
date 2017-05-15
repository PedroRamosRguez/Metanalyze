def referencePointInit(nAlgorithms,nObjectives):
	counter = 0
  	referencePoint = []
  	while counter < nAlgorithms:
		iReferencePoint = []
		for i in range(nObjectives):
			iReferencePoint.append(0)
		referencePoint.append(iReferencePoint)
		counter +=1
	return referencePoint

def referencePointCalculation(dicAlg,referencePoint):
	counter = 0
	coordinate = 0
	for k,v in sorted(dicAlg.iteritems()):
		for kk,vv in sorted(v.iteritems()):
			for kkk,vvv in sorted(vv.iteritems()):
				for x,val in enumerate(vvv):
					counter = 0
					coordinate = 0
					while counter < len(val):
						print referencePoint[int(k)]
						if val[counter] > referencePoint[int(k)][counter]:
							coordinate +=1
						counter +=1
					if coordinate == counter:
						referencePoint[int(k)] = val
	return referencePoint
