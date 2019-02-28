$(document).ready(function()
{
	var frm = $('form')
	
	frm.submit(function(e)
	{
		loadDetails()

		e.preventDefault()
		return false
	})
})

function loadDetails(){
	// get id
	var org_id = $("input").val()
	// window.alert(org_id)
	//
	var url = "http://localhost:6543/api2/" + org_id

	$.get(url, 'json').done(function(results) {
		populatedetails(results)
		//alert(results['2']['GENUS'])
	}).fail(function (e){
		if (e.error) {
			alert("error due to" + e.error)
		}
		else {
			alert("fail")
		}
		})

}

function populatedetails(item) {

	 var org_id = $("input").val()

	 $("#org_details").fadeOut(function() {
         $("#genus").text(item[org_id]['GENUS'])
         $("#species").text(item[org_id]['SPECIES'])
         $("#ncbi").text(item[org_id]['NCBIASSEMBLY'])
         $("#strain").text(item[org_id]['STRAIN'])
	 $("#org_details").fadeIn('slow')
	 })
}




