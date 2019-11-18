// Load an image and put it as a src in output.
var loadImage = function(event) {
  var output = document.getElementById('output');
  output.src = URL.createObjectURL(event.target.files[0]);
};

// Load a file and show a message.
var loadFile = function(event) {
  document.getElementById('succesfully_uploaded_file').style.display = "block";
  var save_button = document.getElementById('save_button')
  if (save_button !== null){
    save_button.style.display= "block";
  }
};
