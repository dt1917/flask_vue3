<template>
  <div class="card bg-secondary">
    <div class="card-body" id="font">
      <br>
      글꼴 설정
      <br>
        <input type="radio"  id="one" value='BareunDotum' v-model="font" checked>
        <label style="margin:5%" for="one">돋움체</label>
        <input type="radio" id="two" value='ChosunGu' v-model="font">
        <label style="margin:5%" for="two">굴림체</label>
    </div>
    <hr>
    <div class="card-body" id="font-size">글자 크기 설정
        <br>
        <div class="col-12">
            <button id="minus" @click="font_size--">-</button>
            <input v-model="font_size" placeholder="0" size="13%" style="width:60%;">%
            <button id="minus" @click="font_size++">+</button>
        </div>
    </div>
    <hr>
    <div class="card-body" id="dark">다크 모드 설정
        <br>
        <input type="radio" id="on" value="#121212" v-model="dark">
        <label style="margin:5%" for="on">ON</label>
        <input type="radio" id="off" value="white" v-model="dark" checked>
        <label style="margin:5%" for="off">OFF</label>
    </div>
   <button class="btn btn-dark text-white btn-lg"
   style="font-weight:bold; font-size:30px;"
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
            dark: ""
        };
    },
    methods: {
      change: function() {
        if(parseInt(this.font_size) > 0) {
          document.getElementById("bg").style.fontFamily = this.font;
          document.getElementById("bg").style.fontSize = this.font_size + "px";
          document.getElementById("bg").style.background = this.dark;
          this.$router.push("/");
          }else {
            alert("폰트 크기를 1 이상으로 맞춰주세요");}
      }
    }
  }
</script>