<template>
  <div class="bgImage">
    <div class="py-8 bg-[#eeeeeedf]">
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
              <span class="text-[#9747FF]">Panda</span>, votre assistant générateur de
              site web
            </h1>
            <p class="font-JakartaSans text-center text-sm">
              Je vous assiste dans la génération de votre site web. Alors dites-moi
              clairement, ce que vous voulez.
            </p>
          </div>
        </section>
        <section class="lg:max-w-5xl xl:max-w-6xl mx-auto">
          <div class="flex justify-center pt-4">
            <img src="/public/assets/img/ressources/icone.png" alt="" class="w-20" />
          </div>
          <!-- Section du chat -->
          <section class="" style="font-family: 'Poppins'">
            <!-- Première question -->
            <p
              class="panda text-white"
              v-if="firstQuestion1"
              v-html="pandaQuestions[0].question"
            ></p>
            <Loader v-if="firstQuestion1 && !firstQuestion2" />
            <p
              class="panda text-white"
              v-if="firstQuestion2"
              v-html="pandaQuestions[1].question"
            ></p>
            <Loader v-if="firstQuestion1 && firstQuestion2 && !firstQuestion3" />
            <p
              class="panda text-white"
              v-if="firstQuestion3"
              v-html="pandaQuestions[2].question"
            ></p>
            <Loader v-if="firstQuestion1 && firstQuestion2 && firstQuestion3 && !userAnswer" />

            <!-- Première réponse de l'utilisateur -->
            <div class="flex justify-end items-end flex-col ml-16" v-if="userAnswer">

                <p v-if="firstAnswer" class="user">
                  <span >{{ userResponses[0].response1 }}</span>
                  <span class="transition-all">
                      <input
                        type="text"
                        name="fullName"
                        v-model = "fullName"
                        id=""
                        class="ml-1 font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                    >.
                    <button @click="showUserAnswer2()" v-if="showNextButton1" class="relative inline-flex items-center justify-center px-3 py-0 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
                          <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
                          <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
                          <span class="relative text-white text-sm">Suivant</span>
                      </button>
                </p>
                <Loader class="ml-auto mt-2" v-if="userAnswer && firstAnswer && !secondAnswer" />
                
                <p class="user" v-if="secondAnswer">
                  <span>{{ userResponses[0].response2 }}</span
                  >
                  <span class="transition-all delay-1000">
                    <select
                    @change="handleCategory($event)"
                      id="categories"
                      v-model ="category"
                      class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer"
                    >
                      <option selected disabled></option>
                      <option
                        :value="cat.category"
                        v-for="(cat, catIndex) in categories"
                      >
                        {{ cat.category }}
                      </option>
                    </select> .
                  </span>
                </p>

                <Loader class="ml-auto mt-2" v-if="userAnswer && firstAnswer && secondAnswer && !thirdAnswer" />

                <p class="user" v-if="thirdAnswer">
                  <span>{{ userResponses[0].response3 }}</span>

                  <span class="transition-all delay-1000">
                    <input
                      type="text"
                      name="siteName"
                      v-model = "siteName"
                      id=""
                      class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                  > .
                  <button @click="showUserAnswer3()" v-if="showNextButton2" class="relative inline-flex items-center justify-center px-3 py-0 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
                          <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
                          <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
                          <span class="relative text-white text-sm">Suivant</span>
                      </button>
                </p>

                <Loader class="ml-auto mt-2" v-if="userAnswer && firstAnswer && secondAnswer && thirdAnswer && !fourthAnswer" />

                <p class="user" v-if="fourthAnswer">
                  <span>{{ userResponses[0].response4 }}</span>

                  <div class="grid grid-cols-4 gap-1 my-2 justify-center" v-if="showAllPalette">
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
                    <div v-if="showSelectedPalette"
                      class="flex z-40 cursor-pointer mt-5 w-[60%] mx-auto rounded-lg border-2 border-transparent"
                    >
                      <div
                        class="w-[34%] h-10 rounded-s-lg"
                        :style="{ backgroundColor: firstColorSelected }"
                      ></div>
                      <div
                        class="w-[34%] h-10"
                        :style="{ backgroundColor: secondColorSelected }"
                      ></div>
                      <div
                        class="w-[33%] h-10 rounded-e-lg"
                        :style="{ backgroundColor: thirdColorSelected }"
                      ></div>
                    </div>
                  
                  <div class="flex justify-center mt-3" v-if="SubmitButton">
                    <button @click="sendMessage()" class="relative inline-flex items-center justify-center px-3 py-2 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
                            <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
                            <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
                            <span class="relative text-white text-sm">Soumettre</span>
                        </button>
                  </div>
                </p>
            </div>

            <Loader class="ml-auto mt-2" v-if="userAnswer && firstAnswer && secondAnswer && thirdAnswer && fourthAnswer && !secondQuestion1" />

            <!-- Deuxième question -->
            <p
              class="panda text-white"
              v-if="secondQuestion1"
              v-html="pandaQuestions[3].question"
            ></p>

            <Loader class="mt-2" v-if="userAnswer && firstAnswer && secondAnswer && thirdAnswer && fourthAnswer && secondQuestion1 && !secondQuestion2" />

            <p
              class="panda text-white"
              v-if="secondQuestion2"
              v-html="pandaQuestions[4].question"
            ></p>
            
            <!-- Loader -->
            <div class="flex justify-center my-4" v-if="loader"><span class="loader"></span></div>

            <!-- Troisième question -->
            <p
              class="panda text-white"
              v-if="thirdQuestion1"
              v-html="pandaQuestions[5].question"
            ></p>

            <Loader class="mt-2" v-if="userAnswer && firstAnswer && secondAnswer && thirdAnswer && fourthAnswer && secondQuestion1 && secondQuestion2 && thirdQuestion1 && !thirdQuestion2 && !loader" />

            <p
              class="panda text-white"
              v-if="thirdQuestion2"
              v-html="pandaQuestions[6].question"
            ></p>


            <!-- Deuxième réponse de l'utilisateur -->
            <div class="flex justify-end items-end flex-col ml-16" v-if="isUserEmail">
                <p
                  class="user"
                  v-for="(response, index) in userResponses.slice(1, 2)"
                  :key="index"
                >
                  {{ response.response1 }}
                  <span class="flex items-center">
                    <span class="transition-all delay-1000">
                      <input
                        type="email"
                        name="fullName"
                        v-model = "email"
                        id=""
                        class="font-bold bg-transparent border-0 border-b-2 appearance-none text-black border-[#9747FF] focus:border-[#0398C7] focus:outline-none focus:ring-0peer" /></span
                    >
                    <button @click="sendWebSite()" v-if="receiveButton" class=" ml-3 mt-3 relative inline-flex items-center justify-center px-3 py-1 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out rounded-full shadow-xl group hover:ring-1 hover:ring-purple-500">
                            <span class="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 via-purple-600 to-pink-700"></span>
                            <span class="absolute bottom-0 right-0 block w-64 h-64 mb-32 mr-4 transition duration-500 origin-bottom-left transform rotate-45 translate-x-24 bg-pink-500 rounded-full opacity-30 group-hover:rotate-90 ease"></span>
                            <span class="relative text-white text-sm">Recevoir</span>
                        </button>
                  </span>
                </p>
            </div>
            <Loader class="ml-auto mt-2 bg-red-500" v-if="userAnswer && firstAnswer && secondAnswer && thirdAnswer && fourthAnswer && secondQuestion1 && secondQuestion2 && thirdQuestion1 && thirdQuestion2 && isUserEmail && !fourthQuestion" />

            <!-- Quatrième question -->
            <p
              class="panda text-white"
              v-if="fourthQuestion"
              v-html="pandaQuestions[7].question"
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
import { ref, onMounted } from "vue";
import Loader from "@/components/Loader.vue";

