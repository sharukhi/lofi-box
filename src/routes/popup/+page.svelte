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

<body>
	<nav class="fixed inset-x-0 top-0 z-50">
		<div class="px-4 md:px-6">
			<div class="flex h-14 items-center">
				<div class="mr-auto">
					<div class="black mx-1 mt-1 grid grid-cols-1 gap-2 text-left">
						<div>
							<a href="https://github.com/sharukhi/lofi-box/" target="_blank">
								<button class="btn btn-square btn-xs opacity-65 hover:opacity-100"
									><iconify-icon icon="lucide:github" style="color: #383404"></iconify-icon></button
								>
							</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</nav>
	<div class=" bg-cover bg-center" style="background-image: url('/bg-img.gif');">
		<div class="flex h-screen items-center justify-center">
			<div>
				<button
					on:click={togglePlaying}
					class="h-10 w-10 rounded-full"
					style="
  					align-items: center;
  					text-align: center;
  					vertical-align: middle;
					}"
				>
					{#if playingState === 'paused'}
						<button class="btn btn-circle"
							><iconify-icon icon="lucide:play" class="text-[23px]" style="color: #383404"
							></iconify-icon></button
						>
					{:else}
						<button class="btn btn-circle"
							><iconify-icon icon="lucide:pause" class="text-[23px]" style="color: #383404"
							></iconify-icon></button
						>
					{/if}
				</button>
			</div>
		</div>
	</div>
</body>
