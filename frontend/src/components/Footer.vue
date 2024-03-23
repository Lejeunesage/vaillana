<template>
    <footer class="text-white font-bold text-center mt-14 lg:max-w-5xl xl:max-w-6xl mx-auto">
      <p class="p-4 text-[0.7rem] md:text-[0.8rem]">
        {{ currentYear }} - VAILLANA - Tous droits réservés.
      </p>
    </footer>
  </template>
  
  <script setup>
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  </script>
  
  <style scoped>
  footer {
      background: linear-gradient(to right, #0398C7 0%, #9747FF 100%);
  }
  </style>
  