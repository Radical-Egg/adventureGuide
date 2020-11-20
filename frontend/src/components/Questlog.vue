<template>
  <div class="wrapper"> 

    <b-container fluid class="bv-example-row">
    <b-row>
      <b-col id="questListCol"><p v-on:click="showDetail($event, quest.id)" v-for="quest in quests" v-bind:key="quest.id"> {{quest.questTitle}} </p></b-col>
      <b-col id="questDetailCol"><p style="white-space:pre-wrap;" id="detailTarget"> {{questDetail}} </p></b-col>
    </b-row>
  </b-container>

  </div>

</template>

<script>

import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
      quests: null,
      questDetail: null
    }
  },
  methods: {
    showDetail: async function(event, id) {
        axios
        .get(`http://127.0.0.1:8000/quests/${id}`)
        .then((response) => {
          this.questDetail = response.data.questContent
          console.log(response);
          })
        .catch(function(error){console.log(error)});
    }

  },
  mounted() {
    axios
    .get('http://127.0.0.1:8000/quests')
    .then(response => {this.quests = response.data})
    
  }
}
</script>

<style>
#questListCol {
  padding-left: 100px;
}

#questDetailCol {
  padding-right: 100px;
}
</style>
