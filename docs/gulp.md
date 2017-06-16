## ¿Qué es gulp?

Gulp es una herramienta de automatización de tareas escrito en Javascript para Node.js. Al contrario que otros sistemas de automatización como [Grunt](http://gruntjs.com/), Gulp hace uso del módulo [Stream](https://nodejs.org/api/stream.html) de Node.js para poder concatenar tareas usando tuberías. Normalmente los automatizadores de tareas escriben los cambios al disco después de cada tarea, lo que provoca retardo cuando manejamos muchos ficheros. La ventaja de usar tuberías, es que estos ficheros no pasan por el disco, sino que se pasan de tubería en tubería, lo que aumenta la velocidad a la que se ejecutan las tareas.

Para utilizar gulp y crear las tareas de automatización es necesario crear antes un fichero llamado `gulpfile.js`

* [Página web de Gulp](http://gulpjs.com/)
* [Repositorio en Github](https://github.com/gulpjs/gulp)
* [Documentación](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)