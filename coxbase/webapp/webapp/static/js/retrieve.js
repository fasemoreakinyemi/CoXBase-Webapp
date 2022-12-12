$(document).ready(function()
{


$('#success').hide();

function throw_acknowledgment_error(){
	$('#agreement').html("Please enter a submission ID")
}

$('#subForm').submit(function(e){

	$('#agreement').empty()
	if ($("#submissionID").val().length === 0){
		throw_acknowledgment_error()
		return false;
	}
	$('#submit_button').prop('disabled',true);
	var ID = $('#submissionID').val()

	$.ajax({
        type: "POST",
        url: "/webapp/retrieve",
        data: {submissionID:ID},
        cache: false
	}).done(function(){
	    $('#success').fadeIn(800);
	}).fail(function(){
		$('#fail').fadeIn(800)
	});
   e.preventDefault(); });


});



