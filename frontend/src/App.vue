<script setup>
import { RouterView, RouterLink } from 'vue-router';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="">
    <Header />
    <RouterView />
    <Footer />
  </div>
</template>

<style scoped></style>
