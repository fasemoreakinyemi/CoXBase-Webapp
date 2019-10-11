$(document).ready(function()
{

dict = {'mlva' : '<table class="query_table"><tr><th class="query_table_header">ms01</th><th class="query_table_header">ms03</th><th class="query_table_header">ms20</th><th class="query_table_header">ms21</th><th class="query_table_header">ms22</th><th class="query_table_header">ms23</th><th class="query_table_header">ms24</th><th class="query_table_header">ms26</th><th class="query_table_header">ms27</th><th class="query_table_header">ms28</th><th class="query_table_header">ms30</th><th class="query_table_header">ms31</th><th class="query_table_header">ms33</th><th class="query_table_header">ms34</th></tr><tr><td><input class="tr_entry" name="ms01" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms03" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms20" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms21" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms22" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms23" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms24" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms26" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms27" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms28" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms30" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms31" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms33" type="number" min="0" step="any"></td><td><input class="tr_entry" name="ms34" type="number" min="0" step="any"></td></tr></table>',
	'mst' : '<table class="query_table"><tr> <th class="query_table_header">COX2</th><th class="query_table_header">COX5</th><th class="query_table_header">COX18</th><th class="query_table_header">COX20</th><th class="query_table_header">COX22</th><th class="query_table_header">COX37</th><th class="query_table_header">COX51</th><th class="query_table_header">COX56</th><th class="query_table_header">COX57</th><th class="query_table_header">COX61</th></tr><tr><td><input class="tr_entry" name="cox2" type="number"></td><td><input class="tr_entry" name="cox5" type="number"></td><td><input class="tr_entry" name="cox18" type="number"></td><td><input class="tr_entry" name="cox20" type="number"></td><td><input class="tr_entry" name="cox22" type="number"></td><td><input class="tr_entry" name="cox37" type="number"></td><td><input class="tr_entry" name="cox51" type="number"></td><td><input class="tr_entry" name="cox56" type="number"></td><td><input class="tr_entry" name="cox57" type="number"></td><td><input class="tr_entry" name="cox61" type="number"></td></tr></table>'}
$('.js-example-basic-single').select2();

$('#select_panel').change(function() {
var key = ($("#select_panel option:selected").val());
var panel = dict[key]
$('#table_div').html(panel)
})

window.validateform = function(){
	if ($("#aof").prop('checked') == false){
	throw_acknowledgment_error()
		return false;
	}
	
};

function throw_acknowledgment_error(){
	$('#agreement').html(" !!! Please agree to fair use by ticking this checkbox")
}

})


