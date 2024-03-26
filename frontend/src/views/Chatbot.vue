<template>
  <div class="bgImage ">
    <div class="py-8  bg-[#eeeeeedf]">
      <div class="mx-4">
        <section class="bg-[#9747ff2c] rounded-xl p-4">
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
        <section class="lg:max-w-5xl xl:max-w-6xl mx-auto">
          <div class="flex justify-center pt-4">
            <img
              src="/public/assets/img/ressources/icone.png"
              alt=""
              class="w-20"
            />
          </div>
          <!-- Section du chat -->
          <section class="" style="font-family: 'Poppins';">
             <!-- Première question -->
              <p
                class="panda text-white"
                v-for="(question, index) in pandaQuestions.slice(0, 3)"
                :key="index"
                v-if="firstQuestion"
                :style="{ transitionDelay: `${index * 1500}ms` }"
                v-html="question.question"
              ></p>

            <!-- Première réponse de l'utilisateur -->
            <div class="flex justify-end items-end flex-col ml-16" v-if="userAnswer">
              <form action=""  @submit.prevent="sendMessage()">
                <p
                  class="user"
                  v-for="(response, index) in userResponses.slice(0, 1)"
                  :key="index"
                >
                  <span v-if="firstAnswer">{{ response.response1 }}</span>
                  <span class="transition-all" v-if="inputName">
                    <input
                      type="text"
                      name="fullName"
                      v-model = "fullName"
                      id=""
                      class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                  >
                  <span v-if="secondAnswer">{{ response.response2 }}</span
                  >
                  <span class="transition-all delay-1000" v-if="selectName">
                    <select
                      id="countries"
                      v-model = "categorie"
                      class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer"
                    >
                      <option selected disabled></option>
                      <option
                        :value="cat.category"
                        v-for="(cat, catIndex) in categories"
                      >
                        {{ cat.category }}
                      </option>
                    </select>
                  </span>

                  <span v-if="thirdAnswer">{{ response.response3 }}</span>

                  <span class="transition-all delay-1000" v-if="fourthAnswer">
                    <input
                      type="text"
                      name="siteName"
                      v-model = "siteName"
                      id=""
                      class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                  >

                  <span v-if="fithAnswer">{{ response.response4 }}</span>

                  <div class="grid grid-cols-4 gap-1 my-2 justify-center" v-if="sixAnswer">
                    <div
                      v-for = "palette in palettes"
                      :key="palette.id"
                      class="flex z-40 cursor-pointer w-full rounded-lg border-2 border-transparent"
                      @click="getColors(palette)"
                      :class="{ 'palette-selectionnee': palette.id === paletteSelectionneeId }"
                    >
                      <div
                        class="w-[34%] h-10 rounded-s-lg"
                        :style="{ backgroundColor: palette.couleur1 }"
                      ></div>
                      <div
                        class="w-[34%] h-10"
                        :style="{ backgroundColor: palette.couleur2 }"
                      ></div>
                      <div
                        class="w-[33%] h-10 rounded-e-lg"
                        :style="{ backgroundColor: palette.couleur3 }"
                      ></div>
                    </div>
                  </div>

                  <div class="flex justify-center" v-if="submitAnswer">
                    <button type="submit" class="relative inline-flex items-center justify-center p-4 px-5 py-3 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
                        <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
                        <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
                        <span class="relative text-white">Soumettre</span>
                    </button>
                  </div>

                </p>
              </form>
            </div>
            
            <!-- Deuxième question -->
            <p
                class="panda text-white"
                v-for="(question, index) in pandaQuestions.slice(3, 5)"
                :key="index"
                v-if="secondQuestion"
                v-html="question.question"
            ></p>

            <!-- Loader -->
            <div class="flex justify-center my-4" v-if="loader"><span class="loader"></span></div>

            <!-- Troisième question -->
            <p
                class="panda text-white"
                v-for="(question, index) in pandaQuestions.slice(5, 7)"
                :key="index"
                v-if="thirdQuestion"
                v-html="question.question"
            ></p>

             <!-- Deuxième réponse de l'utilisateur -->
            <div class="flex justify-end items-end flex-col ml-16" v-if="isUserEmail">
              <form action=""  @submit.prevent="sendMessage()">
                <p
                  class="user"
                  v-for="(response, index) in userResponses.slice(1, 2)"
                  :key="index"
                >
                  {{ response.response1 }}
                  <span class="flex items-center">
                    <span class="transition-all delay-1000">
                      <input
                        type="text"
                        name="fullName"
                        v-model = "email"
                        id=""
                        class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                    >
                    <span>
                      <svg width="30px" height="30px"  viewBox="0 -0.5 25 25" fill="none" xmlns="http://www.w3.org/2000/svg" >
                    <path d="M19.1168 12.1484C19.474 12.3581 19.9336 12.2384 20.1432 11.8811C20.3528 11.5238 20.2331 11.0643 19.8758 10.8547L19.1168 12.1484ZM6.94331 4.13656L6.55624 4.77902L6.56378 4.78344L6.94331 4.13656ZM5.92408 4.1598L5.50816 3.5357L5.50816 3.5357L5.92408 4.1598ZM5.51031 5.09156L4.76841 5.20151C4.77575 5.25101 4.78802 5.29965 4.80505 5.34671L5.51031 5.09156ZM7.12405 11.7567C7.26496 12.1462 7.69495 12.3477 8.08446 12.2068C8.47397 12.0659 8.67549 11.6359 8.53458 11.2464L7.12405 11.7567ZM19.8758 12.1484C20.2331 11.9388 20.3528 11.4793 20.1432 11.122C19.9336 10.7648 19.474 10.6451 19.1168 10.8547L19.8758 12.1484ZM6.94331 18.8666L6.56375 18.2196L6.55627 18.2241L6.94331 18.8666ZM5.92408 18.8433L5.50815 19.4674H5.50815L5.92408 18.8433ZM5.51031 17.9116L4.80505 17.6564C4.78802 17.7035 4.77575 17.7521 4.76841 17.8016L5.51031 17.9116ZM8.53458 11.7567C8.67549 11.3672 8.47397 10.9372 8.08446 10.7963C7.69495 10.6554 7.26496 10.8569 7.12405 11.2464L8.53458 11.7567ZM19.4963 12.2516C19.9105 12.2516 20.2463 11.9158 20.2463 11.5016C20.2463 11.0873 19.9105 10.7516 19.4963 10.7516V12.2516ZM7.82931 10.7516C7.4151 10.7516 7.07931 11.0873 7.07931 11.5016C7.07931 11.9158 7.4151 12.2516 7.82931 12.2516V10.7516ZM19.8758 10.8547L7.32284 3.48968L6.56378 4.78344L19.1168 12.1484L19.8758 10.8547ZM7.33035 3.49414C6.76609 3.15419 6.05633 3.17038 5.50816 3.5357L6.34 4.78391C6.40506 4.74055 6.4893 4.73863 6.55627 4.77898L7.33035 3.49414ZM5.50816 3.5357C4.95998 3.90102 4.67184 4.54987 4.76841 5.20151L6.25221 4.98161C6.24075 4.90427 6.27494 4.82727 6.34 4.78391L5.50816 3.5357ZM4.80505 5.34671L7.12405 11.7567L8.53458 11.2464L6.21558 4.83641L4.80505 5.34671ZM19.1168 10.8547L6.56378 18.2197L7.32284 19.5134L19.8758 12.1484L19.1168 10.8547ZM6.55627 18.2241C6.4893 18.2645 6.40506 18.2626 6.34 18.2192L5.50815 19.4674C6.05633 19.8327 6.76609 19.8489 7.33035 19.509L6.55627 18.2241ZM6.34 18.2192C6.27494 18.1759 6.24075 18.0988 6.25221 18.0215L4.76841 17.8016C4.67184 18.4532 4.95998 19.1021 5.50815 19.4674L6.34 18.2192ZM6.21558 18.1667L8.53458 11.7567L7.12405 11.2464L4.80505 17.6564L6.21558 18.1667ZM19.4963 10.7516H7.82931V12.2516H19.4963V10.7516Z" fill="#9747ff"/>
                    </svg>
                    </span>
                  </span>
                </p>
              </form>
            </div>

            <!-- Quatrième question -->
             <p
                class="panda text-white"
                v-for="(question, index) in pandaQuestions.slice(7, 9)"
                :key="index"
                v-if="fourthQuestion"
                v-html="question.question"
            ></p>


          </section>
        </section>
        <div class="flex justify-center mt-8" v-if="preview">
          <button type="submit" class="relative inline-flex items-center justify-center p-4 px-5 py-3 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
              <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
              <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
              <span class="relative text-white font-Acumin uppercase">Prévisualiser mon site</span>
          </button>
        </div>
      </div> 
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

