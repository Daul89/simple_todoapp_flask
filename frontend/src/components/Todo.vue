<template>
  <div>
    <div class="ui centered card">
      <div class="content">
        <div class="ui sub header">Todo Item {{ todo.id }}</div>
      </div>
      <div class="content" v-show="!Editmode">
        <div class="ui sub header">
          <a>
            <i class="star icon"></i>
            {{ todo.item }}
          </a>
        </div>
        <div class="extra content">
          <span class="right floated delete icon" v-on:click="deleteTodo(todo)">
            <i class="red delete icon"></i>
          </span>
          <span class="right floated edit icon" v-on:click="showForm">
            <i class="blue edit icon"></i>
          </span>
        </div>
      </div>

      <div class="content" v-show="Editmode">
        <div class="ui form">
          <div class="field">
            <label>Item</label>
            <input type="text" v-model="todo.item">
          </div>
          <div></div>
        </div>
        <div class="ui two button attached buttons">
          <button class="ui blue button" v-on:click="updateTodo(todo.item)">Save</button>
          <button class="ui red button" v-on:click="hideForm">Close</button>
        </div>
      </div>

      <div>
        <!-- Use v-show rather than v-if since the element is frequently changed -->
        <div
          class="ui bottom attached inverted green button"
          v-show="todo.is_done && !Editmode"
          v-on:click="undone(todo.id)"
        >Completed</div>
        <div
          class="ui bottom attached inverted red button"
          v-show="!todo.is_done && !Editmode"
          v-on:click="done(todo.id)"
        >Pending</div>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script type = "text/javascript" >
import api from '../api.js'

// declare the property to retrieve the data v-binded
export default {
  props: ['todo'],
  data () {
    return {
      Editmode: false
    }
  },
  methods: {
    done () {
      this.todo.is_done = 1
      api.doneTodo(this.todo)
    },
    undone () {
      this.todo.is_done = 0
      api.doneTodo(this.todo)
    },
    updateTodo (item) {
      this.todo.item = item
      api.putTodo(this.todo)
      this.Editmode = false
    },
    // display form when editmode
    showForm () {
      this.Editmode = true
    },
    // hide form when !editmode
    hideForm () {
      this.Editmode = false
    },
    //
    // handler - delete a todo when onclick
    deleteTodo (todo) {
      swal({
        title: 'Are you sure?',
        text: 'Once deleted, you will not be able to recover.',
        icon: 'warning',
        buttons: true,
        dangerMode: true
      }).then(willDelete => {
        if (willDelete) {
          swal('Your ToDo Item has been successfully deleted!', {
            icon: 'success'
          })
          this.$emit('delete-todo', todo)
        } else {
          swal('Your ToDo Item is safe!')
        }
      })
    }
  }
}
</script>

<style>
</style>
