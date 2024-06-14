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
