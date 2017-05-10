from jchart import Chart
from jchart.config import Axes, DataSet, rgba,ScaleLabel,Tick,Title
from .models import ChartsModel,MinAvgMaxChartModel,MinChartModel,AvgChartModel,MaxChartModel
class MinChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of Minimum Bounds'
    }
    responsive = True
    
    def get_datasets(self,*args):
        print 'estoy en getdatasets...'
        dataModel = MinChartModel.objects.filter().latest('id')
        datos = dataModel.listValues
        data_scatter = []
        chartReturned = []
        for i,v in enumerate(datos):
            print 'esto es el for..'
            print i
            print v
            print v.keys()
            listValues = []
            for ii,vv in sorted(v.iteritems()):
                print ii,
                print vv
                for iii,vvv in sorted(vv.iteritems()):
                    print iii
                    print vvv
                    listValues.append({'x':str(iii),'y':str(vvv)})
            data_scatter.append(listValues)

        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)']
        backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ]
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='MinAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        pruebaImportacionDatos = MinChartModel.objects.filter().latest('id')
        datos = pruebaImportacionDatos.listValues
        labelsChart = []
        for i,v in enumerate(datos):
             print 'esto es el for..'
             print i
             print v
             print v.keys()
             listValues = []
             for ii,vv in sorted(v.iteritems()):
                print ii,
                print vv
                for iii,vvv in sorted(vv.iteritems()):
                    print iii
                    print vvv
                    listValues.append(str(iii))
        labelsChart= listValues
        print 'labelschart:'
        print labelsChart
        return labelsChart

'''class AvgChart(Chart):
    chart_type = 'line'
    title = {
        'display': True,
        'text': 'Chart of Average bounds'
    }
    responsive = True
    
    def get_datasets(self,*args):
        print 'estoy en getdatasets...'
        dataModel = AvgChartModel.objects.filter().latest('id')
        datos = dataModel.listValues
        data_scatter = []
        chartReturned = []
        for i,v in enumerate(datos):
            print 'esto es el for..'
            print i
            print v
            print v.keys()
            listValues = []
            for ii,vv in sorted(v.iteritems()):
                print ii,
                print vv
                for iii,vvv in sorted(vv.iteritems()):
                    print iii
                    print vvv
                    listValues.append({'x':str(iii),'y':str(vvv)})
            data_scatter.append(listValues)

        borderColor = ['rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)']
        backgroundColor = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ]
        for i,v in enumerate(data_scatter):
            chartReturned.append(DataSet(type='line',label='AvgAlgorithm'+str(i+1),showLine=True,data=v, 
                borderColor=borderColor[i],backgroundColor=backgroundColor[i]))
        return chartReturned

    def get_labels(self,*args, **kwargs):

        pruebaImportacionDatos = MinChartModel.objects.filter().latest('id')
        datos = pruebaImportacionDatos.listValues
        labelsChart = []
        for i,v in enumerate(datos):
             print 'esto es el for..'
             print i
             print v
             print v.keys()
             listValues = []
             for ii,vv in sorted(v.iteritems()):
                print ii,
                print vv
                for iii,vvv in sorted(vv.iteritems()):
                    print iii
                    print vvv
                    listValues.append(str(iii))
        labelsChart= listValues
        print 'labelschart:'
        print labelsChart
        return labelsChart'''
