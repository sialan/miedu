define([
  'jquery',
  'underscore',
  'backbone',
  'views/nav',
  'views/footer',
  'router'
], function($, _, Backbone, NavbarView, FooterView, Router) {
  
    var initialize = function() {
        alert(4);
        try {
            //var navbar = new NavbarView();
            //navbar.render();
            //var footer = new FooterView();
            //footer.render();
            //Router.initialize();
        } catch (e) {
            alert(e);
        }
    };

  return {
    initialize: initialize
  };

});