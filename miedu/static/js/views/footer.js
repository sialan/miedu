define([
  'jquery',
  'underscore',
  'backbone',
  'bootstrap',
  'text!templates/footer.html',
  'jquery_flexslider',
  'jquery_quicksand',
  'script'
], function($, _, Backbone, Bootstrap, FooterTemplate) {
    
    var FooterView = Backbone.View.extend({
        el: $("#navigation"),
        initialize: function(){
        },
        render: function() {
            //var variables = LocalSession.toJSON();
            //var compiled = _.template(navTemplate, variables);
            //this.$el.html(compiled);
            this.$el.html(FooterTemplate);
        }
    });
  return FooterView;
});