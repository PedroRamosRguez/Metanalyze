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
class PolarChart(Chart):
    chart_type = 'polarArea'

    def get_labels(self, **kwargs):
        return ["Red", "Green", "Yellow", "Grey", "Blue"]

    def get_datasets(self, **kwargs):
        return [DataSet(label="My DataSet",
                        data=[11, 16, 7, 3, 14],
                        backgroundColor=[
                            "#FF6384",
                            "#4BC0C0",
                            "#FFCE56",
                            "#E7E9ED",
                            "#36A2EB"
                        ])
                ]