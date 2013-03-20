define([
  'jquery',
  'underscore',
  'backbone',
  'bootstrap',
  'text!templates/home.html',
  'jquery_flexslider',
  'jquery_quicksand',
  'script'
], function($, _, Backbone, Bootstrap, HomePageTemplate) {
    
    var HomePageView = Backbone.View.extend({
        el: $("#main"),
        initialize: function(){
        },
        render: function() {
            //var variables = LocalSession.toJSON();
            //var compiled = _.template(navTemplate, variables);
            //this.$el.html(compiled);
            this.$el.html(HomePageTemplate);
        }
    });
  return HomePageView;
});