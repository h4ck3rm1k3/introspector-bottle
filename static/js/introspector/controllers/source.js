//
'use strict';

/**
 * @ngdoc function
 * @name introspectorApp.controller:SourceCtrl
 * @description
 * # TreeCtrl
 * Controller of the introspectorApp
 */

// angular.module('introspectorApp')
//   .controller('SourceCtrl', function () {
//     this.awesomeThings = [
//         'HTML5 Boilerplate',
//         'AngularJS',
//         'Karma',
//         'angular-json-edit'
//     ];
//   });



angular.module('introspectorApp')
    .controller('AceCtrl', ['$scope',
                            function ($scope) {
                                // The modes
                                $scope.modes = ['Javascript'];
                                $scope.mode = $scope.modes[0];
                                
                                var data = $scope.$eval('raw_data_object');     
                                $scope.aceModel = JSON.stringify(data,
                                                                 null,
                                                                2);
                            }
                           ]
               );
