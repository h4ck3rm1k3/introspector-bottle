//
'use strict';

/**
 * @ngdoc function
 * @name introspectorApp.controller:SourceCtrl
 * @description
 * # TreeCtrl
 * Controller of the introspectorApp
 */
angular.module('introspectorApp')
  .controller('SourceCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
        'Karma',
        'angular-json-edit'
    ];
  });
  
angular.module('introspectorApp')
  .controller('SourceCtrlEditor', function () {
      var vm = this;
      vm.config = {
          name: 'JSON-editor',
          keywords: [
              'angular',
              'json',
              'editor'
          ],
          usage: {
              angular: {
                  directive: true
              }
          }
      };
      console.log(vm.config);
    

  });

