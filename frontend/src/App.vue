
<!-- bind the data from data() with v-bind -->
<template>
  <div >
      <todo-list v-bind:todos="todos"></todo-list>

  </div>
</template>

<script>

import TodoList from './components/TodoList' 

// Declares the sub-components
// component word to be seperated with dashes instead of Camel-case automatically in template
export default {
  name: 'app',
  components: {
    TodoList,
  },
  // TODO: data() has to be ajax to call backend API and format the json to 
  data() {
    return {
      todos: [{
        title: 'Todo A',
        id: '1',
        done: false,
      }, {
        title: 'Todo B',
        id: '2',
        done: true,
      }, {
        title: 'Todo C',
        id: '3',
        done: false,
      }, {
        title: 'Todo D',
        id: '4',
        done: false,
      }],
    };
  },
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
