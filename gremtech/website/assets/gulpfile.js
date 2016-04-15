var gulp = require("gulp"),
    cfg = require("./gt.config"),

    glob = require("glob"),
    cProcess = require("child_process"),

    imagemin = require("gulp-imagemin"),
    pngquant = require("imagemin-pngquant");


gulp.task("js", function(){

    var fileList = glob.sync(cfg.js + "/*.js"),
        fileName, bundle;

    fileList.map(function(entry){

        fileName = /\w+(?=\.js)/gi.exec(entry)[0];
        bundle = cProcess.exec('jspm bundle-sfx '+ entry +' '+ cfg.out + '/js/'+ fileName +'.bundle.min.js --minify --skip-source-maps')

        return bundle;
    })

});

gulp.task("css", function(){

    var fileList = glob.sync(cfg.css + "/*.less"),
        fileName, bundle;

    fileList.map(function(entry){
        fileName = /\w+(?=\.less)/gi.exec(entry)[0];
        bundle = cProcess.exec('lessc --clean-css '+ entry +' --autoprefix="last 2 versions" '+ cfg.out +'/css/'+ fileName +'.bundle.min.css');

        return bundle;
    })

});

gulp.task("fonts", function(){
    gulp.src(cfg.fonts +"/**/*.*").pipe(gulp.dest(cfg.out +"/fonts/"));
});

gulp.task("images", function(){

     gulp.src(cfg.images +"/**/*.*")
        .pipe(imagemin({
            optimizationLevel: 4,
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(gulp.dest(cfg.out +"/images/"));

});

gulp.task("watcher", function(){

    //gulp.watch(cfg.js +"/**/*.js", ["js"]);
    gulp.watch(cfg.css +"/**/*.less", ["css"]);
    gulp.watch(cfg.fonts +"/**/*.*", ["fonts"]);
    gulp.watch(cfg.images +"/**/*.*", ["images"]);

});

gulp.task("default", ["css", "fonts", "images", "js"]);
