/*eslint-env node*/

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();

var imagemin = require('gulp-imagemin');
var pngquant = require('imagemin-pngquant');


gulp.task('default', ['copy-html', 'copy-images','images','styles', 'cssStyle'], function() {
	gulp.watch('css/**/*.css', ['cssStyle']).on('change', browserSync.reload);
	gulp.watch('index.html', ['copy-html']).on('change', browserSync.reload);
	gulp.watch('sass/**/*.scss', ['styles']);
	browserSync.init({
		server: './'
	});
	browserSync.stream();
});

gulp.task('cssStyle', function() {
	gulp.src('dist/css/**/*.css', {'read': false})
		.pipe(browserSync.stream());
    });

gulp.task('copy-html', function() {
	gulp.src('./index.html')
		.pipe(gulp.dest('./dist'));
});

gulp.task('copy-images', function() {
	gulp.src('images/*')
		.pipe(gulp.dest('dist/img'));
});

gulp.task('images', function() {
	return gulp.src('dist/img/*')
        .pipe(imagemin({
 			progressive: true,
         	use: [pngquant()]
        }))
        .pipe(gulp.dest('dist/images'));
});

gulp.task('styles', function() {
	gulp.src('sass/**/*.scss')
		.pipe(sass().on('error',sass.logError))
		.pipe(autoprefixer({
			browsers: ['last 2 versions']
		}))
		.pipe(gulp.dest('dist/css'));
});