#este seria el valido...
class TimeSeriesChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Tick(autoSkip=False,autoSkipPadding=True,minRotation=1,maxRotation=5,display=True),Axes(display=False)],
    }
    def get_labels(self, **kwargs):
        return ['1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
         '', '', '', '', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '5', '', '', '', '', '', '', '', '', '', '', '', '', '',
           '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    def get_datasets(self, **kwargs):
        data = [{'y': '0.419112354436', 'x': '1'}, {'y': '0.410862321301', 'x': '1'}, {'y': '0.586926288722', 'x': '1'}, {'y': '0.720418658759', 'x': '1'}, {'y': '0.694849043641', 'x': '1'}, {'y': '0.77533173491', 'x': '1'}, {'y': '0.641951350404', 'x': '1'}, {'y': '0.612305572985', 'x': '1'}, {'y': '0.75032296346', 'x': '1'}, {'y': '0.128812735865', 'x': '1'}, {'y': '0.597809325714', 'x': '1'}, {'y': '0.476768893935', 'x': '1'}, {'y': '0.643304696824', 'x': '1'}, {'y': '0.525775772378', 'x': '1'}, {'y': '0.489434932678', 'x': '1'}, {'y': '0.691221168609', 'x': '1'}, {'y': '0.81576909717', 'x': '1'}, {'y': '0.619424461838', 'x': '1'}, {'y': '0.456995514614', 'x': '1'}, {'y': '0.735386977337', 'x': '1'}, {'y': '0.278942772289', 'x': '1'}, {'y': '0.577454938812', 'x': '1'}, {'y': '0.738984300711', 'x': '1'}, {'y': '0.503889151478', 'x': '1'}, {'y': '0.187055518962', 'x': '1'}, {'y': '0.637362000525', 'x': '1'}, {'y': '0.670935324358', 'x': '1'}, {'y': '0.655918006467', 'x': '1'}, {'y': '0.537663931985', 'x': '1'}, {'y': '0.795638373601', 'x': '1'}, {'y': '0.297787925371', 'x': '2'}, {'y': '0.739821997319', 'x': '2'}, {'y': '0.630916320969', 'x': '2'}, {'y': '0.695943112977', 'x': '2'}, {'y': '0.54833206289', 'x': '2'}, {'y': '0.527112307303', 'x': '2'}, {'y': '0.598575966305', 'x': '2'}, {'y': '0.415076482732', 'x': '2'}, {'y': '0.429344603698', 'x': '2'}, {'y': '0.462768264542', 'x': '2'}, {'y': '0.222737208258', 'x': '2'}, {'y': '0.378098673857', 'x': '2'}, {'y': '0.777866309806', 'x': '2'}, {'y': '0.507666944556', 'x': '2'}, {'y': '0.618761241293', 'x': '2'}, {'y': '0.791914665625', 'x': '2'}, {'y': '0.644086342661', 'x': '2'}, {'y': '0.599990118963', 'x': '2'}, {'y': '0.607400516633', 'x': '2'}, {'y': '0.596390169564', 'x': '2'}, {'y': '0.335042159165', 'x': '2'}, {'y': '0.5527299713', 'x': '2'}, {'y': '0.541329983223', 'x': '2'}, {'y': '0.694421583573', 'x': '2'}, {'y': '0.576994947301', 'x': '2'}, {'y': '0.766458122308', 'x': '2'}, {'y': '0.859925310536', 'x': '2'}, {'y': '0.778558584801', 'x': '2'}, {'y': '0.790677888786', 'x': '2'}, {'y': '0.475986823025', 'x': '2'}, {'y': '0.568233502219', 'x': '3'}, {'y': '0.379604334852', 'x': '3'}, {'y': '0.275227574772', 'x': '3'}, {'y': '0.450445696649', 'x': '3'}, {'y': '0.364634042067', 'x': '3'}, {'y': '0.551006416172', 'x': '3'}, {'y': '0.597782421396', 'x': '3'}, {'y': '0.580141464108', 'x': '3'}, {'y': '0.429592054001', 'x': '3'}, {'y': '0.68188372324', 'x': '3'}, {'y': '0.658471858969', 'x': '3'}, {'y': '0.346495437537', 'x': '3'}, {'y': '0.653359703074', 'x': '3'}, {'y': '0.296745504985', 'x': '3'}, {'y': '0.655717814474', 'x': '3'}, {'y': '0.684413383019', 'x': '3'}, {'y': '0.226629631106', 'x': '3'}, {'y': '0.587358420257', 'x': '3'}, {'y': '0.236148093012', 'x': '3'}, {'y': '0.20958498176', 'x': '3'}, {'y': '0.608677985952', 'x': '3'}, {'y': '0.335481893649', 'x': '3'}, {'y': '0.688083958329', 'x': '3'}, {'y': '0.530227129129', 'x': '3'}, {'y': '0.65030064029', 'x': '3'}, {'y': '0.414733824475', 'x': '3'}, {'y': '0.867124091105', 'x': '3'}, {'y': '0.67019468721', 'x': '3'}, {'y': '0.878714436491', 'x': '3'}, {'y': '0.571513675665', 'x': '3'}, {'y': '0.539940386774', 'x': '4'}, {'y': '0.196030261675', 'x': '4'}, {'y': '0.848719025501', 'x': '4'}, {'y': '0.509088194373', 'x': '4'}, {'y': '0.771129683472', 'x': '4'}, {'y': '0.743055635369', 'x': '4'}, {'y': '0.765886621477', 'x': '4'}, {'y': '0.839944235571', 'x': '4'}, {'y': '0.556502837457', 'x': '4'}, {'y': '0.328160316353', 'x': '4'}, {'y': '0.605009860338', 'x': '4'}, {'y': '0.53931787129', 'x': '4'}, {'y': '0.788560423502', 'x': '4'}, {'y': '0.0813292582893', 'x': '4'}, {'y': '0.437646454385', 'x': '4'}, {'y': '0.532520084251', 'x': '4'}, {'y': '0.250804428711', 'x': '4'}, {'y': '0.709906471701', 'x': '4'}, {'y': '0.693644175756', 'x': '4'}, {'y': '0.47627353281', 'x': '4'}, {'y': '0.839094495008', 'x': '4'}, {'y': '0.559571550526', 'x': '4'}, {'y': '0.418002382163', 'x': '4'}, {'y': '0.463794411639', 'x': '4'}, {'y': '0.307623835325', 'x': '4'}, {'y': '0.792231135877', 'x': '4'}, {'y': '0.664649757432', 'x': '4'}, {'y': '0.546825611789', 'x': '4'}, {'y': '0.888420280559', 'x': '4'}, {'y': '0.33646471804', 'x': '4'}, {'y': '0.827699574064', 'x': '5'}, {'y': '0.72052913811', 'x': '5'}, {'y': '0.548157877649', 'x': '5'}, {'y': '0.553398047241', 'x': '5'}, {'y': '0.679137239955', 'x': '5'}, {'y': '0.336932549662', 'x': '5'}, {'y': '0.648140918649', 'x': '5'}, {'y': '0.487274840953', 'x': '5'}, {'y': '0.789837657705', 'x': '5'}, {'y': '0.55792894757', 'x': '5'}, {'y': '0.543567328503', 'x': '5'}, {'y': '0.576617717121', 'x': '5'}, {'y': '0.384978752808', 'x': '5'}, {'y': '0.411212261678', 'x': '5'}, {'y': '0.203821415368', 'x': '5'}, {'y': '0.90160215176', 'x': '5'}, {'y': '0.712783586377', 'x': '5'}, {'y': '0.424580306325', 'x': '5'}, {'y': '0.406756480252', 'x': '5'}, {'y': '0.600962439629', 'x': '5'}, {'y': '0.505984181739', 'x': '5'}, {'y': '0.872600276555', 'x': '5'}, {'y': '0.295205720802', 'x': '5'}, {'y': '0.889412182455', 'x': '5'}, {'y': '0.43480519152', 'x': '5'}, {'y': '0.641185890655', 'x': '5'}, {'y': '0.836646738029', 'x': '5'}, {'y': '0.596188092811', 'x': '5'}, {'y': '0.554051249768', 'x': '5'}, {'y': '0.746165062323', 'x': '5'}]
        getChart = ChartsModel.objects.filter().latest('id')
        dataset = []
        for i,v in enumerate(getChart.listValues):
            for ii,vv in enumerate(v):
                dataset.append(vv)
        data2 = getChart.listValues[0]
        return [
            DataSet(type='line',
                    label='Algoritmo1',
                    showLine=True,
                    data=data),
            DataSet(type='line',
                    label='Algoritmo2',
                    borderColor='red',
                    data=dataset),
            DataSet(type='line',
                    label='Algoritmo3',
                    borderColor='blue',
                    data=dataset),
        ]