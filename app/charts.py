from jchart import Chart
from jchart.config import Axes, DataSet, rgba,ScaleLabel,Tick,Title
from .models import ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
from labelsChart import labels
from dataSet import dataset,datasetMinAvgMax
class MinChart(Chart):
    chart_type = 'line'
    axes = {
        'id': 'pruebaid'
    }
    title = {
        'display': True,
        'text': 'Chart of Minimum Bounds',
        'fontSize': 20,
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    
    def get_datasets(self,*args):
        dataModel = MinChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        chartReturned = []
        data_scatter = dataset(data)
        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)']
        '''backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ]'''
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='MinAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = MinChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart

class AvgChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of Average bounds',
        'fontSize': 20,
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        dataModel = AvgChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        data_scatter = dataset(data)
        chartReturned = []

        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)']
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='AvgAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = AvgChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart

class MaxChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of Max bounds',
        'fontSize': 20
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        data_scatter = dataset(data)
        chartReturned = []

        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)']
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='MaxAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],fill=False))#,backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart 

class MinAvgMaxChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of MinAvgMax bounds',
        'fontSize': 20
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
    
    def get_datasets(self,*args):
        print 'estoy en getdatasets...'
        dataModel = MinAvgMaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        #print 'esto es la lista de valores del minavgmaxchartmodel'
        #print data
        #print len(data)
        #data_scatter = dataset(data)
        chartLabels = data[0].keys()
        chartLabels.sort()
        #print 'esto es charlabels:'
        #print chartLabels
        dataList=datasetMinAvgMax(data)
        data_scatter = []
        chartReturned = []
        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(128,0,0,1)',
                'rgba(0,0,128,1)',
                'rgba(47,79,79,1)',
                'rgba(75,0,130,1)',
                'rgba(124,252,0,1)',
                'rgba(0,139,139,1)'
                ]
        selectColor = 0
        print 'esto es data list antes del ultimos for..'
        for i,v in enumerate(dataList):
            #print len(v)
            for ii,vv in enumerate(v):
                #print 'este es el ultimo for..'
                #print vv
                #print len(vv)
                #print chartLabels[ii]
                chartReturned.append(DataSet(type='line',label=str(chartLabels[ii])+'Algorithm'+str(i+1),showLine=True,data=vv, 
                borderColor=borderColor[selectColor],fill=False))#,backgroundColor=backgroundColor[selectColor]))
                selectColor +=1
        return chartReturned
    def get_labels(self,*args, **kwargs):

        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        
        labelsChart=labels(data)
        return labelsChart 