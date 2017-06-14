## Generación de los colores de los gráficos creados.

Para asignarle colores a los gráficos generados por la librería *Django-jchart*, es necesario crear un array con el color rgb y la transparencia del color añadido. Un ejemplo de asignación de color a un gráfico sería el siguiente:

```python
colors = [
            rgba(255, 99, 132, 0.2),
            rgba(54, 162, 235, 0.2),
            rgba(255, 206, 86, 0.2),
            rgba(75, 192, 192, 0.2),
            rgba(153, 102, 255, 0.2),
            rgba(255, 159, 64, 0.2)
        ]
```

Debido a que la utilización de la aplicación permite un uso dinámico del número de algoritmos a analizar y comparar, se generó una función la cual generaba'colores de manera aleatoria. Esta manera, no restringía en ningún momento el número de colores a crear sino que sería dinámico. El código utilizado para esta tarea es el siguiente:

```python
from jchart.config import rgba
from random import randint,uniform
def colors():
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	alpha = uniform(0.5,1)
	color = 'rgba('+str(r)+','+str(g)+','+str(b)+','+str(alpha)+')'
	return color
```

Esta función, devuelve en formato cadena un color rgba aleatorio y lo guardará en un array utilizado para este fin.