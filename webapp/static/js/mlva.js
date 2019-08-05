$(document).ready(function()
{
formdata = new FormData();

$('#fileInput').change(function(){    
    //on change event  
    if($(this).prop('files').length > 0)
    {
        file =$(this).prop('files')[0];
        formdata.append("fastafile", file);
    }
});

$( "#lva_form" ).submit(function( event ) {
	event.preventDefault();
	var myfile = $('#fileInput').prop('files')[0];
	var hst = location.host;
	var url = "http://" + hst + "/webapp/mlvaresult"
	$.ajax({
                    method: 'POST',
                    url: url,
                    data:formdata,
		    processData: false,
    		    contentType: false,
                    success: function(response) {
                        console.log(response)
                    },
                    error: function(response) {
                        console.error(response)
                    }
                });

})
});


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

function exportprimertableToCSV(filename) {
    var csv = [];
    var rows = document.querySelectorAll("table tr");

    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");

        for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);

        csv.push(row.join(","));
    }

    // Download CSV file
    downloadCSV(csv.join("\n"), filename);
}


