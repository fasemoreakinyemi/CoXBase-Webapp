$(document).ready(function()
{

var dict = {
	3: ["ms24","ms28","ms33"],
	6: ["ms23","ms24","ms27","ms28","ms33","ms34"],
	141: [ "ms01", "ms03", "ms07", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	142: [ "ms01", "ms03", "ms20", "ms21", "ms22", "ms23", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	15: [ "ms01", "ms03", "ms07", "ms12", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	16: [ "ms01", "ms03", "ms07", "ms12", "ms21", "ms22", "ms23", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34", "ms36"]};

function json2table(json){
	var cols = dict[142] //Object.keys(json[0]);
	var headerRow = '<tr>';
	var bodyRows = '';
	function capitalizeFirstLetter(string) {
		return string;
		}
	cols.map(function(col) {
	 headerRow += '<th>' + capitalizeFirstLetter(col) + '</th>';
		});
	headerRow += '<th>Genotype</th></tr>';

json.map(function(row) {
	bodyRows += '<tr>';
	cols.map(function(colName) {
		bodyRows += '<td>' + row[colName] + '</td>';
				});
	bodyRows += '<td>' + row['Genotype'] + '</td>';
	bodyRows += '<td><button class="btnView">View profile entries</button></td>';
	bodyRows += '</tr>';

	});
	return '<table id="resulttable"><tr>' + headerRow + '</tr>' + bodyRows + '</table>';
};

function create_table(header_array){
var num_cols = header_array.length;
var num_rows = 1;
var table_body = "<table class='query_table'>";
for (var i=0;i<num_rows;i++){
	table_body+="<tr>";
	$.each(header_array, function(index,value){
		table_body+="<th class='query_table_header'>" + value + "</th>";
	});
	table_body+="</tr>"
	table_body+="<tr>"
	$.each(header_array, function(index,value){
		table_body+="<td><input class='tr_entry' name=" + value + " type='number'></td>"
	});
	table_body+="</tr>";
	table_body+="</table>";
};
return table_body
}


$('#select_panel').change(function() {
var key = ($("#select_panel option:selected").val());
var panel = dict[key]
$('#table_div').html(create_table(panel))


});

$( "#mlva_form" ).submit(function( event ) {
var empty_field = [];
var map = {};
$(".tr_entry").each(function(){
	map[$(this).attr("name")] = $(this).val();
});
var len = Object.values(map).length;
var hst = location.host;
var url = "https://" + hst + "/webapp/fp_query"
for (var i=0; i<len; i++) {
	if(Object.values(map)[i] == "")
	{
		url+="/" + 0
		empty_field.push(i);
	} else {
		url+="/" + Object.values(map)[i]
	}
};
if (len === empty_field.length) {
	throw_empty_error()
} else {
	$('#empty_error').empty()
	$.get(url, 'json').done(function(results) {
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
}
event.preventDefault();
});

$( ".submitMLVA" ).click(function( event ) {
var empty_field = [];
var map_list = [];
$(".entry").each(function(){
	if ($(this).text() == " Not detected") {
		var empty_cell = 0
		map_list.push(empty_cell)
	} else {

	map_list.push($(this).text());
	}

});

var len = map_list.length;
var hst = location.host;
var url = "https://" + hst + "/webapp/fp_query"
for (var i=0; i<len; i++) {
		url+="/" + map_list[i]
}
	$.get(url, 'json').done(function(results) {
		create_result(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

event.preventDefault();
});


function create_result(data){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1></div>" + json2table(data))
};

function render_No_match(){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1><h3 style='color:red; padding:20px;'> No match in the database for the queried marker</h3></div>" )
};

function throw_empty_error(){
	$('#result').empty()
	$('#empty_error').html("<div class='container'><div class='well blue'><span class='error_well'><i class='fas fa-exclamation-triangle fa-2x'></i></span></div><div class='well white'>At least one input field should have an entry</div></div>")

}

$(".result_info").on("click", ".btnView",function(){
	var currentRow=$(this).closest("tr");
	var MLVAID=currentRow.find("td:eq(14)").text();
	var hst = location.host;
	var url = "https://" + hst + "/webapp/eview/mlva/" + MLVAID
	window.open(url, '_blank');

});

$("#rz_indicator").on("click", ".alnV",function(){
	var spacer = $(this).text().split(" ")[2];
	var id = location.href.split("/")[location.href.split("/").length - 1];
	var hst = location.host;
	var url = "https://" + hst + "/webapp/blast_api/" + id + "/" + spacer
	$.get(url, 'json').done(function(results) {
		create_alignment(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

});

function create_alignment(data){
	var alignments = data["result"]
	var blasterjs = require("biojs-vis-blasterjs");
        var instance  = new blasterjs({
            string: alignments,
            singleAlignment: "blast-single-alignment"
        });    

};

$("#sampleQuery").click(function(event) {
	$('input[name="ms01"]').val(4);
	$('input[name="ms03"]').val(7);
	$('input[name="ms20"]').val(11.5);
	$('input[name="ms21"]').val(6);
	$('input[name="ms22"]').val(6);
	$('input[name="ms23"]').val(3);
	$('input[name="ms24"]').val(2);
	$('input[name="ms26"]').val(1);
	$('input[name="ms27"]').val(5);
	$('input[name="ms28"]').val(6);
	$('input[name="ms30"]').val(2);
	$('input[name="ms31"]').val(4);
	$('input[name="ms33"]').val(7);
	$('input[name="ms34"]').val(4);
	
	event.preventDefault()
})


$("body").on("click", ".treeMLVA",function(){

	var path = location.pathname
	var path_list = path.split("/")
	var id = path_list[path_list.length - 1]
	var url_path = "/webapp/tree/mlva/" + id

	$.ajax({
            type:"POST",
            url: url_path,
            success:function(result){
		var url = result.ilink
		window.open(url, "_blank")
                }
        });




}); 
}); 
