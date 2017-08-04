var name;
var inside;

function alerting() {
  alert("my alert");
}

function change(){
  inside = document.getElementById("welcome").innerText;
  document.getElementById("welcome").innerText="Welcome, "+name+"!";
}

alerting();
name=prompt("Name?");
$(document).ready(function(){
  change();
}) ;
