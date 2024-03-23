<script setup>

</script>

<template>
  <main class="lg:max-w-5xl xl:max-w-6xl mx-auto">
    <section class="relative overflow-hidden">
      <div class="bg-white py-6 text-center md:flex md:pl-10">
        <!-- Section du texte -->
        <section class="flex justify-center flex-col">
          <h1 class="text-5xl md:text-6xl text-gradient font-Ballsye leading-tight">
            VAILLANA
          </h1>
          <div class="flex flex-col gap-10 justify-center">
            <p class="uppercase font-Komikula font-bold md:text-2xl">Votre <span class="text-[#0398C7]">site web</span> en
              un clic,
              tout-en-un. simple, efficace, abordable.</p>
            <RouterLink class="hidden md:block" to="/chatbot">
              <span
                class="bg-gradient w-fit text-white font-Acumin text-center p-2 px-4 rounded-full uppercase font-bold bg-white">Commencer</span>
            </RouterLink>
          </div>
        </section>
        <div>
          <!-- Section d'ajout d'image -->
          <img src="../../public/assets/img/ressources/pinchot.png" width="70%" class="mx-auto my-8 md:m-0" />
          <div class="md:hidden">
            <RouterLink to="/chatbot">
              <span
                class="bg-gradient w-fit text-white font-Acumin text-center p-1 px-3 rounded-full uppercase font-bold bg-white">Commencer</span>
            </RouterLink>
          </div>
        </div>
        <div class="hidden md:block w-[150px] md:w-[210px] h-[150px] md:h-[210px] bg-[#F8F8F8] absolute right-[-7%] top-[-10%] rounded-full"></div>
        <div class="w-[150px] md:w-[210px] h-[150px] md:h-[210px] bg-[#F8F8F8] absolute left-[-7%] bottom-[-10%] rounded-full"></div>
      </div>
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


