$(document).ready(function()
{

$( ".csv_fill" ).click(function( event ) {

	var path = location.pathname
	var path_list = path.split("/")
	var id = path_list[path_list.length - 1]
	var hst = location.hostname
	var url = "https://" + hst + "/webapp/result/is1111/" + id
	$.post(url, 'json').done(function(results) {
		downloadCSV(generate_csv(results), id)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});
	
	
})



function throw_empty_error(){
	$('#result').empty()
	$('#empty_error').html("<div class='container'><div class='well blue'><span class='error_well'><i class='fas fa-exclamation-triangle fa-2x'></i></span></div><div class='well white'>You did not select any method</div></div>")
}

function downloadCSV(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV file
    csvFile = new Blob([csv], {type: "text/csv"});

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Hide download link
    downloadLink.style.display = "none";

    // Add the link to DOM
    document.body.appendChild(downloadLink);

    // Click download link
    downloadLink.click();
}

function generate_csv(results) {
	var csv = Papa.unparse([results])
	return csv

}

});
