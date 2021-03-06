from jchart import Chart
from jchart.config import DataSet,Axes,Legend
from .models import Configuration,Algorithms,ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
from labelsChart import labels
from dataSet import dataset,datasetMinAvgMax
import getColors as colors

def get_latests_config():
    try:
        return Configuration.objects.filter().latest('id')
    except Configuration.DoesNotExist:
        return {}

class MinChart(Chart):
    last_config = get_latests_config()
    evaluation = last_config.evaluation if last_config else 'Por determinar'
    chart_type = 'line'
    scales = {
        'yAxes': [{'scaleLabel':{'display':True,'labelString':'Hypervolume','fontSize':int(15)}}],
        'xAxes' : [{'scaleLabel':{'display':True,'labelString':evaluation,'fontSize':int(20)}}]
        
    }

    title = {
        'display': True,
        'text': 'Evolution of Minimum Hypervolume',
        'fontSize': 20,
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    

    def get_datasets(self,*args):
        last_config = get_latests_config()
        algorithm_names = []
        getAlgorithms = Algorithms.objects.filter(configuration__id=last_config.id).values().distinct()
        for i in range(int(last_config.nAlgorithms)):
            algorithm_names.append(getAlgorithms[i]['idAlgorithm'])
        dataModel = MinChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        chartReturned = []
        data_scatter = dataset(data)
        borderColor = []
        for i,v in enumerate(data_scatter):
            borderColor.append(colors.colors())

        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='Min '+str(algorithm_names[i]),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = MinChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart

class AvgChart(Chart):
    last_config = get_latests_config()
    evaluation = last_config.evaluation if last_config else 'Por determinar'
    chart_type = 'line'
    scales = {
        'yAxes': [{'scaleLabel':{'display':True,'labelString':'Hypervolume','fontSize':int(15)}}],
        'xAxes' : [{'scaleLabel':{'display':True,'labelString':evaluation,'fontSize':int(20)}}]
        
    }
    title = {
        'display': True,
        'text': 'Evolution of Average Hypervolume',
        'fontSize': 20,
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        last_config = get_latests_config()
        algorithm_names = []
        getAlgorithms = Algorithms.objects.filter(configuration__id=last_config.id).values().distinct()
        for i in range(int(last_config.nAlgorithms)):
            algorithm_names.append(getAlgorithms[i]['idAlgorithm'])
        dataModel = AvgChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        data_scatter = dataset(data)
        chartReturned = []

        borderColor = []
        for i,v in enumerate(data_scatter):
            borderColor.append(colors.colors())
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='Avg '+str(algorithm_names[i]),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = AvgChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart

class MaxChart(Chart):
    last_config = get_latests_config()
    evaluation = last_config.evaluation if last_config else 'Por determinar'
    chart_type = 'line'
    scales = {
        'yAxes': [{'scaleLabel':{'display':True,'labelString':'Hypervolume','fontSize':int(15)}}],
        'xAxes' : [{'scaleLabel':{'display':True,'labelString':evaluation,'fontSize':int(20)}}]
        
    }
    title = {
        'display': True,
        'text': 'Evolution of Maximum Hypervolume',
        'fontSize': 20
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        last_config = get_latests_config()
        algorithm_names = []
        getAlgorithms = Algorithms.objects.filter(configuration__id=last_config.id).values().distinct()
        for i in range(int(last_config.nAlgorithms)):
            algorithm_names.append(getAlgorithms[i]['idAlgorithm'])
        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        data_scatter = dataset(data)
        chartReturned = []
        borderColor = []
        for i,v in enumerate(data_scatter):
            borderColor.append(colors.colors())
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='Max '+str(algorithm_names[i]),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart 

class MinAvgMaxChart(Chart):
    last_config = get_latests_config()
    evaluation = last_config.evaluation if last_config else 'Por determinar'
    chart_type = 'line'
    scales = {
        'yAxes': [{'scaleLabel':{'display':True,'labelString':'Hypervolume','fontSize':int(15)}}],
        'xAxes' : [{'scaleLabel':{'display':True,'labelString':evaluation,'fontSize':int(20)}}]
        
    }
    title = {
        'display': True,
        'text': 'Evolution of Hypervolume',
        'fontSize': 20
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        
        last_config = get_latests_config()
        algorithm_names = []
        getAlgorithms = Algorithms.objects.filter(configuration__id=last_config.id).values().distinct()
        for i in range(int(last_config.nAlgorithms)):
            algorithm_names.append(getAlgorithms[i]['idAlgorithm'])
        dataModel = MinAvgMaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        
        chartLabels = data[0].keys()
        chartLabels.sort()
        
        dataList=datasetMinAvgMax(data)
        chartReturned = []
        selectColor = 0
        borderColor = []
        numberColors = int(len(dataList)*3)
        for i in range(numberColors):
            borderColor.append(colors.colors())
        for i,v in enumerate(dataList):
            #print len(v)
            for ii,vv in enumerate(v):
                
                chartReturned.append(DataSet(type='line',label=str(chartLabels[ii])+' '+str(algorithm_names[i]),showLine=True,data=vv, 
                borderColor=borderColor[selectColor],fill=False))#,backgroundColor=backgroundColor[selectColor]))
                selectColor +=1
        return chartReturned
    def get_labels(self,*args, **kwargs):

        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        
        labelsChart=labels(data)
        return labelsChart 
