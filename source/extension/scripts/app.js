const musicContainer = document.getElementById("music");
const playBtn = document.getElementById("play");

function loadSong(song) {
  audio.src = `https://boxradio-edge-02.streamafrica.net/lofi`;
}

function playSong() {
  musicContainer.classList.add("play");
  playBtn.querySelector("i.fas").classList.add("fa-pause");
  playBtn.querySelector("i.fas").classList.remove("fa-play");

  audio.play();
}

function pauseSong() {
  musicContainer.classList.remove("play");
  playBtn.querySelector("i.fas").classList.add("fa-play");
  playBtn.querySelector("i.fas").classList.remove("fa-pause");

  audio.pause();
}

playBtn.addEventListener("click", () => {
  const isPlaying = musicContainer.classList.contains("play");

  if (isPlaying) {
    pauseSong();
  } else {
    playSong();
  }
});

var modal = document.getElementById("settings-modal");

var btn = document.getElementById("settings");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

document.addEventListener("DOMContentLoaded", function () {
  fetch("../manifest.json")
    .then((response) => response.json())
    .then((data) => {
      const dataDisplay = document.getElementById("version");

      const versionElement = document.createElement("p");
      versionElement.textContent = "version: " + data.version;

      dataDisplay.appendChild(versionElement);
    })
    .catch((error) => console.error("Error fetching JSON data:", error));
});
