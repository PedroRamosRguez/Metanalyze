from .models import Algorithms,Configuration,ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
#metodo que crea el modelo de la configuracion de los algoritmos
def modelConfiguration(form,request):
	#PONER LA CREACION DEL MODELO DE CONFIGURACION EN UN METODO
	print 'esto es request.post test'
	print (request.POST['test'])
	config = Configuration.objects.create()
	config.nAlgorithms = form.cleaned_data['nAlgorithms']
	config.nObjectives = form.cleaned_data['nObjectives']
	config.nExecutions = form.cleaned_data['nExecutions']
	config.step = form.cleaned_data['step']
	config.stopCondition = form.cleaned_data['stopCondition']
	config.dataOutput = form.cleaned_data['dataOutput']
	config.bound = request.POST['bound']
	config.test = request.POST['test']
	config.metric = request.POST['metric']
	config.save()
	return config.id
#metodo que crea el modelo para cada algoritmo introducido
def modelAlgorithm(item,fileName,idConfiguration):
	algorithmModel = Algorithms.objects.create(configuration_id=idConfiguration)
	algorithmModel.algorithm = item['algorithmName']
	algorithmModel.idAlgorithm = item['id']
	algorithmModel.fileName = fileName
	algorithmModel.nVariablesAlgorithm = item['nVariables']
	algorithmModel.save()

def modelCharts(idConfiguration,listValues):
	chartModel = ChartsModel.objects.create(configuration_id=idConfiguration)
	chartModel.listValues = listValues
	chartModel.save()

def modelMinAvgMaxCharts(idConfiguration,listValues):
	minAvgMaxChartModel = MinAvgMaxChartModel.objects.create(configuration_id=idConfiguration)
	minAvgMaxChartModel.listValues = listValues
	minAvgMaxChartModel.save()

def modelMinCharts(idConfiguration,listValues):
	minChartModel = MinChartModel.objects.create(configuration_id=idConfiguration)
	minChartModel.listValues = listValues
	minChartModel.save()

def modelAvgCharts(idConfiguration,listValues):
	avgChartModel = AvgChartModel.objects.create(configuration_id=idConfiguration)
	avgChartModel.listValues = listValues
	avgChartModel.save()

def modelMaxCharts(idConfiguration,listValues):
	maxChartModel = MaxChartModel.objects.create(configuration_id=idConfiguration)
	maxChartModel.listValues = listValues
	maxChartModel.save()


