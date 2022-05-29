<template>
  <div class="container" >
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
      <button type="checkbox" id="full-btn" style="padding:2.5%" class="rounded-pill  btn btn-warning btn-outline-light btn-lg">듣기</button>
      <button id="pause" style="padding:2.5%" class="rounded-pill  btn btn-warning btn-outline-light btn-lg" >일시정지</button>
      <button id="cancel" style="padding:2.5%" class="rounded-pill  btn btn-warning btn-outline-light btn-lg" >정지</button>
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