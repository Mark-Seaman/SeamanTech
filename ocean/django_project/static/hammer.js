angular.module('hammer', ['ui.bootstrap']);

function BudgetController($scope) {
    $scope.name = 'Greeley Vineyard'

    $scope.income = 0
    $scope.giving = 110000
    $scope.rent = 6000

    $scope.todd = 24600
    $scope.jenny = 24600
    $scope.other_staff = 6000
    
    $scope.mortgage = 15000
    $scope.utilities = 14000
    $scope.other_operations = 15000
     
    $scope.global = 1000
    $scope.local = 3600
    $scope.other_outreach = 0 

    $scope.kids   = 2000
    $scope.sunday = 3000
    $scope.pastor = 2000
    $scope.other_ministry  = 1100
        

    $scope.income_change = function() {
        $scope.income     = parseInt($scope.giving) + parseInt($scope.rent)
        $scope.staff      = parseInt($scope.income)*.48
        $scope.operations = parseInt($scope.income)*.38
        $scope.outreach   = parseInt($scope.income)*.07
        $scope.ministry   = parseInt($scope.income)*.07
        $scope.avc = parseInt($scope.income)*.03
        $scope.staff_change()
        $scope.operations_change()
        $scope.outreach_change()
        $scope.ministry_change()
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
             parseInt($scope.sunday) - parseInt($scope.other_ministry) - parseInt($scope.pastor)
    }

    $scope.income_change()
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
