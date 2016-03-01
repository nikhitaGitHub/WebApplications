var gulp = require('gulp');
var browserSync = require('browser-sync').create();

gulp.task('default', ['styles'], function() {
	console.log("Hello");
	gulp.watch('css/**/*.css', ['styles']).on('change', browserSync.reload);
  	browserSync.init({
    	server: "./"
	});
	browserSync.stream();
});

gulp.task('styles', function() {
	gulp.src('css/**/*.css')
		.pipe(browserSync.stream());
});

