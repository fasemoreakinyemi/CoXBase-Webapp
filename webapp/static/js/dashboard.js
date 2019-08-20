$(document).ready(function()
{

	var ctx = $('#chart')[0].getContext('2d');
	ctx.canvas.width = 700;
	ctx.canvas.height = 500;
	myChart = new Chart(ctx, {
    	type: 'line',
    	data: {
        labels: null,
        datasets: [{
            label: '',
            data: null,
	    fill: false,
            backgroundColor:"#4bc0c0",
            borderColor:"#4bc0c0",
            borderWidth: 2
        }]
    },
    options: {
	responsive: true,
	maintainAspectRatio: false,
        scales: {
            yAxes: [
		    {
		    scaleLabel: {
			    display: true
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

	var hst = location.host;
	var url_path = window.location.pathname.split("/")[3]
	var url = "http://" + hst + "/webapp/api_country/" + url_path

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
	var url_path = window.location.pathname.split("/")[3]
	var hst = location.host;
	var url = "http://" + hst + "/webapp/api_country/" + url_path

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.destroy();
		myChart = new Chart(ctx, {
    		type: 'line',
    		data: {
        		labels: null,
       			 datasets: [{
            			label: 'isolates',
            			data: null,
	    			fill: false,
            			backgroundColor:"#4bc0c0",
            			borderColor:"#4bc0c0",
            			borderWidth: 2
        			}]
    			},
    		options: {
			responsive: true,
			maintainAspectRatio: false,
        		scales: {
            			yAxes: [
		    		{
		    		scaleLabel: {
			    		display: true
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
	var url_path = window.location.pathname.split("/")[3]
	var hst = location.host;
	var url = "http://" + hst + "/webapp/api_host/" + url_path

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.destroy();
		myChart = new Chart(ctx, {
    		type: 'doughnut',
    		data: {
        		labels: null,
       			 datasets: [{
            			label: 'sources',
            			data: null,
            			backgroundColor:["#ff6384", "#ff9f40", "#ffcd56", "#36a2eb", "#4bc0c0", "#64b448", "#fff8dc"],
            			borderWidth: 2
        			}]
    			},
			options: {
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Distribution by Host'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});

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
	var url_path = window.location.pathname.split("/")[3]
	var hst = location.host;
	var url = "http://" + hst + "/webapp/api_genotype/" + url_path

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.destroy();
		myChart = new Chart(ctx, {
    		type: 'doughnut',
    		data: {
        		labels: null,
       			 datasets: [{
            			label: 'sources',
            			data: null,
            			backgroundColor:["#ff6384", "#ff9f40", "#ffcd56", "#36a2eb", "#4bc0c0", "#64b448", "#fff8dc", "#93b4cd", "#e33e1b",
						 "#cc6623", "#93b4cd", "#c4fee4", "#2a0e3c", "#2e585b", "#fcb900", "#353535", "#e0e0e0", "#b6dedc",
						  "#f86464", "#fffc74", "#89afb4", "#d6735d", "#efcc82", "#c093b2", "#826860", "#0054a6",  "#89cff0",
						   "#d87fc8", "#ee5444", "#ee5444", "#21aca9", "#7475bb", "#038376", "#74054d", "#f9b1b1", "#055269"],
            			borderWidth: 2
        			}]
    			},
			options: {
				rotation: 1 * Math.PI,
        			circumference: 1 * Math.PI,
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Distribution by MLVA Genotypes'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});

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
	var url_path = window.location.pathname.split("/")[3]
	var hst = location.host;
	var url = "http://" + hst + "/webapp/api_province/" + url_path

	$.get(url, 'json').done(function(results) {
		item = JSON.parse(JSON.stringify(results))
		var i, label = [], values = [];
		for(var key in item) label.push(key);
		for (var key in item) values.push(item[key]);
		myChart.destroy();
		myChart = new Chart(ctx, {
    		type: 'doughnut',
    		data: {
        		labels: null,
       			 datasets: [{
            			label: 'sources',
            			data: null,
            			backgroundColor:["#ff6384", "#ff9f40", "#ffcd56", "#36a2eb", "#4bc0c0", "#64b448", "#fff8dc", "#93b4cd", "#e33e1b",
						 "#cc6623", "#93b4cd", "#c4fee4", "#2a0e3c", "#2e585b", "#fcb900", "#353535", "#e0e0e0", "#b6dedc",
						  "#f86464", "#fffc74", "#89afb4", "#d6735d", "#efcc82", "#c093b2", "#826860", "#0054a6",  "#89cff0",
						   "#d87fc8", "#ee5444", "#ee5444", "#21aca9", "#7475bb", "#038376", "#74054d", "#f9b1b1", "#055269"],
            			borderWidth: 2
        			}]
    			},
			options: {
				rotation: 1 * Math.PI,
        			circumference: 1 * Math.PI,
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Distribution by province'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});

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

