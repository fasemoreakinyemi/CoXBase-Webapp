$(document).ready(function()
{

callIframe("https://www.ncbi.nlm.nih.gov/projects/sviewer/embedded_iframe.html?iframe=sviframe&id=NC_002971.4&amp;v=1k:20000&amp;mk=1500:1700|TestMarker|00ff00'")

function callIframe(url) {
    $("#seqviewerContainer").append('<iframe id="seqviewerPanel">');
    $('iframe#seqviewerPanel').attr('src', url);
}
$('body').on('change', 'select#seqviewer', function() {
var key = ($("#seqviewer option:selected").val());
var orghref =  "https://www.ncbi.nlm.nih.gov/projects/sviewer/embedded_iframe.html?iframe=svifram&amp;v=1k:20000&amp;mk=1500:1700|TestMarker|00ff00'e&id=" + key
    $('iframe#seqviewerPanel').attr('src', orghref);
});

 $('.js-example-basic-single').select2();
//SeqViewOnReady(function() {

//var app = new SeqView.App("seqviewerPanel")
//app.load("?embedded=minimal&appname=testapp1&id=NC_002971.4")
//$('body').on('change', 'select#seqviewer', function() {
//var key = ($("#seqviewer option:selected").val());
//var embed_code =  "?embedded=true&appname=testapp1&id=" + key
//app.reload(embed_code

//})
//})


})


