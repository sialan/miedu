define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var AppRouter = Backbone.Router.extend({
    routes: {
      '*wtf': 'defaultAction'
    }
  });

  var initialize = function(){
    //window.LocalSession = new LocalSessionModel({ id: 1 });
    window.app_router = new AppRouter();

    //app_router.on('route:explore', function () {
    //  require(['views/miVideos'], function(ExploreView) {
    //  // We have no matching route, lets display the home page
    //    var exploreView = new ExploreView();
    //    var back_page = LocalSession.get("last_page");
    //    var temp_page = LocalSession.get("current_page");
    //    LocalSession.set({last_page: "", current_page: "explore"});
    //    exploreView.render();
    //  });
    //});
    app_router.on('route:defaultAction', function (wtf) {
      require(['views/homepage'], function(HomePageView) {
        // We have no matching route, lets display the home page
        var homepage = new HomePageView();
        homepage.render();
      });
    });
    Backbone.history.start();
  };
  return {
    initialize: initialize
  };
});