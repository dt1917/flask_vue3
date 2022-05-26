<template>
<div id="mainView">
  <div class="container">
      <div
        class="col-12 btn  btn-outline-secondary mt-3"
        style="padding:3%; font-size:40px; font-weight:bold;"
        v-for="id in newsObjs" :key="id.id" >
        {{id.pressName}}
           <router-link 
            style="text-decoration:none; color:black;"
            @click="onClickRedirect()"
            :to="{name: 'PressView', query:{pressName:id.pressName,newsTop:JSON.stringify(id.newsTop)}}">
            로 이동
           </router-link>
           
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  el: 'mainView',
  name: 'MainView',
  methods: {
    onClickRedirect : function() {
      this.$router.push({name:'PressView', query: {pressName:this, newsTop:this}});
    },
   },
  compute: {},
  data() {
    return {
      newsObjs : ""
    }
  },
  created(){
    axios
        .get('http://127.0.0.1:5000/')
        .then((res)=>{
          this.newsObjs = res.data.newsObjs
        })
        .catch((err)=>{console.log(err)});
  }
}
</script>

<style scoped>
</style>