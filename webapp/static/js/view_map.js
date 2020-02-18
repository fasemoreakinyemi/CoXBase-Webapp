
$(document).ready(function()
{

var url;
var path_name = window.location.href;
var wanted_id = path_name.split("/")[6];
var typing_method =  path_name.split("/")[5];
var hst = location.host;
if (typing_method === "mlva"){
	var url = "https://" + hst + "/webapp/api_mlva_map/" + wanted_id
}else{
	var url = "https://" + hst + "/webapp/api_mst_map/" + wanted_id
}
$.get(url, 'json').done(function(results) {
		draw_map(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});
function extend_cord(pos){
	var baseJitter = 1.5;
  	var rnd = Math.random;
	new_pos = pos - baseJitter / 2 + rnd() * baseJitter;
	return new_pos;
}

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
	var redMarker = L.AwesomeMarkers.icon({
    		icon: 'bug',
		prefix : 'ion',
    		markerColor: 'orange',
		iconColor: 'black'
  		});
	latitude_list = []
	longitude_list = []
	coord_array.forEach(function(row){
		if (latitude_list.includes(row['lat'])) {
			latitude = extend_cord(row['lat'])
			
		}
		else{
		 	latitude_list.push(row['lat'])
			latitude = row['lat']
		}
		if (longitude_list.includes(row['long'])) {
			longitude = extend_cord(row['long'])
			
		}
		else{
		 	longitude_list.push(row['long'])
			longitude = row['long']
		}

		marker = new L.marker(L.latLng(parseFloat(latitude),parseFloat(longitude)), {icon: redMarker}).bindPopup(row['name']).addTo(mymap)
	})
}
});
