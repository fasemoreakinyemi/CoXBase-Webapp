
$(document).ready(function(){

var hst = location.host;
var url = "http://" + hst + "/webapp/coxviewer_api"
$.get(url, 'json').done(function(results) {
		draw_map(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

function draw_map(results){

var coord_array = JSON.parse(JSON.stringify(results));
var map = L.map('coxviewermap').setView([35, 0], 2.8).setMaxBounds([[-90, -180],[90, 180]]);
L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd'}).addTo(map);
/*L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);*/

function get_iconAnchor(cnt){
	return cnt > 50 ?  [40, 80] :
	       cnt > 10 ?  [30, 60] :
	                    [20, 40] ;
}

function get_popAnchor(cnt){
	return cnt > 50 ?  [0, -80] :
	       cnt > 10 ?  [0, -60] :
	                    [0, -40] ;
}

function get_class(cnt){
	return cnt > 50 ?  'outer_circle_big' :
	       cnt > 10 ?  'outer_circle_medium' :
	                    'outer_circle_small' ;
}
	coord_array.forEach(function(row){

		myhtml = '<div class="inner_circle">' + row['count'] + '</div>'
		myIcon = L.divIcon({
			html: myhtml,
			className: get_class(row['count']),
			iconSize: null,
			iconAnchor: get_iconAnchor(row['count']),
			popupAnchor: get_popAnchor(row['count'])

		});

		var hst = location.host;
		var table_url = "http://" + hst + "/webapp/coxviewer_table/" + row['ID']
		var dashboard_url = "http://" + hst + "/webapp/dashboard/" + row['ID']
		if (row['count'] > 10) {
		mypopup = '<div class=""><h2>Details</h2><table class="table"><tbody><tr><td>Country</td><td>' + row['name'] + '</td></tr><tr><td>No of Isolates </td><td>' + row['count'] + '</td></tr><tr><td>Isolates table</td><td><a href=' + table_url + '><button class="popbutton">here</button></a></td><tr><td>Dashboard</td><td><a href=' + dashboard_url + '><button class="popbutton">here</button></a></td></tr></tbody></table></div>'
		} else {
			mypopup = '<div class=""><h2>Details</h2><table class="table"><tbody><tr><td>Country</td><td>' + row['name'] + '</td></tr><tr><td>No of Isolates </td><td>' + row['count'] + '</td></tr><tr><td>Isolates table</td><td><a href=' + table_url + '><button class="popbutton">here</button></a></td></tr></tbody></table></div>'}

		var customOptions = { 'maxWidth': '250', 'className' : 'custom' }
		marker = new L.marker(L.latLng(parseFloat(row['lat']),parseFloat(row['long'])), {icon: myIcon}).bindPopup(mypopup, customOptions).addTo(map)
	})

var legend = L.control({position: 'topright'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        color = ['#db4453', '#684d91', '#ffc300'],
        labels = {'#db4453': '50 - 200', '#684d91' : '10 - 50', '#ffc300': '1 - 10'}

    // loop through our density intervals and generate a label with a colored square
    for (var i = 0; i < color.length; i++) {
        div.innerHTML +=
            '<p><span style="background:' + color[i] + '"></span>' + labels[color[i]] + '</p>'
    }

    return div;
};

legend.addTo(map);

}

  
  
$(window).on("resize", function() {
    $("#coxviewermap").height($(window).height()).width($(window).width());
    map.invalidateSize();
}).trigger("resize");

});

