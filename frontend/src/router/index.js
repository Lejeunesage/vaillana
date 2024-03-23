import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Chatbot from '../views/Chatbot.vue';
import Equipe from '../views/Equipe.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/equipe',
      name: 'Equipe',
      component: Equipe
    },
    {
      path: '/chatbot',
      name: 'Chatbot',
      component: Chatbot
    },
  ]
})

export default router
