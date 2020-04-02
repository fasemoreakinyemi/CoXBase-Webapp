$(document).ready(function()
{

function render_No_match(){
$('#result_error').html("<div class='result_header'><h1>Found profile(s)</h1><h3 style='color:red; padding:20px;'> No match in the database for your query</h3></div>" )
};


var iso_field = "<li style='margin-right:30px;margin-top:5px;'><span style='white-space:nowrap'><select name='iso_field1' class='fieldlist' id='iso_subject'><option value='year'>year</option><option value='host'>host</option><option value='country'>country</option><option value='plasmid'>plasmid</option><option value='ada'>adaGene</option><option value='mst'>MST group</option><option value='mlva'>MLVA Genotype</option></select> <select name='iso_operator1' id='iso_operator' ><option value='='>=</option><option value='contains'>contains</option><option value='starts with'>starts with</option><option value='ends with'>ends with</option><option value='NOT'>NOT</option><option value='NOT contain'>NOT contain</option></select> <input type='text' name='iso_value1'  class='value_entry' id='iso_value' placeholder='Enter value...' /> </span></li>"
$( ".add_button" ).click(function( event ) {
	if($("#combo").is(':hidden')){$("#combo").show();}
	$("ul#query_list").append(iso_field)

})

$( "#isolate_form" ).submit(function( event ) {
var combo_para = ""
var combo_para = ($("#combo_para option:selected").val());
var query_items = $("ul#query_list li")
var container_list = []
query_items.each(function(){
	var subject = $(this).find("#iso_subject option:selected").val();
	var operatr = $(this).find("#iso_operator option:selected").val();
	var value = $(this).find("#iso_value").val();
	entry_list = [subject, operatr, value]
	container_list.push(entry_list)
})

var myjson = JSON.stringify(container_list)
var hst = location.host;
var url = "https://" + hst + "/webapp/query/isolates/" + myjson + "/" + combo_para
alert(url)
/*$.get(url, 'json').done(function(results) {
	if(results.hasOwnProperty('STATUS')){
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
}*/
	

event.preventDefault();
});
});         /*closee ready*/
