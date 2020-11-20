import Vue from 'vue'
import App from './App.vue'
import Questlog from './components/Questlog'
import axios from 'axios'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Install BootstrapVue
Vue.use(BootstrapVue)

Vue.component('Questlog', Questlog);
Vue.prototype.$http = axios

new Vue({
  el: '#app',
  render: h => h(App)
})
