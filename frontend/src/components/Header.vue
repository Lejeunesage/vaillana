<template>
    <header class="p-4 text-white md:flex md:justify-between md:items-center md:px-8 lg:max-w-5xl xl:max-w-6xl mx-auto">
        <div class="flex justify-between items-center">
            <div class>
                <!-- Ajout du Nom du site -->
                <h1 class="font-Ballsye md:text-2xl">VAILLANA</h1>
            </div>
            <!-- Menu d'Hamburger -->
            <div class="wrapper md:hidden">
                <svg v-if="!openMenu" @click="toggleMenu()" xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                    fill="currentColor" class="bi bi-list showAnimate" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5" />
                </svg>
                <svg v-if="openMenu" @click="toggleMenu()" xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                    fill="currentColor" class="bi bi-x-lg showAnimate" viewBox="0 0 16 16">
                    <path
                        d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z" />
                </svg>
            </div>
        </div>
        <div class="mt-6 md:mt-0" v-if="openMenu">
            <nav class="flex flex-col justify-center gap-2 md:flex-row md:gap-4">
                <RouterLink to="/" class="text-center p-1 inline-block uppercase font-bold ">
                    <span class="font-Acumin" :class="{ 'line underline': $route.path === '/' }">Accueil</span>
                </RouterLink>
                <RouterLink to="/equipe" class="text-center p-1 rounded-lg inline uppercase font-bold ">
                    <span class="font-Acumin" :class="{ 'line underline': $route.path === '/equipe' }">l'équipe</span>
                </RouterLink>
                <RouterLink to="/commencer" class="text-center p-1 px-2 rounded-md uppercase font-bold bg-white">
                    <span class="text-gradient font-Acumin">Commencer</span>
                </RouterLink>
            </nav>
        </div>
    </header>
</template>

<script setup>
/**
 * 
 * Importation
 */
import { ref } from 'vue';


/**
 * 
 * Déclaration des variables 
 */
const openMenu = ref(false)



/**
* 
* Méthodes
*/

const toggleMenu = () => {
    openMenu.value = !openMenu.value
}

</script>

<style scoped>
/*** Animation d'apparition du menu */

.showAnimate {
    animation: showAnimation 1.5s ease-in-out;
}

@keyframes showAnimation {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

header {
    background: linear-gradient(to right, #0398C7 0%, #9747FF 100%);
}


.text-gradient {
    background-image: linear-gradient(to right, #0398C7 0%, #9747FF 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.line {
    position: relative;
    text-decoration: none;
}

.line::after {
    content: '';
    position: absolute;
    left: 50%;
    bottom: -2px;
    width: 0;
    height: 2px;
    background-color: white;
    transition: width 1s ease-in-out;
    transform: translateX(-50%);
}

.line:hover::after {
    width: calc(100% + 2px);
}
.line::after {
    width: calc(100% + 2px);
}
</style>