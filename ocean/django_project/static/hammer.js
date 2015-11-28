angular.module('hammer', ['ui.bootstrap']);

function BudgetController($scope) {
    $scope.name = 'Greeley Vineyard'

    $scope.income = 0
    $scope.giving = 110000
    $scope.rent = 6000

    $scope.todd = 26000
    $scope.jenny = 26000
    $scope.other_staff = 90
    
    $scope.mortgage = 20000
    $scope.utilities = 20000
    $scope.other_operations = 90
     
    $scope.avc = 1000
    $scope.global = 9999
    $scope.local = 9000
    $scope.other_outreach = 9999

    $scope.kids = 0
    $scope.sunday =9

    $scope.income_change = function() {
        $scope.income = parseInt($scope.giving) + parseInt($scope.rent)
        $scope.staff = parseInt($scope.giving)*.45
        $scope.operations = parseInt($scope.giving)*.35
        $scope.outreach = parseInt($scope.giving)*.1
        $scope.ministry = parseInt($scope.giving)*.1
    }
    $scope.staff_change = function() {
        $scope.remaining_staff = parseInt($scope.staff) - parseInt($scope.other_staff) -
            parseInt($scope.todd) - parseInt($scope.jenny)
    }
    $scope.operations_change = function() {
        $scope.remaining_operations = $scope.operations - parseInt($scope.other_operations) -
            parseInt($scope.mortgage) - parseInt($scope.utilities)
    }
    $scope.outreach_change = function() {
        $scope.remaining_outreach = $scope.outreach - parseInt($scope.avc) - 
            parseInt($scope.local) - parseInt($scope.global) - parseInt($scope.other_outreach)
    }
    $scope.ministry_change = function() {
        $scope.remaining_ministry = $scope.ministry - parseInt($scope.kids) -
             parseInt($scope.sunday)
    }

    $scope.income_change()
    $scope.staff_change()
    $scope.operations_change()
    $scope.outreach_change()
    $scope.ministry_change()

}

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
