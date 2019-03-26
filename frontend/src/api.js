import axios from 'axios'

const API_URL = 'http://127.0.0.1:9200'

export default {
  listTodo, getTodo, putTodo, postTodo, deleteTodo
}

function listTodo () {
  return axios.get(`${API_URL}/todos`)
}

function getTodo (id) {
  return axios.get(`${API_URL}/todos/${id}`)
}

function doneTodo (todo) {
  var dataArray = { 'is_done': todo.is_done }
  var body = JSON.stringify(dataArray)
  return axios.put(`${API_URL}/todos/${todo.id}`, body)
}

function putTodo (todo) {
  var dataArray = { 'item': todo.item }
  var body = JSON.stringify(dataArray)
  return axios.put(`${API_URL}/todos/${todo.id}`, body)
}

function postTodo (item) {
  var dataArray = { 'item': item }
  var body = JSON.stringify(dataArray)
  return axios.post(`${API_URL}/todos`, body)
}

function deleteTodo (id) {
  return axios.delete(`${API_URL}/todos/${id}`)
}
