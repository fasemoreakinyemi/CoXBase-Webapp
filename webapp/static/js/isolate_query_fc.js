
$(document).ready(function(){

var hst = location.host;
var url = "https://" + hst + "/webapp/query/isolate/fc/api"
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
	colHeaders: ['Name', 'YearofIsolation', 'Host', 'Source', 'Location',
			'Province', 'PlasmidType', 'adaGeneType', 'MLVA genotype',
				'MST genotype', 'is Group'],
  	filters: true,
	hiddenColumns: {
    		columns: [4],
    		indicators: false
	},
  	dropdownMenu: ['filter_by_condition', 'filter_action_bar', 'filter_by_value'],
	licenseKey: "non-commercial-and-evaluation"
});
	hot.updateSettings({
        readOnly: true
    });}
});