let paletteSelectionneeId = ref(null);
let rgbaToHex = (rgba) => {
  const [r, g, b] = rgba.match(/\d+/g);
  return `#${Number(r).toString(16)}${Number(g).toString(16)}${Number(b).toString(16)}`;
};

/**
 * Les varaibles
 */

let fullName = ref("");
let email = ref("");
let siteName = ref("");
let category = ref("");
let colors = ref([]);
let firstColorSelected = ref("")
  let secondColorSelected = ref("")
  let thirdColorSelected = ref("")
  let showAllPalette = ref(true)
  let showSelectedPalette = ref(false)

let data = {
  fullName: fullName.value,
  email: email.value,
  siteName: siteName.value,
  category: category.value,
  palettes: colors.value,
};

let sendMessage = () => {
  data.fullName = fullName.value;
  data.email = email.value;
  data.siteName = siteName.value;
  data.category = category.value;
  data.palettes = colors.value;

  firstColorSelected.value = selectedPalette.value.couleur1
  secondColorSelected.value = selectedPalette.value.couleur2
  thirdColorSelected.value = selectedPalette.value.couleur3
  SubmitButton.value = false;
  secondQuestion1.value = true;
  showAllPalette.value = false;
  showSelectedPalette.value = true;
  setTimeout(() => {
    secondQuestion2.value = true;
    loader.value = true;
  }, 2000);
  setTimeout(() => {
    loader.value = false;
    thirdQuestion1.value = true
  }, 12000);
  setTimeout(() => {
    thirdQuestion2.value = true
    isUserEmail.value = true;
  }, 14000);

};

