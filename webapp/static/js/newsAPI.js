$(document).ready(function()
{




$('.js-example-basic-single').select2();

$( "#subform" ).submit(function( event ) {
var search = $("#searchTerm").val()
var lang = $("#select_panel").val()

var hst = location.host;
var url = "https://" + hst + "/webapp/newsAPI/" + lang +"/" + search

if (search == "" ) {
	throw_empty_error()
} else {
	$('#empty_error').empty()
	$.get(url, 'json').done(function(results) {
		if(results.totalResults == 0) {
			render_No_match()

		}
		else {
		create_result(results)
		}
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});
}
event.preventDefault();
});



function create_result(results){
	var container = $("#result")
	container.empty()
	for(var i = 0; i < results.results.articles.length; i++) {
		var obj = results.results.articles[i];
		div = create_div(obj)
		container.append(div)
}

};

function create_div(obj){

 var newdiv = "<div class='card' style='width: 56rem;'>" +
  "<img src=" + obj.urlToImage + " style='width:72px;height:72px;'" +
    "<div class='card-body'>" +
    "<h5 class='card-title'>" + obj.title + "</h5>" +
    "<p class='card-text'>" + obj.description + "</p>" +
    "<hr><p class='card-text'>Source: " + obj.source.name + "</p>" + 
    "<hr><a href=" + obj.url + " target='_blank' class='btn btn-primary'>More</a></div></div>"
return newdiv


}


function render_No_match(){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1><h3 style='color:red; padding:20px;'> Nothing was found for your search term</h3></div>" )
};

function throw_empty_error(){
	$('#result').empty()
	$('#empty_error').html("<div class='container'><div class='well blue'><span class='error_well'><i class='fas fa-exclamation-triangle fa-2x'></i></span></div><div class='well white'>You've not submitted any search term</div></div>")

}


}); 
