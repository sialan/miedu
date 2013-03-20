define([
  'jquery',
  'underscore',
  'backbone',
  'bootstrap',
  'text!templates/nav.html',
  'jquery_flexslider',
  'jquery_quicksand',
  'script'
], function($, _, Backbone, Bootstrap, NavTemplate) {
    
    var NavbarView = Backbone.View.extend({
        el: $("#navigation"),
        initialize: function(){
        },
        render: function() {
            //var variables = LocalSession.toJSON();
            //var compiled = _.template(navTemplate, variables);
            //this.$el.html(compiled);
            this.$el.html(NavTemplate);
        }
    });
  return NavbarView;
});