let selectedPalette = ref([]);

let getColors = (palette) => {
  paletteSelectionneeId.value = palette.id;
  selectedPalette.value = palettes.find(palet => palet.id === palette.id);
  colors.value.push(palette.couleur1);
  colors.value.push(palette.couleur2);
  colors.value.push(palette.couleur3);

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
    response2: "Je veux un site web dans le domaine de ",
    response3: "Le nom de mon entreprise est  ",
    response4: "Et je voudrais les palettes de couleur ",
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

let firstQuestion1 = ref(true);
let firstQuestion2 = ref(false);
let firstQuestion3 = ref(false);
let secondQuestion1 = ref(false);
let secondQuestion2 = ref(false);
let thirdQuestion1 = ref(false);
let thirdQuestion2 = ref(false);
let fourthQuestion = ref(false);
let loader = ref(false);
let userAnswer = ref(false);
let isUserEmail = ref(false);
let firstAnswer = ref(false);
let secondAnswer = ref(false);
let thirdAnswer = ref(false);
let fourthAnswer = ref(false);
let preview = ref(false);
let SubmitButton = ref(true);
let showNextButton1 = ref(true);
let showNextButton2 = ref(true);
let selectedCategory = ref("");
let receiveButton = ref(true)

setTimeout(() => {
  firstQuestion2.value = true;
}, 2000);

setTimeout(() => {
  firstQuestion3.value = true;
}, 4000);
setTimeout(() => {
  userAnswer.value = true;
  firstAnswer.value = true;
}, 7000);

// Fonction appelée lors de soumission du nom de l'utilisateur
const showUserAnswer2 = () => {
  if(fullName.value == '') {
    secondAnswer.value = false;
  } else {
    secondAnswer.value = true;
    showNextButton1.value = false;
  }
}



// Fonction appelée lors de soumission du domaine d'activité
const handleCategory = (event) => {
  selectedCategory.value = event.target.value;
  if (selectedCategory.value != "") {
    thirdAnswer.value = true;
  } else {
    thirdAnswer.value = false;
    
  }
}

// Fonction appelée lors de soumission du nom de l'entreprise
const showUserAnswer3 = () => {
  if(siteName.value == '') {
    fourthAnswer.value = false;
  } else {
    fourthAnswer.value = true;
    showNextButton2.value = false;
  }
}

// Fonction appelée lors de l'envoi de l'adresse email
const sendWebSite = () => {
    preview.value = true;
    receiveButton.value = false;
    fourthQuestion.value = true;
}
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
  border: 2px solid #9747ff;
  border-radius: 10px;
}

.loader {
  display: block;
  position: relative;
  height: 32px;
  width: 200px;
  background: #fff;
  border: 2px solid #fff;
  color: #9747ff;
  overflow: hidden;
}
.loader::before {
  content: "";
  background: #9747ff;
  position: absolute;
  left: 0;
  top: 0;
  width: 0;
  height: 100%;
  animation: loading 10s linear infinite;
}
.loader:after {
  content: "";
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
  0% {
    width: 0;
  }
  100% {
    width: 100%;
  }
}
@keyframes percentage {
  0% {
    content: "0%";
  }
  5% {
    content: "5%";
  }
  10% {
    content: "10%";
  }
  20% {
    content: "20%";
  }
  30% {
    content: "30%";
  }
  40% {
    content: "40%";
  }
  50% {
    content: "50%";
  }
  60% {
    content: "60%";
  }
  70% {
    content: "70%";
  }
  80% {
    content: "80%";
  }
  90% {
    content: "90%";
  }
  95% {
    content: "95%";
  }
  96% {
    content: "96%";
  }
  97% {
    content: "97%";
  }
  98% {
    content: "98%";
  }
  99% {
    content: "99%";
  }
  100% {
    content: "100%";
  }
}
</style>
