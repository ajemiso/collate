/**
 * Created by Dizz on 9/4/16.
 */
function logIn() {
   var $username = $('input[id="username"]').val();
   var $password = $('#password').val();

   var data = {'username': $username, 'password': $password}

  $.ajax({
      url: 'http://localhost:8000/login/',
      type: 'POST',
      data: data,
      error: alert();
     });

};


$('#login').submit(function(evt) {
    evt.preventDefault();
    logIn();


});