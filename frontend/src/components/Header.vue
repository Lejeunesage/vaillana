<template>
    <header class="p-4 text-white">
        <div class="flex justify-between items-center">
            <div class>
                <!-- Ajout du Nom du site -->
                <h1 class="font-Ballsye">VAILLANA</h1>
            </div>
            <!-- Menu d'Hamburger -->
            <div class="wrapper">
                <svg v-if="openMenu" @click="toggleMenu()" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-list showAnimate"
                    viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5" />
                </svg>
                <svg v-if="!openMenu" @click="toggleMenu()" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-lg showAnimate"
                    viewBox="0 0 16 16">
                    <path
                        d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z" />
                </svg>
            </div>
        </div>
    </header>
    <!-- <div class="wrapper">
        <nav>
            <RouterLink to="/" class="text-red-600 uppercase font-JakartaSans">Salut</RouterLink>
            <RouterLink to="/" class="text-red-600 uppercase font-JakartaSans italic">Salut</RouterLink>
            <RouterLink to="/" class="text-red-600 uppercase font-Ballsye">Salut</RouterLink>
            <RouterLink to="/" class="text-red-600 uppercase font-Komikula">Salut</RouterLink>
            <RouterLink to="/" class="text-red-600 uppercase font-Komikula">Salut</RouterLink>
            <RouterLink to="/about">About</RouterLink>
        </nav>
    </div> -->
</template>

<script setup>
/**
 * 
 * Importation
 */
// import { RouterLink } from 'vue-router';
import { ref } from 'vue';


/**
 * 
 * Déclaration des variables 
 */
 const openMenu = ref(true)


 
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
    background: linear-gradient(to right,#0398C7  0%,#9747FF  100%);
}
</style>