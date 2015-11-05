//
'use strict';

/**
 * @ngdoc function
 * @name introspectorApp.controller:TableCtrl
 * @description
 * # TreeCtrl
 * Controller of the introspectorApp
 */
function domap(x) {
    return {
        val : x,
    };
}

angular.module('introspectorApp').controller(
    'TableCtrl',
    ['$scope', 'uiGridConstants',
     function ($scope, uiGridConstants )
     {
         $scope.gridOptions = {  
             enableFiltering: true,
             flatEntityAccess: true,
             showGridFooter: true,
             showColumnFooter: true,
             fastWatch: true,
             enableCellEditOnFocus: true,
         };

         $scope.gridOptions.columnDefs = [
             {
                 name:'val',
                 
             },
         ];
        
         var data = $scope.$eval('raw_data_object');
         $scope.gridOptions.data = data['stdout'].map(domap);
     }
    ]);
 
