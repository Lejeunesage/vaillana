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
        <div
          class="hidden md:block w-[150px] md:w-[210px] h-[150px] md:h-[210px] bg-[#F8F8F8] absolute right-[-7%] top-[-10%] rounded-full">
        </div>
        <div
          class="w-[150px] md:w-[210px] h-[150px] md:h-[210px] bg-[#F8F8F8] absolute left-[-7%] bottom-[-10%] rounded-full">
        </div>
      </div>
    </section>

    <hr class="h-1 bg-gradient" />

    <article class="my-8 flex justify-center flex-col gap-4">
      <p class="text-3xl md:text-4xl text-center w-[80vw] mx-auto font-Komikula font-bold leading-tight uppercase mb-8">
        Construisez votre site en quelques clics
      </p>
      <div class="flex flex-col gap-12 md:gap-16">
        <section class="flex gap-8 md:gap-10 flex-col md:flex-row md:w-[60vw] mx-auto md:mt-[4rem] justify-center">
          <div class="flex justify-center flex-col gap-4 w-[80vw] mx-auto">
            <span class="text-[#9747FF] text-4xl md:text-6xl font-Komikula font-bold text-center">01</span>
            <p class="text-justify md:text-right font-semibold">Notre plateforme facilite la création de votre site web. Pas besoin de compétences techniques, notre interface intuitive vous guide à chaque étape. Avec des modèles personnalisables et des outils conviviaux, concrétisez votre vision rapidement.</p>
          </div>
          <img src="../../public/assets/img/ressources/icone.png" class="mx-auto md:m-0 w-[70%] md:w-[100%]" />
        </section>
        <section class="flex gap-8 md:gap-10 flex-col md:flex-row md:w-[60vw] mx-auto md:mt-[4rem] justify-center">
          <img src="../../public/assets/img/ressources/icone.png" class="mx-auto md:m-0 w-[70%] md:w-[100%]" />
          <div class="flex justify-center flex-col gap-4 w-[80vw] mx-auto">
            <span class="text-[#9747FF] text-4xl md:text-6xl font-Komikula font-bold text-center">02</span>
            <p class="text-justify md:text-left font-semibold">Notre plateforme facilite la création de votre site web. Pas besoin de compétences techniques, notre interface intuitive vous guide à chaque étape. Avec des modèles personnalisables et des outils conviviaux, concrétisez votre vision rapidement.</p>
          </div>
        </section>
        <section class="flex gap-8 md:gap-10 flex-col md:flex-row md:w-[60vw] mx-auto md:mt-[4rem] justify-center">
          <div class="flex justify-center flex-col gap-4 w-[80vw] mx-auto">
            <span class="text-[#9747FF] text-4xl md:text-6xl font-Komikula font-bold text-center">03</span>
            <p class="text-justify md:text-right font-semibold">Notre plateforme facilite la création de votre site web. Pas besoin de compétences techniques, notre interface intuitive vous guide à chaque étape. Avec des modèles personnalisables et des outils conviviaux, concrétisez votre vision rapidement.</p>
          </div>
          <img src="../../public/assets/img/ressources/icone.png" class="mx-auto md:m-0 w-[70%] md:w-[100%]" />
        </section>
      </div>
    </article>

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


