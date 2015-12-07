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


function HammerCtrl($scope,$http) {

    $scope.text    = []
    $scope.id      = '42'
    $scope.child   = '0'
    $scope.xname   = 'New Name'
    $scope.gstatus = 'no status'
    $scope.gdata   = "no data"
    $scope.pstatus = 'no status'
    $scope.pdata   = "no data"

    $scope.get_name = function () {
        return $scope.xname
    }

    $scope.add_record = function (name) {
        var id = parseInt($scope.id)
        $scope.text.push( {"id": id, "name": name, "children": ""} )
        $scope.id = id+1
    }

    $scope.add_child = function (name,child) {
        $scope.text.push({"name": name, "children": child})
    }


    $scope.get_config_data = function () {
        $http.get('/get_thot')
        .success(function(data,status,headers,config) {
            $scope.gstatus = status
            $scope.gdata = data
            $scope.text = data  
        })
        .error (function(data,status,headers,config) { 
            $scope.gstatus = status // 'Error: failed to get_thot'
            $scope.gdata = data // "no data"
        })            
    }
    //$scope.get_config_data()


    $scope.put_config_data = function () {
        $http.post ('/put_thot', $scope.text)
            .success (function(data,status,headers,config) {
                $scope.pstatus = status // "Success status"
                $scope.pdata = data
            })
            .error (function(data,status,headers,config) { 
                $scope.pstatus = status //'Error: failed to put_thot'
                $scope.pdata = data //"no data"
            }) 
    }
    //$scope.put_config_data($scope.text)
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
