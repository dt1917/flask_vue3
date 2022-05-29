<template>
  <div class="card bg-secondary">
    <div class="card-body" id="font">
      <br>
      글꼴 설정
      <br>
        <input type="radio"  id="one" class="form-check-input" style="margin:3%" value='BareunDotum' v-model="font" checked>
        <label class="form-check-label"  for="one">돋움체</label> <br>
        <input type="radio" id="two" class="form-check-input" style="margin:3%" value='ChosunGu' v-model="font">
        <label class="form-check-label"  for="two">굴림체</label>
    </div>
    <hr>
    <div class="card-body" id="font-size">글자 크기 설정
        <br>
        <div class="col-12">
            <button id="minus" @click="font_size--">-</button>
            <input v-model="font_size" placeholder="300" size="13%" style="width:60%;">%
            <button id="minus" @click="font_size++">+</button>
        </div>
    </div>
    <hr>
    <div class="card-body" id="dark">다크 모드 설정
        <br>
        <input class="form-check-input" type="radio" id="on" value=1 v-model="dark">
        <label class="form-check-label" style="margin:1%;" for="on">ON</label><br>
        <input class="form-check-input" type="radio" id="off" value=0 v-model="dark" checked>
        <label class="form-check-label" style="margin:1%;" for="off">OFF</label>
    </div>
   <button class="btn btn-dark text-white btn-lg"
   style="font-weight:bold; font-size:120%;"
    @click="change">확인</button>
  </div>
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