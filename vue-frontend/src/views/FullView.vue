<template>
  <div class="container row" >
    <div class="container">
      <div id="title" style="font-weight:bold">
    {{news_title}}
    </div>
    <hr>
    {{full_content}}
    <hr>
    </div>
  <!-- <div class="card"
  style="margin:0% 0% 5% 0%">
    <div class="card-header">
    {{news_title}}
    </div>
    <div class="card-body col-12" autocomplete="off" >
      {{full_content}}
    </div>
  </div> -->
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
        full_content:this.$route.query.fullContent,
      }
    },
    created() {
      tts
    }
  }
</script>