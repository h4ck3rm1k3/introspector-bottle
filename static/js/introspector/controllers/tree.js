//
'use strict';

/**
 * @ngdoc function
 * @name introspectorApp.controller:TreeCtrl
 * @description
 * # TreeCtrl
 * Controller of the introspectorApp
 */
angular.module('introspectorApp')
  .controller('TreeCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });


// (function () {
//   'use strict';
//   angular.module('ui.tree', [])
//     .constant('treeConfig', {
//       treeClass: 'angular-ui-tree',
//       emptyTreeClass: 'angular-ui-tree-empty',
//       hiddenClass: 'angular-ui-tree-hidden',
//       nodesClass: 'angular-ui-tree-nodes',
//       nodeClass: 'angular-ui-tree-node',
//       handleClass: 'angular-ui-tree-handle',
//       placeholderClass: 'angular-ui-tree-placeholder',
//       dragClass: 'angular-ui-tree-drag',
//       dragThreshold: 3,
//       levelThreshold: 30
//     });
// })();

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


    
