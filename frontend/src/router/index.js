import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/equipe',
      name: 'Equipe',
      component: () => import('../views/EquipeView.vue')
    },
    {
      path: '/commencer',
      name: 'Commencer',
      component: () => import('../views/CommencerView.vue')
    }
  ]
})

export default router
