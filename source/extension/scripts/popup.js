var modal = document.getElementById("modal");

var btn = document.getElementById("play");

btn.onclick = function () {
  modal.style.display = "block";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

function main_window() {
  var myWindow = window.open("main.html", "", "width=400,height=500");
}

document.getElementById("main_window").addEventListener("click", main_window);
