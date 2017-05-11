from jchart import Chart
from jchart.config import Axes, DataSet, rgba,ScaleLabel,Tick,Title
from .models import ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
from labelsChart import labels
from dataSet import dataset
class MinChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of Minimum Bounds'
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
            chartReturned.append(DataSet(type='line',label='MinAlgorithm'+str(i+1),showLine=False,data=v, 
                borderColor=borderColor[i]))#,backgroundColor=backgroundColor[i]))
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
        'text': 'Chart of Average bounds'
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
        '''backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ]'''
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='AvgAlgorithm'+str(i+1),showLine=False,data=v, 
                borderColor=borderColor[i]))#,backgroundColor=backgroundColor[i]))
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
        'text': 'Chart of Max bounds'
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
        '''backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ]'''
        print 'esto es data_scatter'
        print data_scatter
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='MaxAlgorithm'+str(i+1),showLine=False,data=v, 
                borderColor=borderColor[i]))#,backgroundColor=backgroundColor[i]))
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
        'text': 'Chart of MinAvgMax bounds'
    }
    responsive = True
    
    def get_datasets(self,*args):
        print 'estoy en getdatasets...'
        dataModel = MinAvgMaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        print data
        dataList=[]
        #data_scatter = dataset(data)
        chartLabels = data[0].keys()
        for i,v in enumerate(data):
            #print i
            #print v
            print v.keys()
            listValues = []
            for ii,vv in sorted(v.iteritems()):
                #print ii
                #print vv
                listBound = []
                for iii,vvv in sorted(vv.iteritems()):
                    #print iii
                    #print vvv
                    listBound.append({'x':str(iii),'y':str(vvv)})
                listValues.append(listBound)
            dataList.append(listValues)
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
        '''backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(218,165,32,0.2)',
                'rgba(255,127,80,0.2)',
                'rgba(30,144,255,0.2)',
                'rgba(47,79,79,0.2)',
                'rgba(0,100,0,0.2)',
                'rgba(220,20,60,0.2)'
            ]'''
        selectColor = 0
        for i,v in enumerate(dataList):
            print len(v)
            for ii,vv in enumerate(v):
                print vv
                chartReturned.append(DataSet(type='line',label=str(chartLabels[ii])+'Algorithm'+str(i+1),showLine=False,data=vv, 
                borderColor=borderColor[selectColor]))#,backgroundColor=backgroundColor[selectColor]))
                selectColor +=1
        #print chartReturned
        

        
        '''print data_scatter
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='MaxAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],backgroundColor=backgroundColor[i]))'''
        #return chartReturned
        return chartReturned
    def get_labels(self,*args, **kwargs):

        dataModel = MaxChartModel.objects.filter().latest('id')
        data = dataModel.listValues
        labelsChart=labels(data)
        return labelsChart 