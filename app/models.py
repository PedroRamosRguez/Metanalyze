from django.db import models
import ast
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
# Create your models here.
class Configuration(models.Model):
  nAlgorithms = models.CharField(max_length = 100) #Numero de algoritmos
  #test =  ListField()#models.CharField(max_length = 100)        #Almacena los tests estadisticos que se realizaran
  nObjectives = models.CharField(max_length = 100)  #Numero de objetivos que se utiliza para el analisis del algoritmo
  nExecutions = models.CharField(max_length = 100) #Numero de ejecuciones realizadas para las pruebas del algoritmo
  step = models.CharField(max_length = 100)        #Numero del paso del analisis del algoritmo. Ej; cada 200
  stopCondition = models.CharField(max_length = 100) #Condicion de parada para el analisis del algoritmo
  dataOutput = models.CharField(max_length = 100)   #Formato de salida de datos despues de realizar el analisis(grafico,tabla o ambas)
  bound =  ListField()#models.CharField(max_length = 100)        #Guardara la opcion de calcular en la metrica: minimo, media o maximo
  metric =  ListField()#models.CharField(max_length = 100)       # Guarda la metrica o metricas que se analizaran
  statisticTest = models.CharField(max_length = 2)
  evaluation = models.CharField(max_length = 100)     #guarda el titulo del ejex del grafico
# Mirar el paquete jsonfield para la insercion de valores en el modelo tipo json
class Algorithms(models.Model):
  
  algorithm = models.CharField(max_length = 100)   #Nombre del algoritmo
  idAlgorithm = models.CharField(max_length = 100) #Guarda el identificador que se le de al algoritmo. Ej: NSGA2_90_6_5
  #file = models.FileField()                        #Fichero adjunto a cada algoritmo insertado
  fileName = models.CharField(max_length = 100)    #Nombre del fichero adjunto
  nVariablesAlgorithm = models.CharField(max_length = 100) # Numero de variables que posee el algoritmo a analizar.
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)
  hypervolumeValues = ListField()
class ChartsModel(models.Model):
    listValues = ListField()
    configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class MinAvgMaxChartModel(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class MinChartModel(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class AvgChartModel(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class MaxChartModel(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class StatisticDataframeTex(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)

class StatisticDataframeTxt(models.Model):
  listValues = ListField()
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)