$(document).ready(function()
{

var path = location.pathname
var path_list = path.split("/")
var id = path_list[path_list.length - 1]
var hst = location.host;
var url = "https://" + hst + "/webapp/status/arg-prediction/" + id
var count = 0

function check_status(){
	$.ajax({
		type: "GET",
        	url: url
		}).done(function(data){
	    		display_result(data);
			}).fail(function(){
			$('#fail').fadeIn(800)
			});

}

function display_result(data){
	if (data["state"] == "PENDING"){
		setTimeout(function () { check_status() }, 1 * 60 * 1000);
		count += 1
		if (count > 7) {
			$(".well-lg").remove()
			$(".container").append("<div class='well'>Server is not responding to this task contact admin</div>");

		}
	}
	else {
		$(".well-lg").remove()
		d3.csv('https://coxbase.q-gaps.de/predictions/' + id + '.csv')
		.then(makeChart);
	}

}

function make_grid(data){
	var container = document.getElementById('coxviewertable');
	var hot = new Handsontable(container, {
  	data: data,
  	rowHeaders: false,
	colWidths: 300,
	manualColumnResize: true,
	colHeaders: ["Name", "Length", "Sequence", "Category", "Probability"],
  	filters: true,
	contextMenu: ['copy'],
  	dropdownMenu: ['filter_by_condition', 'filter_action_bar', 'filter_by_value'],
	style: ''
	licenseKey: "non-commercial-and-evaluation"
});
	hot.updateSettings({
        readOnly: true
    });}

function makeChart(pred) {
  var count_dict = {}
  var Labels = pred.map(function(d) {return d["Predicted ARG category"]});
  const counts = {};
  for (const num of Labels) {
  counts[num] = counts[num] ? counts[num] + 1 : 1;
	}

  var chart = new Chart('chart', {
    type: 'bar',
    options: {
      maintainAspectRatio: false,
      plugins: {
	      legend: {
                display: false
              },
             title: {
	        display: true,
	         text: 'Distribution by ARG category'
	     }
    }},
    data: {
      labels: Object.keys(counts),
      datasets: [
        {
          data: Object.values(counts),
	  fill: false,
          backgroundColor:["#ff6384", "#ff9f40", "#ffcd56", "#36a2eb", "#4bc0c0", "#64b448", "#fff8dc"],
          borderWidth: 2
        }
      ]
    }
  })
make_grid(pred)
}

setTimeout(function () { check_status() }, 1 * 60 * 10);

});



