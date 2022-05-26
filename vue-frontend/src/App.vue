<template>
  <div class="background container" id="bg">
    
  <div>
    <div class="seear">  
      <router-link to="/">
          <img class="mx-auto d-block" src="./assets/logo.png"
          style="width:40%">
      </router-link>
    </div>
  </div>
  <div class="row"
    style="padding:3% 0% 5% 0%;">

      <div class="col-12 btn-group">
      <div class="btn btn-outline-secondary"
      style="font-size:30px; font-weight:bold;"
        @click="$router.back()">이전</div>
      <div class="btn btn-outline-secondary"
      style="font-size:30px; font-weight:bold;" 
      @click="$router.push('/settingView')">
        설정
      </div>
      </div>
    </div>
    <br>
  <router-view></router-view>

  </div>
</template>

<script>
export default {
  el: 'app',
  name: 'App'
}
</script>

<style>
@import url("./assets/css/style.css");
</style>