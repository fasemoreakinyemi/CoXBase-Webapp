$(document).ready(function()
{

var example_tree = "'(((((((other:1.071429,sheep:1.071429):0.161361,(((goat:0.142857,sheep:0.142857):0.142857,goat:0.285714):0.417776,sheep:0.703490):0.529300):0.119204,(((human:0.428571,goat:0.428571):0.230935,human:0.659507):0.253306,rodent:0.912813):0.439181):0.140503,((((((((((cattle:0.071429,cattle:0.071429):0.035714,cattle:0.107143):0.007199,cattle:0.114342):0.001730,cattle:0.116071):0.041196,(goat:0.071429,cattle:0.071429):0.085839):0.026489,(cattle:0.142857,cattle:0.142857):0.040899):0.094379,((cattle:0.071429,cattle:0.071429):0.107143,cattle:0.178571):0.099563):0.073989,cattle:0.352124):0.177630,cattle:0.529754):0.016485,cattle:0.546238):0.946257):0.503005,human:1.995501):0.721331,((((((((goat:0.071429,sheep:0.071429):0.071429,(goat:0.071429,sheep:0.071429):0.071429):-0.008039,((sheep:0.071429,sheep:0.071429):0.035714,sheep:0.107143):0.027676):0.148795,cattle:0.283614):0.094377,(human:0.214286,cattle:0.214286):0.163705):0.007705,sheep:0.385696):0.292494,(goat:0.214286,human:0.214286):0.463905):0.353721,(sheep:0.500000,sheep:0.500000):0.531912):1.684920):0.479510,(cattle:1.000000,cattle:1.000000):2.196341);'"

function default_tree_settings () {
    tree = d3.layout.phylotree();
    tree.branch_length (null);
    tree.branch_name (null);
    tree.node_span ('equal');
    tree.options ({'draw-size-bubbles' : false}, false);
    //tree.radial (true);
    //tree.style_nodes (node_colorizer);
    //tree.style_edges (edge_colorizer);
    //tree.selection_label (current_selection_name);
    tree.node_circle_size (undefined);
    tree.radial (false);
}

function default_tree(){
var example_tree = "'(((((((other:1.071429,sheep:1.071429):0.161361,(((goat:0.142857,sheep:0.142857):0.142857,goat:0.285714):0.417776,sheep:0.703490):0.529300):0.119204,(((human:0.428571,goat:0.428571):0.230935,human:0.659507):0.253306,rodent:0.912813):0.439181):0.140503,((((((((((cattle:0.071429,cattle:0.071429):0.035714,cattle:0.107143):0.007199,cattle:0.114342):0.001730,cattle:0.116071):0.041196,(goat:0.071429,cattle:0.071429):0.085839):0.026489,(cattle:0.142857,cattle:0.142857):0.040899):0.094379,((cattle:0.071429,cattle:0.071429):0.107143,cattle:0.178571):0.099563):0.073989,cattle:0.352124):0.177630,cattle:0.529754):0.016485,cattle:0.546238):0.946257):0.503005,human:1.995501):0.721331,((((((((goat:0.071429,sheep:0.071429):0.071429,(goat:0.071429,sheep:0.071429):0.071429):-0.008039,((sheep:0.071429,sheep:0.071429):0.035714,sheep:0.107143):0.027676):0.148795,cattle:0.283614):0.094377,(human:0.214286,cattle:0.214286):0.163705):0.007705,sheep:0.385696):0.292494,(goat:0.214286,human:0.214286):0.463905):0.353721,(sheep:0.500000,sheep:0.500000):0.531912):1.684920):0.479510,(cattle:1.000000,cattle:1.000000):2.196341);'"

var tree = d3.layout.phylotree()
      // create a tree layout object
      .svg(d3.select("#tree_display"))
	.radial(false)
	.options({
		'zoom':false});
      // render to this SVG element

    tree(example_tree)
      // parse the Newick into a d3 hierarchy object with additional fields
      .layout();
      // layout and render the tree
}

$("#Country").on ("click", function () {
	var country_tree = "'(((((((RU:1.071429,DE:1.071429):0.161361,(((NL:0.142857,DE:0.142857):0.142857,DE:0.285714):0.417776,DE:0.703490):0.529300):0.119204,(((US:0.428571,US:0.428571):0.230935,CA:0.659507):0.253306,US:0.912813):0.439181):0.140503,((((((((((DE:0.071429,DE:0.071429):0.035714,DE:0.107143):0.007199,DE:0.114342):0.001730,DE:0.116071):0.041196,(DE:0.071429,DE:0.071429):0.085839):0.026489,(DE:0.142857,DE:0.142857):0.040899):0.094379,((DE:0.071429,DE:0.071429):0.107143,DE:0.178571):0.099563):0.073989,DE:0.352124):0.177630,DE:0.529754):0.016485,DE:0.546238):0.946257):0.503005,FR:1.995501):0.721331,((((((((DE:0.071429,DE:0.071429):0.071429,(DE:0.071429,DE:0.071429):0.071429):-0.008039,((DE:0.071429,DE:0.071429):0.035714,DE:0.107143):0.027676):0.148795,CH:0.283614):0.094377,(SK:0.214286,DE:0.214286):0.163705):0.007705,DE:0.385696):0.292494,(AT:0.214286,IT:0.214286):0.463905):0.353721,(DE:0.500000,DE:0.500000):0.531912):1.684920):0.479510,(DE:1.000000,DE:1.000000):2.196341);'";
	var res = d3.layout.newick_parser(country_tree);
	default_tree_settings();
	tree(res).svg(d3.select("#tree_display")).layout();
});

$("#Host").on ("click", function () {
	default_tree()
});

default_tree_settings();

tree(example_tree).svg(d3.select("#tree_display")).layout();

$("#branch_filter").on ("input propertychange", function (e) {
   var filter_value = $(this).val();

   var rx = new RegExp (filter_value,"i");

  tree.modify_selection (function (n) {
    return filter_value.length && (tree.branch_name () (n.target).search (rx)) != -1;
   },"tag");

});

});
