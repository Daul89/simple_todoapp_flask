// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$http = axios
/* eslint-disable no-new */
/* Init Vue instance */

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

const API_URL = 'http://127.0.0.1:9200'

export function listTodo () {
  return axios.get(`${API_URL}/todos/`)
}

export function getTodo (id) {
  return axios.get(`${API_URL}/todos/${id}/`)
}

export function putTodo (todo) {
  return axios.put(`${API_URL}/todos/${todo.id}/`, todo)
}

export function postTodo (todo) {
  return axios.post(`${API_URL}/todos/`, todo)
}

export function deleteTodo (id) {
  return axios.post(`${API_URL}/todos/${id}/`)
}
