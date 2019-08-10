$(document).ready(function()
{

window.validateform = function(){
	if (document.forms['mlvaInput']['fastaentry'].value == "" && document.forms['mlvaInput']['fastafile'].value == "") {
		throw_empty_error()
		return false;
	}
};

function throw_empty_error(){
	$('#result').empty()
	$('#empty_error_mlva').html("<div class=''><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> Please upload a file in fasta format or paste your sequence in the sequence field <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
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

});

