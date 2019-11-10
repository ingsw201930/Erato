// Load a file and show a message.
var show_inputs = function(event) {
  console.log("in inputs");
  $('#standard_calendar').calendar();

  document.getElementById('button_edit').style.display = "none";
  document.getElementById('button_delete').style.display = "none";
  document.getElementById('button_save').style.display = "block";

  var x = document.getElementsByClassName("showable");
  var i;
  for (i = 0; i < x.length; i++) {
  x[i].style.display = "block";
  }
  var x = document.getElementsByClassName("hidable");
  var i;
  for (i = 0; i < x.length; i++) {
  x[i].style.display = "none";
  }

};

var hide_hidable = function(){
  console.log("Hiding");
  var x = document.getElementsByClassName("showable");
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
}
