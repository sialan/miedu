requirejs.config({
  baseUrl: 'js',
  paths: {
    jquery: 'libs/jquery/jquery-min.js',
    "jquery-quicksand": 'libs/jquery/jquery.quicksand',
    "jquery-flexslider": 'libs/jquery/jquery.flexslider-min',
    bootstrap: 'libs/bootstrap/bootstrap.min',
    underscore: 'libs/underscore/underscore-min',
    backbone: 'libs/backbone/backbone-optamd3-min',
    script: 'scripts/script'
  },
  shim: {
    bootstrap: ["jquery"],
    backbone: {
      deps: ["jquery", "underscore"],
      exports: "Backbone"
    },
    "jquery-quicksand": ["jquery"],
    "jquery-flexslider": ["jquery-quicksand"],
    script: ["jquery-flexslider"]
  }
});

requirejs([
  'app'
], function(App){
  App.initialize();
});