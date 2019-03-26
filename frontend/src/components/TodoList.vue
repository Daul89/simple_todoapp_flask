<template>
  <div>
    <!--<todo  v-for="todo in todos" v-bind:todo="todo"></todo>
    <todo  v-on:delete-todo="deleteTodo" v-for="todo in todos" v-bind:todo="todo"></todo>
    -->
    <todo
      v-on:delete-todo="deleteTodo"
      v-for="todo in todos"
      :todo.sync="todo"
    ></todo>

    <p>Completed tasks: {{todos.filter(todo => {return todo.is_done === true}).length}}</p>
    <p>Pending tasks: {{todos.filter(todo => {return todo.is_done === false}).length}}</p>
  </div>
</template>

<script type = "text/javascript" >
import Todo from './Todo'
import api from '../api.js'

// declare the property to retrieve the data v-binded
export default {
  props: ['todos'],
  components: {
    Todo
  },
  methods: {
    deleteTodo (todo) {
      api.deleteTodo(todo.id)
        .then(() => {
          const todoIndex = this.todos.indexOf(todo)
          this.todos.splice(todoIndex, 1)
        })
    }
  }
}

</script>

<style>
</style>
