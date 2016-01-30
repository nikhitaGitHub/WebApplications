var app = angular.module('OutboxApp', ['ngRoute']);
app.config(function($routeProvider) {
  $routeProvider
    .when('/outbox/:id', {
       controller:'HomeController',
       templateUrl:'views/home.html'
     })
     .when( '/outbox',{
       controller:'EmailController',
       templateUrl:'views/emails.html'
     })
    .otherwise({
       redirectTo:'/'
     });
});