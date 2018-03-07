def labels(datos):
    labelsChart = []
    for i,v in enumerate(datos):
         listValues = []
         for algorithm,values in sorted(v.iteritems()):
            for step,stepvalues in sorted(values.iteritems()):
                listValues.append(str(step))
                listValues.sort(key=int)
    labelsChart= listValues
    return labelsChart