
$(document).ready(function()
{

var path_name = window.location.href;
var wanted_id = path_name.split("/")[5];
var hst = location.host;
var url = "http://" + hst + "/webapp/api_view_map/" + wanted_id

$.get(url, 'json').done(function(results) {
		draw_map(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

function draw_map(results){
var coord_array = JSON.parse(JSON.stringify(results));
var mymap = L.map('view_map').setView([51, -10], 4);
	
//map.flyTo(new L.LatLng(51, 11), 6);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
	coord_array.forEach(function(row){

		marker = new L.marker(L.latLng(parseFloat(row['lat']),parseFloat(row['long']))).bindPopup(row['name']).addTo(mymap)
	})
}
});
