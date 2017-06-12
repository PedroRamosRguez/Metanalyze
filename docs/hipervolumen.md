## Hipervolumen

Para comparar el rendimiento de las diferentes metaheurísticas utilizadas en la resolución de un problema multi-objetivo se implementó la métrica del hipervolumen.

El hipervolumen es la métrica más utilizada para comprobar el rendimiento de metaheurísticas. Para la implementación de esta métrica, se ha utilizado una implementación creada por [Simon Wessing](https://github.com/DEAP/deap/blob/master/deap/tools/indicator.py) adaptada de la librería [Pygmo](https://github.com/esa/pagmo/tree/master/PyGMO) con una serie de modificaciones para el correcto funcionamiento de la misma. Esta adaptación es una reimplementación en puro código Python del código de *by Fonseca et al. (Variant 3, Version 1.2)*

## Cita bibliográfica de la implementación del hipervolumen
*Hypervolume computation based on variant 3 of the algorithm in the paper:
C. M. Fonseca, L. Paquete, and M. Lopez-Ibanez. An improved dimension-sweep
algorithm for the hypervolume indicator. In IEEE Congress on Evolutionary
Computation, pages 1157-1163, Vancouver, Canada, July 2006.*