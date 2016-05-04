// function demoDisplay(adiv){
//   if (adiv =='assets'){
//   	div.getElementById('assets').style.display = block;	
//   }
    
// function Confirmer(user) {
//     if (confirm("Change user level")){
//     	alert('name is %r' % user);
//     };
// }
// $(document).ready(function(){
//     $("#assets").click(function(){
//     alert("The paragraph was clicked.");
// });
// });
$(function(){
    $("#assets").hide();
    $("#previewU").on("click", function(){
        $("#assets, #users").toggle();
    });
    $("#previewA").on("click", function(){
        $("#assets, #users").toggle();
    });
});

function change(){
	document.getElementById('assets').style.display = block;
	document.getElementById('users').style.display = none;
}
function changeagain(){
	document.getElementById('assets').style.display = none;
	document.getElementById('users').style.display = block;
}