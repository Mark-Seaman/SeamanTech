angular.module('hammer', ['ui.bootstrap']);

var tabs = [
    { 'title':"Tab 1", 'content':'Text Body 1' },
    { 'title':"Tab 2", 'content':'Text Body 2' },
    { 'title':"Tab 3", 'content':'Text Body 3' }
]


function HammerCtrl($scope) {
    $scope.text = [
        {"name": "Mark Seaman",   "children": [1,2,3] },
        {"name": "Stacie Seaman", "children": [3,4,5] },
        {"name": "Mark Seaman",   "children": [1,2,3] },
        {"name": "Stacie Seaman", "children": [3,4,5] },
        {"name": "Mark Seaman",   "children": [1,2,3] },
        {"name": "Stacie Seaman", "children": [3,4,5] }
    ]
}



function TabbedViewCtrl($scope) {
    $scope.tabs = tabs
}


function food_selector($scope) {

    $scope.selection = [ 'None' ]

    $scope.set_choices =  function(options) {
        $scope.options = options;
    }
        
    $scope.select_item = function(name) { 
        $scope.selection.push(name);
    }

    $scope.appetizers = '0'
}
