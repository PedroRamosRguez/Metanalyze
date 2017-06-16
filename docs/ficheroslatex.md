## Creación de ficheros latex

Para guardar los datos del hipervolumen por paso de cada algoritmo en un fichero *Latex*, lo que se ha realizado es lo siguientes pasos:

* Generar una plantilla de fichero *Latex*.
* Transformar el *DataFrame* de resultados de hipervolumen por paso de cada algoritmo a latex mediante el uso de la función de **Pandas** `DataFrame.to_latex()`.
* Escribir en la plantilla de fichero creada el contenido del `DataFrame.to_latex()`.
* Utilizar el módulo *subprocess* para generar el fichero *Latex* y *Pdf* con los resultados del algoritmo en concreto.


```python
filename = os.path.join(mediafolder,str(algorithm_names[i])+'results'+'.tex')
        template = r'''\documentclass[preview]{{standalone}}
                    \usepackage{{booktabs}}
                    \begin{{document}}
                    \begin{{tabular}}{{|c|c|c|c|}}
                    {}
                    \end{{tabular}}
                    \end{{document}}
                    '''
        with open(filename, 'wb') as f:
          f.write(template.format(df[i].to_latex()))
        subprocess.call(['pdflatex','-output-directory='+str(mediafolder),filename])
with open(filename, 'wb') as f:
          f.write(template.format(df[i].to_latex()))
        subprocess.call(['pdflatex','-output-directory='+str(mediafolder),filename])
```


## Creación ficheros Latex con los resultados estadísticos

En esta ocasión también se siguen los mismos pasos.

* Generar una plantilla de fichero *Latex*.
* Transformar el *DataFrame* de resultados de hipervolumen por paso de cada algoritmo a latex mediante el uso de la función de **Pandas** `DataFrame.to_latex()`.
* Escribir en la plantilla de fichero creada el contenido del `DataFrame.to_latex()`.
* Utilizar el módulo *subprocess* para generar el fichero *Latex* y *Pdf* con los resultados del algoritmo en concreto.

```python
filename = os.path.join(mediafolder,'statisticalResults.tex')
        template = r'''\documentclass[preview]{{standalone}}
                    \usepackage{{booktabs}}
                    \begin{{document}}
                    \begin{{tabular}}{{|c|c|c|}}
                    {}
                    \end{{tabular}}
                    \end{{document}}
                    '''
        
        with open(filename, 'wb') as f:
          f.write(template.format(statisticDftex.to_latex(escape=False)))
        subprocess.call(['pdflatex','-output-directory='+str(mediafolder),filename])
```

En esta ocasión, lo único diferente es la utilización de `escape=False` en la llamada a la función `statisticDftex.to_latex()` ya que al utilizar símbolos como `\` es necesario pasarle esta opción ya que sino al convertir el fichero a latex, lee este símbolo y lo transforma a formato texto introduciéndolo como `backslash` y no se generaría correctamente el símbolo utilizado.