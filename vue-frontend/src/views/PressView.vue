<template>
<div id="pressView" class="container">
    <div 
      class="mt-4 p-5 border border-secondary row" 
      v-for="dummy in dummy_title" :key="dummy.rank">
      <div class="col-9 border-end">
      {{dummy.title}}
      </div>
      <div class="col-1"></div>
      <router-link
        id="test"
        class="col-2 rounded-pill btn btn-warning btn-outline-light"
        style="font-weight:bold; font-size:120%; padding-top:2%;"
        @click="onClickRedirect()"
        :to="{name: 'FullView', query:{title:dummy.title,fullContent:JSON.stringify(dummy.fullContent)}}">
         이동
      </router-link>
      <!-- <hr style="border:solid 1px #4b4a47"> -->
  </div>
  <br>
  <br>
</div>
 
</template>
<script>
  export default {
    el: 'pressView',
    name: 'PressView',
    methods: {
      onClickRedirect : function() {
      this.$router.push({name:'FullView', query: {title:this, fullContent:this}})
      }
    },
    data(){
      return {
        pressName : this.$route.query.pressName,
        dummy_title: JSON.parse(this.$route.query.newsTop)
      }
    }
  }
</script>