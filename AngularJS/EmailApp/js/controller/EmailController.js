app.controller('EmailController', ['$scope', 'emails', '$routeParams', function($scope, emails, $routeParams) {
  emails.success(function(data) {
    $scope.emailExpand = data[$routeParams.id];
  });
}]);