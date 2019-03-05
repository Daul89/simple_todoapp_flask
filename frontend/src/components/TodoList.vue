<template>
  <div>
  	<h1 class='ui centered header dividing'> Simple SPA Todo app with Flask & Vue.js </h1>

<!-- Looping and Rendering Data with v-for
### Todo 1: adding buttons which is reacted with backend apis - create/delete/edit. <-- axion maybe
    Todo 2: Display boolean:done on each todo card
    Todo 3: Display the count of boolean:done on top of the application. <-- filter & length?
-->
    <div class='ui centered card' v-for="todo in todos">
      <div class='content'>
        <div class='header'>
          {{ todo.id }}
        </div>
        <div class='meta'>
          {{ todo.title }}
        </div>
        <div class='extra content'>
          <span class='right floated edit icon'>
            <i class='edit icon'></i>
          </span>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script type = "text/javascript" >

//declare the property to retrieve the data v-binded
export default {
	props: ['todos'],
};
</script>
<style>
</style>