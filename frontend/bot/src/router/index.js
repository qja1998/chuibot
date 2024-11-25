import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '@/views/SignupView.vue'
import BoardView from '@/views/BoardView.vue'
import LoginView from '@/views/LoginView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import PostView from '@/views/PostView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/create-post',
      name: 'create-post',
      component: CreatePostView,
    },
    {
      path: '/post-detail/:id',
      name: 'post-detail',
      component: PostView,
      props: true
    },
  ],
})

export default router
