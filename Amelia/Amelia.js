var see=true;
var side=true;
var date;

function disappear() {
  if (see==true){
    $("img#hide-img").hide();
    see=false;
    alert("images hidden!");
  }
  else {
    $("img#hide-img").show();
    see=true;
    alert("images shown!");
  }
  return see;
}

function move() {
  if (see==true){
    $(".section").animate(
      {marginLeft: "300px"},  // Final CSS states
      1000  // Milliseconds of animation
    );
    see=false;
  }
  else{
    (".section").animate(
      {marginLeft: "0px"},  // Final CSS states
      1000  // Milliseconds of animation
    );
    see=true;
  }

}

function change(){
  inside = document.getElementById("welcome").innerText;
  document.getElementById("welcome").innerText="Welcome, "+name+"!";
}

function setDate(){
  date=Date();
  document.getElementById("date").innerText=date;
}

function toggleProf(){
  $("#prof-pic").toggle();
}


alert("Welcome!");
var name=prompt("What is your name?");
$(document).ready(function() {
    setDate();
    $("#disappear-btn").click(disappear);
    $(".heading").click(move);
    $("#prof-pic").fadeOut(3000);
    change();
    $("div#show").click(toggleProf);
  }
)
