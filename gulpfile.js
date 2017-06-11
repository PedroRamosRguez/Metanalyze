const gulp = require('gulp');
const deploy = require ('gulp-gh-pages');

gulp.task('deploy',()=>{
  return gulp.src("./docs/_book/**/*")
  .pipe(deploy())
})