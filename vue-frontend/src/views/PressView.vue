<template>
<div id="pressView" class="container">
    <div class="mt-4 p-5" 
      v-for="dummy in dummy_title" :key="dummy.rank">
      <router-link
        style="text-decoration:none; color:black; font-weight:bold;"
        @click="onClickRedirect()"
        :to="{name: 'FullView', query:{title:dummy.title,fullContent:JSON.stringify(dummy.fullContent)}}">
        {{dummy.title}}
      </router-link>
      <hr style="border:solid 1px #4b4a47">
  </div>
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