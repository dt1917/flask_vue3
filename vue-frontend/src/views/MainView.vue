<template>
<div id="mainView">
  <div class="container">
      <div
        class="row mt-4 p-5 border border-secondary"
        style="padding:3%;  font-weight:bold;"
        v-for="id in newsObjs" :key="id.id" >
        <div class="col-9 border-end" style="">
        {{id.pressName}}
        </div>
        <div class="col-1"></div>
           <router-link 
            class="col-2 rounded-pill btn btn-warning btn-outline-light"
            style="text-decoration:none; font-size:120%; font-weight:bold; "
            @click="onClickRedirect()"
            :to="{name: 'PressView', query:{pressName:id.pressName,newsTop:JSON.stringify(id.newsTop)}}">
            이동
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