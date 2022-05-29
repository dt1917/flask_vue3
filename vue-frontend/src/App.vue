<template>
  <div class="background container" id="bg">
  <div id="test"></div>    
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
      <div class="rounded-pill btn btn-secondary btn-outline-light border border-secondary"
      style="font-size:100%; font-weight:bold;margin-right:5%;"
        @click="$router.back()">이전</div>
      <div class="rounded-pill btn btn-secondary btn-outline-light border border-secondary"
      style="font-size:100%; font-weight:bold;" 
      @click="$router.push('/settingView')">
        설정
      </div>
      </div>
    </div>
    
  
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