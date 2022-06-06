<template>
<div class="row">
  <div class="col-1"></div>
  <div class="col-10">
    <div id="font">
      <br>
   <div style="font-weight:bold;margin-bottom:-12%">   글꼴 설정</div>
      <br>
        <input type="radio"  id="one" class="form-check-input" style="margin:3% " value='BareunDotum' v-model="font" checked>
        <label class="form-check-label"  for="one">돋움체</label> <br>
        <input type="radio" id="two" class="form-check-input" style="margin:3%" value='ChosunGu' v-model="font">
        <label class="form-check-label"  for="two">굴림체</label>
    </div>
    <hr>
    <div id="font-size">
      <div style="font-weight:bold;margin-bottom:-10%">글자 크기 설정</div>
        <br>
            <button id="minus" class="btn btn-secondary col-1" @click="font_size--">-</button>
            <input v-model="font_size" class="col-8"  placeholder="기본 300">%
            <button id="minus" class="btn btn-secondary col-1" @click="font_size++">+</button>
    </div>
    <hr>
    <div id="dark">
      <div style="font-weight:bold;margin-bottom:-13%">다크 모드 설정</div>
        <br>
        <input class="form-check-input" type="radio" id="on" value=1 v-model="dark">
        <label class="form-check-label" style="margin:1%;" for="on">ON</label><br>
        <input class="form-check-input" type="radio" id="off" value=0 v-model="dark" checked>
        <label class="form-check-label" style="margin:1%;" for="off">OFF</label>
    </div>
  </div>
  </div>
  <div class="col-1"></div>
   <button class="btn btn-light btn-outline-dark col-12"
   style="font-weight:bold; font-size:120%; margin:0 auto;"
    @click="change">확인</button>
  
</template>

<script>
  export default {
    el: 'settingView',
    name: 'SettingView',
    data() {
        return {
            font: "",
            font_size: "",
            font_color: "", 
            dark:""
        };
    },
    methods: {
      change: function() {
        
          document.getElementById("app").style.fontFamily = this.font;
          if (this.font_size == ""){
            document.getElementById("bg").style.fontSize = 100 + "%";}
          else {
            document.getElementById("app").style.fontSize = this.font_size + "%";
          }
          if (this.dark==1){
            document.getElementById("app").style.background = "#121212";
            document.getElementById("bg").style.color="white";
          }else {
            document.getElementById("app").style.background = "#ffffff";
            document.getElementById("bg").style.color ="black";
          }
          this.$router.back();
         }
    }
  }
</script>