
$(document).ready(function()
{

$('#mlva_field').multiselect();
$('#mst_field').multiselect();

$("#multimarker_form").submit(function (e) {
        var fd = new FormData();
	var fastaFile = $('#fileInput').prop('files');
	var selectedMLVAmarkers = [];
	var selectedMSTspacers = [];
	$("#mlva_field :selected").each(function(){
		selectedMLVAmarkers.push($(this).val());
	})
	$("#mst_field :selected").each(function(){
		selectedMSTspacers.push($(this).val());
	})

        // Check file selected or not
        if(fastaFile.length > 0 ){
		fd.append('fastafile', fastaFile[0], type="text/plain");
        	if(selectedMLVAmarkers.length > 0 || selectedMSTspacers.length > 0){
			fd.append('mlva_markers', JSON.stringify(selectedMLVAmarkers));
			fd.append('mst_spacers', JSON.stringify(selectedMSTspacers));
	   
           		$.ajax({
              			url: '/webapp/result/multimarker',
              			type: 'post',
              			data: fd,
				beforeSend: function() {
					$('#empty_error').empty()
					$('#result').empty()
					$("#loader").fadeIn();},
              			contentType: false,
              			processData: false,
              			success: function(response){
					$("#loader").fadeOut();
					create_result(response)
                 			}
           			});
        	}else{
           		throw_empty_marker();
        	}
	}else{
		throw_empty_file();
	}

	e.preventDefault()
})

function throw_empty_marker(){
	$('#result').empty()
	$('#empty_error').html("<div style='margin-top:40px;margin-left:350px;'><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> Please select a marker or spacer <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
    $("#loader").css("display", "none");
}
function throw_empty_file(){
	$('#result').empty()
	$('#empty_error').html("<div style='margin-top:40px;'><div class='well blue_card'><span><i class='fas fa-exclamation-triangle fa-2x'></i></span> Please upload a FASTA file <span><i class='fas fa-exclamation-triangle fa-2x'></i></span></div>")
}

function create_result(data){
	if  (Object.keys(data).length === 0){
		$('#result').html("<div class='result_header'><h1>Found profile(s)</h1><div style='color:red;' class='well white'>No matches for this query in the database, try using 5+ as the Max Distance</div></div>")
	}
	else{
		$('#result').html("<div class='result_info'><div class='result_header'><h1>Result(s)</h1></div>" + json2table(data) + "</div>")}
};

function json2table(json){
	var cols = Object.keys(json["result"]);
	var headerRow = '';
	var bodyRows = '';
	function capitalizeFirstLetter(string) {
		return string;
		}
	cols.map(function(col) {
	 headerRow += '<th>' + capitalizeFirstLetter(col) + '</th>';
		});

	bodyRows += '<tr>';
	Object.values(json["result"]).map(function(row) {
		bodyRows += '<td style="color:#40B0A6;">' + row + '</td>';})

	bodyRows += '</tr>';

	return '<table class="query_table"><tr>' + headerRow + '</tr>' + bodyRows + '</table>';
	};

});
