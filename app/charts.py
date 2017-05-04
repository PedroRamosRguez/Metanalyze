from random import randint
from jchart import Chart
from jchart.config import Axes, DataSet, rgba

class BubbleChart(Chart):
    chart_type = 'bubble'
    responsive = True
    def get_datasets(self, **kwargs):
        data = [{
            'x': randint(1, 10),
            'y': randint(1, 25),
            'r': randint(1, 10), #esto es el radio del punto que se muestra 
        } for i in range(25)]

        return [DataSet(label="Algoritmo1",
                        data=data,
                        backgroundColor='#FF6384',
                        hoverBackgroundColor='#FF6384')]