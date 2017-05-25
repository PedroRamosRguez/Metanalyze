from jchart.config import DataSet,rgba
from random import randint,uniform
def colors():
	print 'estoy en getcolors..'
	#'rgba(255,99,132,1)'
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	alpha = uniform(0.5,1)
	color = 'rgba('+str(r)+','+str(g)+','+str(b)+','+str(alpha)+')'
	return color


