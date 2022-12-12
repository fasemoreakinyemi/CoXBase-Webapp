
$(document).ready(function(){

var country_id = window.location.pathname.split("/")[3]
var hst = location.host;
var url = "https://" + hst + "/webapp/coxviewer_api/" + country_id 
$.get(url, 'json').done(function(results) {
		make_grid(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});



function make_grid(data){
	var container = document.getElementById('coxviewertable');
	var hot = new Handsontable(container, {
  	data: data,
  	rowHeaders: false,
	colHeaders: ['Name', 'YearofIsolation', 'Host', 'Source', 'Country',
		'Province', 'PlasmidType', 'adaGeneType', 'MLVA genotype',
				'MST genotype', 'PubMed PMID'],
  	filters: true,
	hiddenColumns: {
	},
  	dropdownMenu: ['filter_by_condition', 'filter_action_bar', 'filter_by_value'],
	licenseKey: "non-commercial-and-evaluation"
});
	hot.updateSettings({
        readOnly: true
    });}
});



