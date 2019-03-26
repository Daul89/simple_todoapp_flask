<template>
  <div class="ui basic content center aligned segment">
    <div class="ui center aligned grid form">
      <div class="ui fluid action input" style="width:400px; height:50px">
        <input type="text" placeholder="What is your ToDo?" v-model="item">
        <div class="ui button" v-on:click="send(item)">Send</div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js'

export default {
  props: ['todos'],
  data () {
    return {
      item: ''
    }
  },
  methods: {
    send (item) {
      this.item = item
      api.postTodo(item)
        .then((res) => {
          this.todos.push(res.data)
        })
        .then(() => {
          swal('Your ToDo Item has been successfully created!', {
            icon: 'success'
          })
        })
    }
  }
}
</script>