let paletteSelectionneeId = ref(null);
let rgbaToHex = (rgba) => {
  const [r, g, b] = rgba.match(/\d+/g);
  return `#${Number(r).toString(16)}${Number(g).toString(16)}${Number(
    b
  ).toString(16)}`;
};

/**
 * Les varaibles 
 */

let fullName = ref("");
let email = ref("");
let siteName = ref("");
let categrorie = ref("");
let colors = ref([]);

let data = {
  fullName : fullName.value,
  email : email.value,
  siteName : siteName.value,
  categrorie : categrorie.value,
  palettes : colors.value,
}

let sendMessage = () => {
  data.fullName = fullName.value
  data.email = email.value
  data.siteName = siteName.value
  data.categrorie = categrorie.value
  data.palettes = colors.value
  console.log(data);
};

let getColors = (palette) => {
  paletteSelectionneeId.value = palette.id;
  colors.value.push(palette.couleur1)
  colors.value.push(palette.couleur2)
  colors.value.push(palette.couleur3)

  return colors.value;
};

let pandaQuestions = [
  {
    id: 1,
    question: "Bonjour, je suis <span class='italic font-bold'>Panda</span> !",
  },
  {
    id: 2,
    question: "Je vais t’aider à générer ton site.",
  },
  {
    id: 3,
    question: "Alors, veux-tu bien m’en dire plus ?",
  },
  {
    id: 4,
    question: "Bien reçu !",
  },
  {
    id: 5,
    question: "Votre site est en cours de génération...",
  },
  {
    id: 6,
    question: "Ton site est prêt ! ",
  },
  {
    id: 7,
    question: "Sur quelle adresse veux-tu le recevoir ?",
  },
  {
    id: 8,
    question: "Super ! ",
  },
  {
    id: 7,
    question: "Veuille prévisualiser ton site web ici.",
  },
];
let userResponses = [
  {
    id: 1,
    response1: "Bonjour Panda. Je m'appelle",
    response2: ". Je veux un site web dans le domaine de ",
    response3: ". Le nom de mon entreprise est  ",
    response4: " et je voudrais les palettes de couleur ",
  },
  {
    id: 2,
    response1: "Je voudrais le recevoir sur l'adresse email ",
    
  },
];

