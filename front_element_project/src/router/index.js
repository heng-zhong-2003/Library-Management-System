import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: () => import('../views/login.vue')
    },
    {
      path: '/homepage',
      component: () => import('../views/homepage.vue')
    },
    {
      path: '/search',
      component: () => import('../views/search.vue')
    },
    {
      path: '/borrows',
      component: () => import('../views/borrows.vue')
    },
    {
      path: '/manage',
      component: () => import('../views/manage.vue')
    },
    {
      path: '/addbook',
      component: () => import('../views/addbook.vue')
    },
    {
      path: '/delbook',
      component: () => import('../views/delbook.vue')
    },
    {
      path: '/register',
      component: () => import('../views/register.vue')
    },
    {
      path: '/manageusr',
      component: () => import('../views/manageusr.vue')
    },
    {
      path: '/bk.jpg',
      component: () => import('../views/bk.jpg')
    }
  ]
})

export default router
