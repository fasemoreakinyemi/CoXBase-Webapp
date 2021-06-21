$(document).ready(function()
{

var dict = {
	3: ["ms24","ms28","ms33"],
	6: ["ms23","ms24","ms27","ms28","ms33","ms34"],
	141: [ "ms01", "ms03", "ms07", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	142: [ "ms01", "ms03", "ms20", "ms21", "ms22", "ms23", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	15: [ "ms01", "ms03", "ms07", "ms12", "ms20", "ms21", "ms22", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34"],
	16: [ "ms01", "ms03", "ms07", "ms12", "ms21", "ms22", "ms23", "ms24", "ms26", "ms27", "ms28", "ms30", "ms31", "ms33", "ms34", "ms36"]};


$('.query_table tbody tr td input').bind('paste', null, function (e) {
        $txt = $(this);
        setTimeout(function () {
	console.log($txt.val())
        var values = $txt.val().split(/\s+/);
	console.log(values)
        var currentColIndex = $txt.parent().index();
        console.log(currentColIndex)
        var totalCols = $('.query_table thead th').length;
        var count =0;
        for (var i = currentColIndex; i < totalCols; i++) {
             var value = values[count];
             console.log(value)
             var inp = $('.query_table tbody tr td').eq(i).find('input');
             inp.val(value);
             count++;
                           
                        }


                }, 0);
            });

function json2table(json, marker_dict){
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
		if (parseFloat(marker_dict[colName]) == parseFloat(row[colName])){
		bodyRows += '<td style="color:green;">' + row[colName] + '</td>';
		}
		else {
			bodyRows += '<td style="color:red;">' + row[colName] + '</td>'
		}

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
var query_dict = {};
$(".tr_entry").each(function(){
		query_dict[$(this).attr("name")] = $(this).val();
	});
var distance = ($("#distance option:selected").val());
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
	var url = url + "/" + distance
	$.get(url, 'json').done(function(results) {
		if(results.hasOwnProperty('STATUS')){
			render_No_match()

		}
		else {
		create_result(results, query_dict)
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
marker_list = dict[142]
marker_dict = {}
marker_list.forEach((key, i) => marker_dict[key] = map_list[i]);
var distance = ($("#distance option:selected").val());
var len = map_list.length;
var hst = location.host;
var url = "https://" + hst + "/webapp/fp_query"
for (var i=0; i<len; i++) {
		url+="/" + map_list[i]
}
var url = url + "/" + distance
	$.get(url, 'json').done(function(results) {
		create_result(results, marker_dict)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

event.preventDefault();
});


function create_result(data, marker_dict){
if  (Object.keys(data).length === 0){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1><div style='color:red;' class='well white'>No matches for this query in the database, try using 5+ as the Max Distance</div></div>")
}
else{
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1></div>" + json2table(data, marker_dict) + "<div style='margin-top:20px;'> Phylogenetic tree: <button id='tree' class='my_button'>Phyd3</button></div>")}
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
	$('input[name="ms20"]').val(9);
	$('input[name="ms21"]').val(6);
	$('input[name="ms22"]').val(6);
	$('input[name="ms23"]').val(8);
	$('input[name="ms24"]').val(29);
	$('input[name="ms26"]').val(4);
	$('input[name="ms27"]').val(4);
	$('input[name="ms28"]').val(6);
	$('input[name="ms30"]').val(5.5);
	$('input[name="ms31"]').val(19);
	$('input[name="ms33"]').val(9);
	$('input[name="ms34"]').val(5);
	
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
		var hst = location.host;
		var baseurl = "https://" + hst + "/webapp/tree/phyd3/"
		var url = baseurl + result.itms
		    

	window.open(url, "_blank")
                }
        });




}); 

$("body").on("click", "#tree",function(){
	items_list = [];
	mlva_list = []
	ent_list = []
	$(".tr_entry").each(function(){
		if ($(this).val() == ""){
			mlva_list.push("0");}
		else{
			mlva_list.push($(this).val());}

	});

	$('#resulttable tbody tr').each( function(){
	var genotype = $(this).find('td:nth-child(15)').text()
	if (! genotype == ""){
	ent_list.push(genotype)
	}
});
	items_list.push(mlva_list)
	items_list.push(ent_list)
	$.ajax({
            type:"POST",
            url:"/webapp/tree/mlva_query",
            data:JSON.stringify(items_list),
            success:function(result){
		var hst = location.host;
		var baseurl = "https://" + hst + "/webapp/tree/phyd3/"
		var url = baseurl + result.itms
		    

	window.open(url, "_blank")
//	tree(res).svg(d3.select("#tree_display")).layout();
                //alert( result.itms )
                }
        });
//	var hst = location.host;
//	var url = "https://" + hst + "/webapp/tree/mlva/analysis/" + JSON.stringify(items_list)

})


$("body").on("click", ".downloadbutton",function(){
var address = location.pathname
var path_list = address.split("/")
var id = path_list[path_list.length - 1]
var Genotype = path_list[path_list.length - 2].toUpperCase()
var today = new Date();
var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
var dd = String(today.getDate()).padStart(2, '0');
var mm = months[today.getMonth()]
var yyyy = today.getFullYear();

today = mm + "." + " " + dd + "," + " " + yyyy
var date_accessed = "Date accessed: " + today
var doc = new jsPDF();
doc.setFontSize(12);
doc.text(date_accessed, 140, 50);
// image
var myImage = new Image();
myImage.src = "https://coxbase.q-gaps.de/webapp/static/img/logo_transparent.png";
myImage.onload = function(){
doc.addImage(myImage , 'png', 10, 10, 60, 60);

// meta
doc.setFillColor(238,238,238);
doc.rect(10, 80, 190, 10, "F");
doc.setFont("Normal", "bold");
doc.setTextColor("#555555");
doc.setFontSize(14);
doc.text("Genotyping method", 13, 87);
doc.text("#ID", 180, 87);
doc.text(id, 120, 97);
doc.text(Genotype, 13, 97);

// Result
doc.setFillColor(238,238,238);
doc.rect(10, 120, 190, 10, "F");
doc.setFont("Normal", "bold");
doc.setTextColor("#555555");
doc.setFontSize(14);
doc.text("Result", 13, 127);
doc.autoTable({ html: '.jspdf', startY:140 })


doc.save(id + '.pdf');
};

//doc.rect(10, 20, 100, 20, "F");
//doc.setFontSize(16);
//doc.setFont("courier", "bold");
//doc.setTextColor("#555555");
//doc.text("Genotyping Method", 20, 50);

});

}); 
