// $(function(){
//     $("#assets").hide();
//     $("#previewU").on("click", function(){
//         $("#assets, #users").toggle();
//     });
//     $("#previewA").on("click", function(){
//         $("#assets, #users").toggle();
//     });
// });
$(function(){
     $("#assets").hide();
     $("#assigned").hide();
 });
$(function(){
     $("#assetsu").hide();
     
 });
function showAssigned(){
	document.getElementById('assigned').style.display = "block";
	document.getElementById('users').style.display = "none";
	document.getElementById('assets').style.display = "none";
}
function showUsers(){
	document.getElementById('assigned').style.display = "none";
	document.getElementById('users').style.display = "block";
	document.getElementById('assets').style.display = "none";
}
function showAssets(){
	document.getElementById('assigned').style.display = "none";
	document.getElementById('users').style.display = "none";
	document.getElementById('assets').style.display = "block";
}
// $('.reclaim').click(function(){             
//         var assigned_id = $(this).data('name');
//         if (confirm("Do you want to reclaim?")){
//         	$.ajax({
//             url_for: '/reclaim',
//             type: 'POST',
//         })
//         }
// });