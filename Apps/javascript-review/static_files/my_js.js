function stuffToDoWhenFadeOutIsDone() {
  alert("done fading out");
}

function stuffToDoWhenClicked() {
  $("#emoji").fadeOut(1000);
}

function stuffToDoWhenReady(){
  $("#hello").fadeOut(1000, stuffToDoWhenFadeOutIsDone);
  // $("#emoji").click(stuffToDoWhenClicked);
  $("#emoji").click(function(){
    $("#emoji").fadeOut(1000);
  })
}

$(document).ready(stuffToDoWhenReady);
