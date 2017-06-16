## ¿Qué es gulp-gh-pages?

Gulp-gh-pages es un paquete que permite automatizar la tarea de desplegar a la [gh-pages](./gh-pages.md) el contenido de un directorio.

## Instalación de gulp-gh-pages

Para instalar el plugin de gulp que automatice el despliegue a las github pages, es necesario instalar como dependencia el plugin. Para ello se instalará mediante el gestor de paquetes [NPM](https://www.npmjs.org)
`npm install --save-dev gulp-gh-pages`.

## Tarea para desplegar el gitbook realizado

Para automatizar el gitbook del proyecto creado a la gh-pages, es necesario crear una tarea. A continuación, se detalla el código de la tarea para realizar el despliegue del gitbook.

```js
const gulp = require('gulp');
const deploy = require ('gulp-gh-pages');

gulp.task('deploy',()=>{
  return gulp.src("./docs/_book/**/*")
  .pipe(deploy())
})
```

Esta tarea es una tarea que se llama deploy la cual actualizará la rama gh-pages del proyecto con el contenido de la carpeta `docs/_book` con la introducción de los ficheros de manera recursiva. Para el correcto funcionamiento de la tarea, es necesario que anteriormente se haya generado el gitbook. Para utilizar la tarea y realizar el despliegue es necesario acceder a la carpeta donde se encuentra el fichero gulpfile e introducir en consola el siguiente comando:

```bash
gulp deploy
```

```bash
[13:01:34] Using gulpfile ~/Documentos/repos/appTFG/gulpfile.js
[13:01:34] Starting 'deploy'...
[13:01:34] [gh-pages] Cloning repo
[13:01:34] [gh-pages] Checkout branch `gh-pages`
[13:01:34] [gh-pages] Updating repository
[13:01:37] [gh-pages] Copying files to repository
[13:01:38] [gh-pages] Adding 37 files.
[13:01:38] [gh-pages] Committing "Update 2017-06-16T12:01:34.139Z"
[13:01:38] [gh-pages] Pushing to remote.
[13:01:42] Finished 'deploy' after 8.83 s
```