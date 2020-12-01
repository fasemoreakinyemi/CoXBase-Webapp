$(document).ready(function()
{

window.validateform = function(){
	if (document.forms['mlvaInput']['fastaentry'].value == "" && document.forms['mlvaInput']['fastafile'].value == "") {
		throw_empty_error()
    		$("#loader").remove();
		return false;
	}
	else if (document.forms['mlvaInput']['fastaentry'].value !== "" && document.forms['mlvaInput']['fastafile'].value !== "") {
		throw_multiple_error()
    		$("#loader").remove();
		return false;
	}
	else if (document.forms['mlvaInput']['fastaentry'].value !== "" && document.forms['mlvaInput']['fastaentry'].value.charAt(0) != ">") {
		throw_not_fasta_error()
		return false;
	}

	
};

function throw_empty_error(){
	$('#result').empty()
	$('#empty_error_mlva').html("<div class=''><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> Please upload a file in fasta format or paste your sequence in the sequence field <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
    $("#loader").css("display", "none");
}
function throw_multiple_error(){
	$('#result').empty()
	$('#empty_error_mlva').html("<div class=''><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> Please upload either a fasta file  or sequence input not both <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
}
function throw_not_fasta_error(){
	$('#result').empty()
	$('#empty_error_mlva').html("<div class=''><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> The sequences you submitted is not fasta formatted <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
}

function to_file(input_id){
	var text = document.getElementById(input_id).innerHTML;
	var textFile = new Blob([text], {type: 'text/plain'});
	return textFile
}

function send_to_backend(file){
	var formdata = new FormData();
	var hst = location.host;
	formdata.append('fastafile', file)
	$.ajax({
 	 url: 'https://'+ hst +'/webapp/result/mst',
  	data: formdata,
  	processData: false,
  	contentType: false,
  	type: 'POST',
  	success: function(data){
   	 alert(data);
  		}
	});

//	var xhr = new XMLHttpRequest();
//	xhr.open('POST', 'http://coxiella.net/webapp/result/mst', true)
//	xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
//	xhr.send(formdata)
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

 $("#mlva_form").on("submit", function(){
    $("#loader").fadeIn();
  });//subm

});

