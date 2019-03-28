$(document).ready(function()
{

	var ctx = $('#barchart')[0].getContext('2d');
	ctx.canvas.width = 700;
	ctx.canvas.height = 500;
	myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: null,
        datasets: [{
            label: '# of Isolates',
            data: null,
            backgroundColor: "#3e95cd",
            borderWidth: 1
        }]
    },
    options: {
	responsive: true,
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

	var url = "http://localhost:6543/api/" + "SampleHost"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})


$("#SampleYear").on ("click", function () {
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + "SampleYear"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

});

$("#SampleHost").on ("click", function () {
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + "SampleHost"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

});
$("#SampleCountry").on ("click", function () {
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + "SampleCountry"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

});
$("#TypingID").on ("click", function () {
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + "TypingID"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

});
$("#CountryProvince").on ("click", function () {
	var url_path = window.location.pathname.split("/")[2]
	var url = "http://localhost:6543/api/" + "CountryProvince"

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.data.labels = label;
		myChart.data.datasets[0].data = values;
		myChart.update();
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

});


});	

