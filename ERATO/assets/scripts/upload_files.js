var loadImage = function(event) {
  var output = document.getElementById('output');
  output.src = URL.createObjectURL(event.target.files[0]);
};

var loadFile = function(event) {
  var output = document.getElementById('output');
  output.chasuccesfully_uploaded_file;
  document.getElementById('succesfully_uploaded_file').style.display = "block";
};