let categories = [
  {
    id: 1,
    category: "Développement Web",
  },
  {
    id: 2,
    category: "Développement personnel",
  },
  {
    id: 3,
    category: "Culture générale",
  },
  {
    id: 4,
    category: "Mathématique",
  },
  {
    id: 5,
    category: "Web Design",
  },
];

let palettes = [
  {
    id: 1,
    couleur1: "#f72585",
    couleur2: "#f2f0f5",
    couleur3: "#7209b7",
  },
  {
    id: 2,
    couleur1: "#228B22",
    couleur2: "#f2f0f5",
    couleur3: "#00471B",
  },
  {
    id: 3,
    couleur1: "#FFD700",
    couleur2: "#f2f0f5",
    couleur3: "#FF9800",
  },
  {
    id: 4,
    couleur1: "#7CFC00",
    couleur2: "#f2f0f5",
    couleur3: "#006400",
  },
  {
    id: 5,
    couleur1: "#4682B4",
    couleur2: "#f2f0f5",
    couleur3: "#000080",
  },
  {
    id: 6,
    couleur1: "#800080",
    couleur2: "#f2f0f5",
    couleur3: "#4B0082",
  },
  {
    id: 7,
    couleur1: "#FFFF00",
    couleur2: "#f2f0f5",
    couleur3: "#BDB76B",
  },
  {
    id: 8,
    couleur1: "#8A2BE2",
    couleur2: "#f2f0f5",
    couleur3: "#9932CC",
  },
  {
    id: 9,
    couleur1: "#00BFFF",
    couleur2: "#f2f0f5",
    couleur3: "#1E90FF",
  },
  {
    id: 10,
    couleur1: "#008080",
    couleur2: "#f2f0f5",
    couleur3: "#20B2AA",
  },
  {
    id: 11,
    couleur1: "#FF1493",
    couleur2: "#f2f0f5",
    couleur3: "#FF69B4",
  },
  {
    id: 12,
    couleur1: "#ADFF2F",
    couleur2: "#f2f0f5",
    couleur3: "#32CD32",
  },
  {
    id: 13,
    couleur1: "#FF6347",
    couleur2: "#f2f0f5",
    couleur3: "#DC143C",
  },
  {
    id: 14,
    couleur1: "#00FFFF",
    couleur2: "#f2f0f5",
    couleur3: "#87CEEB",
  },
  {
    id: 15,
    couleur1: "#40E0D0",
    couleur2: "#f2f0f5",
    couleur3: "#7FFFD4",
  },
  {
    id: 16,
    couleur1: "#FFDAB9",
    couleur2: "#f2f0f5",
    couleur3: "#FFA07A",
  },
  {
    id: 17,
    couleur1: "#DA70D6",
    couleur2: "#f2f0f5",
    couleur3: "#FFC0CB",
  },
  {
    id: 18,
    couleur1: "#6495ED",
    couleur2: "#f2f0f5",
    couleur3: "#4169E1",
  },
  {
    id: 19,
    couleur1: "#DAA520",
    couleur2: "#f2f0f5",
    couleur3: "#CD853F",
  },
  {
    id: 20,
    couleur1: "#00FF00",
    couleur2: "#f2f0f5",
    couleur3: "#7CFC00",
  },
];

