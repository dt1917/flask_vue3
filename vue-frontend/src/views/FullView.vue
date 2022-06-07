<template>
  <div class="container row" >
    <div class="container" style="height:40vh; overflow:scroll;">
      <div id="title" style="font-weight:bold">
    {{news_title}}
    </div>
    <hr>
    {{full_content}}
    <hr>
    </div>
      <button type="checkbox" id="full-btn" style="padding:1%;" class="rounded-pill  btn btn-warning btn-outline-light ">듣기</button>
    <br>  <button id="pause" style="padding:1%; margin:3% 0% 3% 0%" class="rounded-pill  btn btn-warning btn-outline-light " >일시정지</button>
    <br>  <button id="cancel" style="padding:1%;" class="rounded-pill  btn btn-warning btn-outline-light " >정지</button>
  </div>
</template>
<script>
import tts from '../assets/tts.js'
  export default {
    el: 'fullView',
    name: 'FullView',
    data(){
      return {
        news_title: this.$route.query.title,
        full_content:JSON.stringify(this.$route.query.fullContent),
      }
    },
    created() {
      tts
    }
  }
</script>