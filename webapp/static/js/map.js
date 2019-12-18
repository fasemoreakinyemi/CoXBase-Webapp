
$(document).ready(function()
{

var map = L.map('map').setView([51, -10], 4);
map.flyTo(new L.LatLng(51, 11), 6);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 40,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.light'
}).addTo(map);

var geojson = L.geoJson(statesData).addTo(map);

// functions
function getColor(d) {
    return d > 40 ? '#800026' :
           d > 30  ? '#BD0026' :
           d > 20  ? '#E31A1C' :
           d > 15  ? '#FC4E2A' :
           d > 10   ? '#FD8D3C' :
           d > 5   ? '#FEB24C' :
           d > 1   ? '#FED976' :
                      '#FFEDA0';
}

function style(feature) {
    return {
        fillColor: getColor(feature["properties"]["No. of Isolates"]),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
};

function json2table(json){
		var cols = Object.keys(json[0]);
		var headerRow = '';
		var bodyRows = '';
		function capitalizeFirstLetter(string) {
			return string.charAt(0).toUpperCase() + string.slice(1);
			}
		cols.map(function(col) {
 		 headerRow += '<th>' + capitalizeFirstLetter(col) + '</th>';
			});
	
	json.map(function(row) {
  		bodyRows += '<tr>';
		cols.map(function(colName) {
  			bodyRows += '<td>' + row[colName] + '</td>';
					});
		bodyRows += '</tr>';

		});
		return '<table><tr>' + headerRow + '</tr>' + bodyRows + '</table>';
};

function show_details(e){
	layer = e.target
	var data;
      var state = layer.feature["properties"]["State"] //(feature ? feature["properties"]["State"] : 'none');
	var hst = location.host;
	var url = "https://" + hst + "/webapp/api_map/CountryProvince/" + state;
	$.get(url, 'json').done(function(results) {
		create_table(results)
		//alert(results['2']['GENUS'])
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		});
};
function create_table(data){

	$('#new-parent').html(json2table(data))
};

//var details = L.control();
//
//details.onAdd = function (map) {
//    this._div = L.DomUtil.create('div', 'details'); // create a div with a class "info"
//    this.update();
//    return this._div;
//};
//
//details.update = function (feature) {
//	var data;
//	state = (feature ? feature["properties"]["State"] : 'none');
//	var url = "http://localhost:6543/api_map/CountryProvince/" + state;
//	$.get(url, 'json').done(function(results) {
//		data = results
//		//alert(results['2']['GENUS'])
//	}).fail(function (e){
//		if (e.error) {
//			alert("error due to" + e.error)
//		}
//		else {
//			alert("fail")
//		}
//		});
//
//    	details._div.innerHTML = (feature ?
//        '<b>' + feature["properties"]["State"] + '</b><br />' + feature["properties"]["No. of Isolates"] + ' isolate(s)<br>' + json2table(data)
//        : '');
//};
//details.addTo(map);
//var htmlObject = details.getContainer();
//
//var side = document.getElementById('new-parent');
//
//side.appendChild(htmlObject);
//};

// info
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (feature) {
    this._div.innerHTML = '<h4>Isolate Information </h4>' +  (feature ?
        '<b>' + feature["properties"]["State"] + '</b><br />' + feature["properties"]["No. of Isolates"] + ' isolate(s)<br>' +'<i>click for more details</i>'
        : 'Hover over a state');
};

info.addTo(map);
// info end 


//var htmlObject = info.getContainer();
//
//var side = document.getElementById('new-parent');
//
//side.appendChild(htmlObject);

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });
    info.update(layer.feature);
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
	info.update();
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
	    click: show_details
    });
}

geojson = L.geoJson(statesData, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);

});
