<template>
  <div id="app">
  <div id="titleContainer" style="padding-bottom:50px;"> 
    <h1 style="text-align:center;"> {{title}}</h1>
  </div>
  
  <Questlog> </Questlog>

  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      title: "Adventure Guide"
    }
  }
}
</script>

<style>

</style>
