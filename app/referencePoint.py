import sys
def referencePointInit(nAlgorithms,nObjectives):
	counter = 0
  	referencePoint = []
	for i in range(nObjectives):
		referencePoint.append(0)
	return referencePoint

def referencePointCalculation(dicAlg,referencePoint):
	for k,v in sorted(dicAlg.iteritems()):
		for kk,vv in sorted(v.iteritems()):
			for kkk,vvv in sorted(vv.iteritems()):
				for x,value in enumerate(vvv):
					maxX = float(value[0])
					maxY = float(value[1])
					if maxX > referencePoint[0]:
						referencePoint[0] = maxX
					if maxY > referencePoint[1]:
						referencePoint[1] = maxY
				
	 #referencePoint = val
	return referencePoint
