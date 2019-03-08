$(document).ready(function()
{
//	display_href()
	get_data()
	
})

function display_href(){
	var ref = window.location.href
	var dom_ = window.location.hostname
	var pat = window.location.pathname.split("/")
	alert(pat[2])
	




}
function get_data(){


	// get data
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + url_path

	$.get(url, 'json').done(function(results) {
		drawchart(results)
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

}


	
function drawchart(result) {
	// get key value
	item = JSON.parse(JSON.stringify(result))
	var i, label = [], values = [];
	for(var key in item) label.push(key);
	for (var key in item) values.push(item[key]);
	
	// get element
	var ctx = $('#barchart')[0].getContext('2d');
	ctx.canvas.width = 700;
	ctx.canvas.height = 500;
	myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label,
        datasets: [{
            label: '# of Isolates',
            data: values,
            backgroundColor: "#3e95cd" // "#8e5ea2","#3cba9f","#e8c3b9","#c45850"
            ,
          //  borderColor: [
          //      'rgba(255,99,132,1)',
          //      'rgba(54, 162, 235, 1)',
          //      'rgba(255, 206, 86, 1)',
          //      'rgba(75, 192, 192, 1)',
          //      'rgba(153, 102, 255, 1)',
          //      'rgba(255, 159, 64, 1)'
          //  ],
            borderWidth: 1
        }]
    },
    options: {
	responsive: false,
	maintainAspectRatio: false,
        scales: {
            yAxes: [
		    {
		    scaleLabel: {
			    display: true,
			    labelString: 'Count',
		    },
                ticks: {
                    beginAtZero:true
                }
            }
	    ],
		xAxes: [{
                ticks: {
                    beginAtZero:true,
			autoSkip:false
                }
            }]

        }
    }
});
	

}

function update_chart(result) {
	// get key value
	item = JSON.parse(JSON.stringify(result))
	var i, label = [], values = [];
	for(var key in item) label.push(key);
	for (var key in item) values.push(item[key]);
	myChart.data.labels = label;
	myChart.data.datasets.data = values;
	myChart.update();
}

//$( "button" ).click(function() {
//	var cond = $(this).attr("value");
//	var url = "http://localhost:6543/api/" + cond
//
//	$.get(url, 'json').done(function(results) {
//		update_chart(results)
//
//		
//	}).fail(function (e){
//		if (e.error) {
//			alert("error due to" + e.error)
//		}
//		else {
//			alert("fail")
//		}
//		})
//	
//
//});
//
//  
////function draw_filter_chart(){
////      // get current url
////	var url_path = window.location.pathname.split("/")[2]
//	var cond = $(this).value
//	var url = "http://localhost:6543/api/" + url_path
//	alert(cond)
//}
//	// add filter
//	// get data
//	// make plot