/**
 * Les booléens pour conditionner l'affichage des messages.
*/

let firstQuestion = ref(true);
let secondQuestion = ref(true);
let thirdQuestion = ref(true);
let fourthQuestion = ref(true);
let loader = ref(true);
let userAnswer = ref(true);
let isUserEmail = ref(true);
let firstAnswer = ref(true);
let secondAnswer = ref(true);
let thirdAnswer = ref(true);
let fourthAnswer = ref(true);
let fithAnswer = ref(true);
let sixAnswer = ref(true);
let submitAnswer = ref(true);
let preview = ref(true);
let inputName = ref(true);
let selectName = ref(true);



</script>

<style scoped>


.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}


.bgImage {
  background-image: url("/public/assets/img/ressources/mascotte_pandagouin.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  background-attachment: fixed;
}
.panda {
  background: linear-gradient(to top left, #0398c7 0%, #9747ff 100%);
  width: fit-content;
  border-radius: 50px;
  padding-inline: 1rem;
  margin-top: 0.5rem;
}

.user {
  background: white;
  border-radius: 10px;
  padding-inline: 1rem;
  padding-block: 0.7rem;
  margin-top: 0.5rem;
}



.palette-selectionnee {
  border: 2px solid #9747FF;
  border-radius: 10px;
}

.loader{
    display: block;
    position: relative;
    height: 32px;
    width: 200px;
    background: #fff;
    border:2px solid #fff;
    color: #9747ff;
    overflow: hidden;
  }
  .loader::before{
    content: '';
    background: #9747ff;
    position: absolute;
    left: 0;
    top: 0;
    width: 0;
    height: 100%;
    animation: loading 10s linear infinite;
  }
  .loader:after{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    text-align: center;
    font-size: 24px;
    line-height: 32px;
    color: #9747ff;
    mix-blend-mode: multiply;
    animation: percentage 10s linear infinite;
  }
  
  @keyframes loading {
    0% { width: 0 }
    100% { width: 100% }
  }
  @keyframes percentage {
    0% { content: "0%"}
    5% { content: "5%"}
    10% { content: "10%"}
    20% { content: "20%"}
    30% { content: "30%"}
    40% { content: "40%"}
    50% { content: "50%"}
    60% { content: "60%"}
    70% { content: "70%"}
    80% { content: "80%"}
    90% { content: "90%"}
    95% { content: "95%"}
    96% { content: "96%"}
    97% { content: "97%"}
    98% { content: "98%"}
    99% { content: "99%"}
    100% { content: "100%"}
  }
  
  
</style>
