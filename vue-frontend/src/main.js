import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'

import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import router from './router'
import axios from 'axios'

const app = createApp(App).use(router).use(router)
app.use(BootstrapVue3)
app.config.globalProperties.$axios = axios;
app.mount('#app')
