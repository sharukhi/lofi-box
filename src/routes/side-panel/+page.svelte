<script lang="ts">
	//@ts-nocheck
	import 'iconify-icon';

	const playlist = [
		{
			audio: `https://boxradio-edge-02.streamafrica.net/lofi`
		}
	];

	let playingState = 'paused';
	let songPlayingIndex = 0;
	let song = null;

	function togglePlaying() {
		playingState === 'paused' ? play() : pause();
	}

	function loadSong() {
		song = new Audio(playlist[songPlayingIndex].audio);
		song.volume = 0.2;
		song.play();
	}

	function play() {
		if (playingState === 'playing') {
			pause();
		}

		playingState = 'playing';
		loadSong();
	}

	function playSelectedSong(event) {
		const songIndex = +event.target.dataset.index;

		if (songIndex === songPlayingIndex) {
			songPlayingIndex = null;
			return pause();
		}

		songPlayingIndex = songIndex;
		play();
	}

	function pause() {
		playingState = 'paused';
		song.pause();
	}
</script>

<div class="h-screen bg-cover bg-center" style="background-image: url('/bg.gif');">
	<div class="flex h-screen items-center justify-center">
		<div>
			<button
				on:click={togglePlaying}
				class="text-md h-10 w-10 rounded-full bg-[#0B3220] text-lg"
				style="  font-size: 30px;
  					align-items: center;
  					text-align: center;
  					vertical-align: middle;
					}"
			>
				{#if playingState === 'paused'}
					<iconify-icon icon="solar:play-line-duotone" style="color: white"></iconify-icon>
				{:else}
					<iconify-icon icon="solar:pause-linear" style="color: white"></iconify-icon>
				{/if}
			</button>
		</div>
	</div>
</div>
