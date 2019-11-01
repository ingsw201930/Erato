// Load an image and put it as a src in output.
var loadImage = function(event) {
  var output = document.getElementById('output');
  output.src = URL.createObjectURL(event.target.files[0]);
};

// Load a file and show a message.
var loadFile = function(event) {
  var output = document.getElementById('output');
  output.chasuccesfully_uploaded_file;
  document.getElementById('succesfully_uploaded_file').style.display = "block";
};
