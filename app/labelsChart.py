def labels(datos):
    labelsChart = []
    for i,v in enumerate(datos):
         listValues = []
         for ii,vv in sorted(v.iteritems()):
            for iii,vvv in sorted(vv.iteritems()):
                listValues.append(str(iii))
                listValues.sort(key=int)
    labelsChart= listValues
    return labelsChart