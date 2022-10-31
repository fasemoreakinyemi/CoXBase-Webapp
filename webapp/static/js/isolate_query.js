$(document).ready(function()
{

var subject_name = $("#iso_subject option:selected").val();
$('#iso_value').attr('name', subject_name);

$(document).on('change', 'select#iso_subject', function() {
	var subject_name = $(this).find("option:selected").val();
	$(this).siblings('input').attr('name', subject_name);
	reload_autocomplete(subject_name)
	
});

country_list = ['Portugal', 'Romania', 'Belgium', 'Australia', 'Greece', 'Namibia', 'Mongolia', 'Italy', 'Saudi Arabia', 'Slovakia', 'Austria', 'Japan', 'United Kingdom', 'Hungary', 'Ireland', 'United States', 'Canada', 'Cuba', 'Egypt', 'Denmark', 'South Africa', 'Qatar', 'Spain', 'Switzerland', 'Poland', 'Guyana', 'Netherlands', 'Central African Republic', 'China', 'Kyrgyzstan', 'Sweden', 'Morocco', 'Germany', 'Argentina', 'Algeria', 'France', 'Ethiopia', 'Brazil', 'Russia', 'Croatia', 'India', 'Ukraine', 'Iran', 'Lebanon']

ada_list = [{label: "Wildtype", value: 'pos.'},
	    {label: "Wildtype with insertion", value: 'pos.S'},
	    {label: "Negative", value: 'neg.'},
	    {label: "Q212 Deletion", value: 'Q212-del'},
	    {label: "Q154 Deletion", value: 'Q154-del'},
	    {label: "A431T SNP", value: 'pos.*'},
	    {label: "Wildtype*", value: 'pos.?'}]
var plasmid_list = ['QpH1', 'QpRS', 'nan', 'plasmidless', 'QpDV', 'QpDG']
var mst_list = ['1', '2', '4', '7', '8', '12', '16', '18', '20', '21', '23', '30', '32', '33', '35', '36', '37', '38', '39', '40']
var mlva_list = ['B1', 'B2', 'A1', 'A3', 'A13', 'A2', 'A7', 'A8', 'A6', 'A5', 'A9', 'D1', 'A11', 'nan', 'C4', 'C1', 'C2', 'C7', 'C8', 'C10', 'C11', 'C3', 'C15', 'D13', 'D11', 'B3', 'A28', 'B6', 'A20', 'D9', 'A16', 'A19', 'A29', 'B7', 'A21', 'D19', 'D14', 'A25', 'D12', 'D7', 'D8', 'B4', 'D10', 'A15', 'B5', 'D16', 'A17', 'D4', 'D18', 'D15', 'A14', 'A22', 'D20', 'A18', 'A26', 'A27', 'A24', 'C6', 'D17', 'A4', 'C14', 'D6', 'D2', 'D5', 'C5', 'C13', 'A23', 'C9', 'C12', 'A12', 'D3', 'B', 'C', 'D', 'E', 'A', 'H', 'F', 'G', 'P', 'p', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'Y', 'V', 'W', 'U', 'X', 'AE', 'AC', 'AD', 'AB', 'AA', 'Z', 'A10']

var year_list = ['1995', '1990', '1999', '1998', '2003', '1997', '2004', '2001', '2009', '2005', '1992', '1993', '1994', '1982', '1969', '1991', '1996', '2007', '2002', '2008', '1965', '1948', '2000', '1968', '1967', '1985', '1956', '1962', '1989', '1978', '1954', '2006', '1958', '1945', '1946', '1957', '1935', '1980', '1955', '1981', '1949', '1976', '2010', '2011', '1939', '2012', '1936', '1983', '1975', '2014']

var host_list = ['cattle', 'sheep', 'goat', 'deer', 'tick', 'human', 'environment', 'mouse', 'rodent', 'other']

$('input[name^="year"]').autocomplete( { source : year_list } );
$('input[name^="country"]').autocomplete( { source : country_list } );
$('input[name^="host"]').autocomplete( { source : host_list} );
$('input[name^="mlva"]').autocomplete( { source : mlva_list} );
$('input[name^="mst"]').autocomplete( { source : mst_list} );
$('input[name^="plasmid"]').autocomplete( { source : plasmid_list} );
$('input[name^="ada"]').autocomplete( { source : ada_list} );


function reload_autocomplete(val) {
	if (val == "year"){
		$('input[name^="year"]').autocomplete( { source : year_list } );
	}
	else if (val == "country"){
		$('input[name^="country"]').autocomplete( { source : country_list } );
	}
	else if (val == "host"){
		$('input[name^="host"]').autocomplete( { source : host_list } );
	}
	else if (val == "mlva"){
		$('input[name^="mlva"]').autocomplete( { source : mlva_list } );
	}
	else if (val == "mst"){
		$('input[name^="mst"]').autocomplete( { source : mst_list } );
	}
	else if (val == "plasmid"){
		$('input[name^="plasmid"]').autocomplete( { source : plasmid_list } );
	}
	else if (val == "ada"){
		$('input[name^="ada"]').autocomplete( { source : ada_list } );
	}

}



$('#isolate_form').validate({
	rules : {
		name : 'required',
		email : {
			required : true,
			email : true
		}
	}
});

function render_No_match(){
$('#result_error').html("<div class='result_header'><h1>Found records(s)</h1><h3 style='color:red; padding:20px;'> No match in the database for your query</h3></div>" )
};


function create_result(data){
$('#result').html("<div class='result_header'>MLVA tree: <button id='mlvaTree' class='my_button'>grapeTree</button><button id='itolTree' class='my_button'>phyD3</button><h1>Found record(s)</h1></div>" + json2table(data))
};

function json2table(json){
	var cols = Object.keys(json[0]);
	var headerRow = '<tr>';
	var bodyRows = '';
	function capitalizeFirstLetter(string) {
		return string;
		}
	cols.map(function(col) {
	 headerRow += '<th>' + capitalizeFirstLetter(col) + '</th>';
		});
//	headerRow += '<th>Genotype</th></tr>';

json.map(function(row) {
	bodyRows += '<tr>';
	cols.map(function(colName) {
		if (colName != "Pubmed"){
			col_val = row[colName]

			if (col_val == "None"){
				col_val = ""
			}
			else if (col_val == null ){
				col_val = ""
			}
			else {
				col_val = col_val
			}
			                 
		}
		else{
			col_val = row[colName]

			if (col_val == "None"){
				col_val = ""
			}
			else if (col_val == null ){
				col_val = ""
			}
			else {
				col_val = "<a href=" +"https://pubmed.ncbi.nlm.nih.gov/"+ col_val + "/ style='display:block;'>publication</a>"
			}
		}
		
		bodyRows += '<td>' + col_val + '</td>';
				});
	//bodyRows += '<td>' + row['Genotype'] + '</td>';
	//bodyRows += '<td><button class="btnView">View profile entries</button></td>';
	bodyRows += '</tr>';

	});
	return '<table id="resulttable"><tr>' + headerRow + '</tr>' + bodyRows + '</table>';
};


var iso_field = "<li style='margin-top:5px; margin-right:10px;'><span style='white-space:nowrap'><select name='iso_field1' class='fieldlist' id='iso_subject'><option value='year'>year</option><option value='host'>host</option><option value='country'>country</option><option value='plasmid'>plasmid</option><option value='ada'>adaGene</option><option value='mst'>MST group</option><option value='mlva'>MLVA Genotype</option></select> <select name='iso_operator1' id='iso_operator' ><option value='='>=</option><option value='contains'>contains</option><option value='starts with'>starts with</option><option value='ends with'>ends with</option><option value='NOT'>NOT</option><option value='NOT contain'>NOT contain</option></select> <input type='text' name='year'  class='value_entry' id='iso_value' placeholder='Enter value...' /><a style='margin-left:5px;' class='remove_field'><i class='fas fa-trash-alt fa-lg'></i></a></span></li>"
$( ".add_button" ).click(function( event ) {
	if($("#combo").is(':hidden')){$("#combo").show();}
	$("ul#query_list").append(iso_field)

})

$('body').on('click', 'a.remove_field', function() {
    $(this).parent().parent().remove()
});

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
//alert(url)
$.get(url, 'json').done(function(results) {
	if(results.hasOwnProperty('STATUS')){
		$("#result").empty()
		render_No_match()
	}
	else {
		$('#result_error').empty()
		create_result(results)
		}
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

	

event.preventDefault();
});

function default_tree_settings () {
    tree = d3.layout.phylotree();
    tree.branch_length (null);
    tree.branch_name (null);
    tree.node_span ('equal');
    tree.options ({'draw-size-bubbles' : false}, false);
    tree.node_circle_size (undefined);
    tree.radial (false);
}

$("body").on("click", "#mlvaTree",function(){
items_list = [];
	$('#resulttable tbody tr').each( function(){
	ent_list = []
	var genotype = $(this).find('td:nth-child(8)').text()
	if (! genotype == ""){
	ent_list.push(genotype)
	var name = $(this).find('td:nth-child(1)').text()
	ent_list.push(name)
	var host_type = $(this).find('td:nth-child(4)').text()
	ent_list.push(host_type)
	items_list.push( ent_list );
	ent_list = []
	}
});
	$.ajax({
            type:"POST",
            url:"/webapp/tree/mlva",
            data:JSON.stringify(items_list),
            success:function(result){
		var hst = location.host;
		var baseurl = "https://" + hst + "/GrapeTree/"
		var treeUrl = "?tree=https://" + hst + "/tmp/" + result.itms + ".nwk"
		var metaUrl = "&metadata=https://" + hst + "/tmp/" + result.itms + ".txt"
		var url = baseurl + treeUrl + metaUrl
		    

	window.open(url, "_blank")
//	tree(res).svg(d3.select("#tree_display")).layout();
                //alert( result.itms )
                }
        });
//	var hst = location.host;
//	var url = "https://" + hst + "/webapp/tree/mlva/analysis/" + JSON.stringify(items_list)

})
$("body").on("click", "#itolTree",function(){
items_list = [];
	$('#resulttable tbody tr').each( function(){
	ent_list = []
	var genotype = $(this).find('td:nth-child(8)').text()
	if (! genotype == ""){
	ent_list.push(genotype)
	var name = $(this).find('td:nth-child(1)').text()
	ent_list.push(name)
	var host_type = $(this).find('td:nth-child(4)').text()
	ent_list.push(host_type)
	items_list.push( ent_list );
	ent_list = []
	}
});
	$.ajax({
            type:"POST",
            url:"/webapp/tree/mlva",
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

});         /*closee ready*/

//$('#resulttable tbody tr td:nth-child(9)').each( function(){
