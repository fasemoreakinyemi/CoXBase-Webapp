$(document).ready(function(){
var opts = {
         dynamicHide: true,
         height: 800,
         invertColors: false,
         lineupNodes: true,
         showDomains: true,
         showDomainNames: false,
         showDomainColors: true,
         showGraphs: true,
         showGraphLegend: true,
         showSupportValues: false,
         maxDecimalsSupportValues: 1,
         showLengthValues: false,
         maxDecimalsLengthValues: 3,
         showLength: false,
         showNodeNames: true,
         showNodesType: "all",
         showPhylogram: false,
         showTaxonomy: true,
         showFullTaxonomy: true,
         showSequences: false,
         showTaxonomyColors: true,
         backgroundColor: "#f5f5f5",
         foregroundColor: "#000000",
     };

function get_newick(){
	var id = location.href.split("/")[location.href.split("/").length - 1];
	var hst = location.host;
	var url = "https://" + hst + "/webapp/tree/phyd3/API/" + id 
	$.get(url, 'json').done(function(results) {
		var nwk_data = results.nwk
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});


}

var nwk_data = "" ;
	
window.load = function(){
	 jQuery("#familyID").val("HOM03D000802");
         jQuery('#foregroundColor').val(opts.foregroundColor);
         jQuery('#backgroundColor').val(opts.backgroundColor);
         jQuery('#foregroundColorButton').colorpicker({color: opts.foregroundColor});
         jQuery('#backgroundColorButton').colorpicker({color: opts.backgroundColor});
            d3.xml("sample.xml", function(xml) {
	var id = location.href.split("/")[location.href.split("/").length - 1];
	var hst = location.host;
	var url = "https://" + hst + "/webapp/tree/phyd3/API/" + id 
	$.ajax({
            type:"GET",
            url: url,
            success:function(result){
		nwk = String(result.nwk)
                var tree = phyd3.newick.parse(nwk);
                phyd3.phylogram.build("#phyd3", tree, opts);
		colorNewProfile()
                
	    }
        });
            });
        };

function colorNewProfile(){
	var vis = d3.select("#phyd3").append("svg:svg")
	plot = vis.selectAll("g.node.inner")
        node = $("g.leaf.node text");
        node.each(function(){
	    		if ($(this).text().toString() == "your profile ") {
				$(this).attr("stroke", "#FF0000")
				$(this).attr("fill", "#FF0000")
			}
	})}
});	

