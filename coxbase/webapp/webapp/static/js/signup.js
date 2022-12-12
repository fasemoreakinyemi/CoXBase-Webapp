
$(document).ready(function()
{

$('#success').hide();
$('#fail').hide();
$('#signup').submit(function(e){
	$('#submit_button').prop('disabled',true);
	var emailInput = $('#email').val()
	var usernameInput = $('#username').val()
	var passwordInput = $('#password').val()

	$.ajax({
        type: "POST",
        url: "/webapp/register",
        data: {email:emailInput, username:usernameInput, password:passwordInput},
        cache: false
	}).done(function(){
            $('#signup').fadeOut(800);
	    $('#success').fadeIn(800);
	}).fail(function(){
		$('#fail').fadeIn(800)
	});
   e.preventDefault(); });


});
