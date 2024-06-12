<template>
  <header class="py-12 px-4 sm:px-6 lg:px-8">
    <div class="relative mx-auto max-w-[37.5rem] pt-20 text-center pb-20">
      <div class="flex items-center justify-center space-x-3">
        <img loading="lazy" src="/icon.png" alt="Logspot" class="h-20 w-20 rounded-full border-2 border-slate-600 border-opacity-20" />
        <h1 class="text-4xl font-extrabold tracking-tight text-slate-700 sm:text-5xl">
          Lofi-Box
        </h1>
      </div>
      <p class="mt-4 text-lg leading-7 text-slate-600">
        ✨ Relaxing lo-fi tunes directly within your web browser.
      </p>
      <div class="grid grid-cols-1 gap-0 sm:grid-cols-1 lg:grid-cols-2 md:grid-cols-2 lg:mx-[115px] md:mx-[115px] sm:mx-[115px] mx-0 place-items-center my-5">
      <div class="mb-2">
        <a href="https://chromewebstore.google.com/detail/lofi-box/fbogegnhfhlbdjjhompihcgcenhdclhj">
          <img class="h-12"src="/chrome.svg">
        </a>
      </div> 
      <div class="mb-2">
        <a href="https://addons.mozilla.org/en-US/firefox/addon/lofi-box/">
          <img class="h-12" src="/firefox.svg">
        </a>
      </div>
    </div>
    </div>
  </header>
</template>

<script setup></script>

<style scoped>
.form-input {
  @apply block h-10 w-full rounded-md bg-white pr-3 pl-12 text-slate-900 shadow-md shadow-black/5 ring-1 ring-slate-900/5 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-primary sm:text-sm sm:leading-6;
}
.form-submit {
  @apply inline-flex justify-center rounded-lg text-sm font-semibold py-2.5 px-4 bg-slate-900 text-white hover:bg-slate-700 ml-4 flex-none;
}
</style>
