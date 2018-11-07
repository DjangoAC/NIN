$(document).ready(function() {
 $(".login").on("click", function() {
    $("#login")
      .modal()
      .addClass("animated shake");
  
});
 $('#submit').on('click', function(){
 	var value = $('#text').val();
 		$('.render').append('<p>', value,'</p>','<hr>', '<br>'); });


  
});
