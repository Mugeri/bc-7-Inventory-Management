// function demoDisplay(adiv){
//   if (adiv =='assets'){
//   	div.getElementById('assets').style.display = block;	
//   }
    
function Confirmer(user) {
    if (confirm("Change user level")){
    	alert('name is %r' % user);
    };
}
$(document).ready(function(){
    $("#assets").click(function(){
    alert("The paragraph was clicked.");
});
});