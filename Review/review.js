var count1=0;
var count2=0;
var count3=0;
var count4=0;


function update1(){
  count1++;
  alert("You voted for pose 1!");
  $("#dog1Num").text(count1+"");
}

function update2(){
  count2++;
  alert("You voted for pose 2!");
  $("#dog2Num").text(count2+"");
}

function update3(){
  count3++;
  alert("You voted for pose 3!");
  $("#dog3Num").text(count3+"");
}

function update4(){
  count4++;
  alert("You voted for pose 4!");
  $("#dog4Num").text(count4+"");
}

$(document).ready(function(){
  $("#dog1 img").click(update1);
  $("#dog2 img").click(update2);
  $("#dog3 img").click(update3);
  $("#dog4 img").click(update4);
});
