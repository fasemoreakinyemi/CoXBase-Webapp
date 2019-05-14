$(document).ready(function()
{


var dict = {
	3: ["ms24","ms28","ms33"],
	6: ["ms23","ms24","ms27","ms28","ms33","ms34"],
	14: [ "ms01", "ms03", "ms07", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	15: [ "ms01", "ms03", "ms07", "ms12", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	16: [ "ms01", "ms03", "ms07", "ms12", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34", "ms36"]};

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
		for (var i=0;i<num_cols;i++){
			table_body+="<td><input class='tr_entry'></td>"
		};
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



});	

