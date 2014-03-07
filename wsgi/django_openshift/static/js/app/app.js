var service = angular.module('django-service', [
    'ngRoute', // Include Angular routing modele
    'django-service.services',
    'django-service.controllers'
    ]);
// config some app base routing
service.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: 'static/pages/hello.html',
            controller: 'pingController'
        }).
        otherwise({
            redirectTo: '/'
        });
    }
    ]);
