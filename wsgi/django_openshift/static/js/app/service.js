//  Rest service calls
angular.module('django-service.services', [])

    // Config for http provider and CSRF token compatibility with Django
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
        ])
    .factory('APIservice', function($http) {
        var APIservice = {};
        // define API calls and return data
        
        // Ping server to check status
        APIservice.pingService = function() {
            return $http({
                method: 'GET',
                url: '/api/ping/'
            });
        }
        return APIservice;
    });