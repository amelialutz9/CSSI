function moveText() {
  var input_text = $('input').val();
  alert("You typed: "+input_text);
  $('#result').text(input_text);
  $('input').val("");
}


function stuffToDoOnLoad() {
  $("#go-btn").click(moveText);
}

$(document).ready(stuffToDoOnLoad);
