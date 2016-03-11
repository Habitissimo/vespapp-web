var gulp = require('gulp');
var path = require('path');
var less = require('gulp-less');
var sourcemaps = require('gulp-sourcemaps');
var concat = require('gulp-concat');
var minifyCSS = require('gulp-minify-css');
var lessPluginAutoPrefix = require('less-plugin-autoprefix');
var autoprefix= new lessPluginAutoPrefix({ browsers: ["last 2 versions"] });

// Watching paths
var paths = {
  scripts: ['src/js/**/*.js'],
  images: ['src/img/**/*'],
  less: ['src/less/**/*.less'],
  dist: 'web/static/'
};

gulp.task('default', function() {
  // main task
});

gulp.task('scripts', function() {
  // scripts task
  return gulp.src([
    'bower_components/jquery/dist/jquery.min.js',
    'bower_components/bootstrap/dist/js/bootstrap.min.js',
    'src/**/*.js'
  ])
    .pipe(sourcemaps.init())
    .pipe(concat('main.min.js'))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(path.join(paths.dist, 'js/')));
});

gulp.task('watch', function() {
  // main task
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(paths.less, ['less']);
});

gulp.task('less', function() {
  // main task
  return gulp.src('./src/less/main.less')
  .pipe(less({
    plugins: [autoprefix]
  }))
  .pipe(minifyCSS())
  .pipe(concat('main.min.css'))
  .pipe(gulp.dest('./web/static/css'));
});