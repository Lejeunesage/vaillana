<script setup>

</script>

<template>
  <main class="lg:max-w-5xl xl:max-w-6xl mx-auto">
    <section class="bg-white py-6 text-center">

      <!-- Section du texte -->
      <section class="flex justify-center flex-col">
        <h1 class="text-5xl text-gradient font-Ballsye leading-tight">
          VAILLANA
        </h1>
        <div class="flex flex-col gap-10 justify-center">
          <p class="uppercase font-Komikula font-bold">Votre <span class="text-[#0398C7]">site web</span> en un clic,
            tout-en-un. simple, efficace, abordable.</p>
          <RouterLink to="/commencer">
            <span
              class="bg-gradient w-fit text-white font-Acumin text-center p-1 px-2 rounded-full uppercase font-bold bg-white">Commencer</span>
          </RouterLink>
        </div>
      </section>
      <!-- Section d'ajout d'image -->
      <!-- <img src="../" /> -->

    </section>
    <hr class="h-1 bg-gradient" />
    <section class="bg-blue-500 my-12">
      Section 2
    </section>

  </main>
</template>

<style scoped>
.bg-gradient {
  background: linear-gradient(to right, #0398C7 0%, #9747FF 100%);
}

.text-gradient {
  background-image: linear-gradient(to right, #0398C7 0%, #9747FF 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
</style>


