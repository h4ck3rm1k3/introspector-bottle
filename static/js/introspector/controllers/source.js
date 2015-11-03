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
    .controller('SourceCtrlEditor',
                ['$scope',
                 function ($scope) {
                     var vm = this;
                     var data = $scope.$eval('raw_data_object');
                     vm.config = data;
                     console.log(vm.config);
                 }
                ]
               );

