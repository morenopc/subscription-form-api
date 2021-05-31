var app = angular.module('subscriptionApp', []);

app.controller('SubscriptionListController', function($scope, $http) {
  var subscriptions = [];
  var api_host = 'http://localhost:8000/';

  $scope.options = [
    {name:'Free', value:'free'},
    {name:'Plus', value:'plus'},
    {name:'Pro', value:'pro'}
  ];
  
  $scope.subscription_type = $scope.options[0].value;

  $http.get(api_host + 'api/subscriptions/').then(
    function(response) {
        $scope.subscriptions = response.data;
    });

  $scope.addSubscription = function() {
    if ($scope.subscription_form.$valid) {
      var data = {
        name: this.name,
        email: this.email,
        subscription_type: this.subscription_type
      }
      $http.post(api_host + 'api/subscriptions/', data).then(
        function(response) {
        $scope.subscriptions.unshift(response.data);
      });

      $scope.name = '';
      $scope.email = '';
      $scope.subscription_type = $scope.options[0].value;
    }
  };
});
