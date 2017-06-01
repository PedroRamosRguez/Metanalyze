from jchart.config import DataSet,rgba
from random import randint,uniform
def colors():
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	alpha = uniform(0.5,1)
	color = 'rgba('+str(r)+','+str(g)+','+str(b)+','+str(alpha)+')'
	return color


