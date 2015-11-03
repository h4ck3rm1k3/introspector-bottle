'use strict';

/**
 * @ngdoc overview
 * @name introspectorApp
 * @description
 * # introspectorApp
 *
 * Main module of the application.
 */
angular
  .module('introspectorApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: '/static/views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/tree', {
        templateUrl: '/static/views/tree.html',
        controller: 'TreeCtrl',
        controllerAs: 'tree'
      })
      .when('/graph', {
        templateUrl: '/static/views/graph.html',
        controller: 'GraphCtrl',
        controllerAs: 'tree'
      })

      .when('/source', {
        templateUrl: '/static/views/source.html',
        controller: 'SourceCtrl',
        controllerAs: 'tree'
      })

      .when('/table', {
        templateUrl: '/static/views/table.html',
        controller: 'TableCtrl',
        controllerAs: 'tree'
      })

.otherwise({
        redirectTo: '/'
      });
  });
