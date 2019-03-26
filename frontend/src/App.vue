
<!-- bind the data from data() with v-bind -->
<template>
  <div>
    <h1 class="ui centered header dividing">Simple SPA Todo app with Flask & Vue.js</h1>
    <create-todo v-bind:todos="todos" v-on:add-todo="addTodo"></create-todo>
    <todo-list v-bind:todos="todos"></todo-list>
  </div>
</template>

<script>
import TodoList from './components/TodoList'
import CreateTodo from './components/CreateTodo'
import api from './api.js'

// Declares the sub-components
// component word to be seperated with dashes instead of Camel-case automatically in template
export default {
  data () {
    return {
      todos: []
    }
  },
  mounted () {
    api.listTodo().then(res => {
      this.todos = res.data
    })
  },
  name: 'app',
  components: {
    // component will be mounted as todo-list see line:5
    TodoList,
    CreateTodo
  },

  // TODO: data() has to be ajax to call backend API and format the json to

  methods: {
    addTodo (item) {
      this.todos.push({
        item
      })
    }
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
