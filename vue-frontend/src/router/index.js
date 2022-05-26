import { createRouter, createWebHistory } from 'vue-router'
import PressView from '../views/PressView.vue'
import MainView from '../views/MainView.vue'
import FullView from '../views/FullView.vue'
import SettingView from '../views/SettingView.vue'

const routes = [
  {
    path: '/pressView',
    name: 'PressView',
    component: PressView,
  },
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/fullView',
    name: 'FullView',
    component: FullView
  },
  {
    path: '/settingView',
    name: 'SettingView',
    component: SettingView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router