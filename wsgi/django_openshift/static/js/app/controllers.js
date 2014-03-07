// Rest service controller

angular.module('django-service.controllers', []).
    // Say hello to service
    controller('pingController', function($scope, APIservice) {
        $scope.ping = function(){

            APIservice.pingService().success(function (data) {
            //Dig into the response to get the ping response
            $scope.data = data
        })
            .error(function() {
                // handling service error
                alert('BOOOM!') // be more creative
            })
        }
    });
