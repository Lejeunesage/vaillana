<template>
  <div class="bgImage">
    <div class="py-8 min-h-screen bg-[#eeeeeedf]">
      <div class="mx-4">
          <section class=" bg-[#9747ff2c] rounded-xl p-4">
            <div class="flex justify-center pt-4">
              <img
                src="/public/assets/img/ressources/mascotte.png"
                alt=""
                class="object-contain w-20"
              />
            </div>
            <div>
              <h1 class="font-Komikula text-center text-3xl py-2 font-bold">
                <span class="text-[#9747FF]">Panda</span>, votre assistant
                générateur de site web
              </h1>
              <p class="font-JakartaSans text-center text-sm">
                Je vous assiste dans la génération de votre site web. Alors
                dites-moi clairement, ce que vous voulez.
              </p>
            </div>
          </section>
          <section>
            <div class="flex justify-center pt-4">
              <img
                src="/public/assets/img/ressources/icone.png"
                alt=""
                class="w-20"
              />
            </div>
            <!-- Section du chat -->
            <section class="font-JakartaSans ">
              <div class="flex justify-start items-start flex-col text-white mr-16">
                <p class="panda " v-for="(question, index) in pandaQuestions.slice(0, 3)" :key="index" v-html="question.question"></p>
              </div>
              <div class="flex justify-end items-end flex-col ml-28">
                  <p class="user" v-for="(response, index) in userResponses.slice(0, 1)" :key="index">{{response.response}} <span class="transition-all delay-1000"> <input type="text" name="" id="" class="bg-transparent border-0 border-b-2 border-gray-300 appearance-none text-black border-gray-600 focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"></span></p>
              </div>
            </section>
          </section>
      </div>
    </div>
  </div>
</template>



<script setup>
    let pandaQuestions = [
        {
            id : 1,
            question : "Bonjour, je suis <span class='italic font-bold'>Panda</span> !",   
        },
        {
            id : 2,
            question : "Je vais t’aider à générer ton site.",   
        },
        {
            id : 3,
            question : "Alors, veux-tu bien m’en dire plus ?",   
        },
        {
            id : 4,
            question : "Bien reçu !",   
        },
        {
            id : 5,
            question : "Votre site est en cours de génération...",   
        },
        {
            id : 6,
            question : "Ton site est prêt ! ",   
        },
        {
            id : 7,
            question : "Sur quelle adresse veux-tu le recevoir ?",   
        },
        {
            id : 8,
            question : "Super ! ",   
        },
        {
            id : 7,
            question : "Veuille prévisualiser ton site web ici.",   
        },
    ]
    let userResponses = [
        {
            id : 1,
            response : "Bonjour Panda. Je m'appelle",   
        },
        
    ]
</script>





<style scoped>
.bgImage {
  background-image: url("/public/assets/img/ressources/mascotte_pandagouin.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  background-attachment: fixed;
}
.panda {
  background: linear-gradient(to right, #0398c7 0%, #9747ff 100%);
  width: fit-content;
  border-radius: 50px;
  padding-inline: 1rem;
  margin-top: 0.5rem;
}

.user {
  background: white;
  width: fit-content;
  border-radius: 50px;
  padding-inline: 1rem;
  padding-block: 0.7rem;
  margin-top: 0.5rem;
}
</style>
