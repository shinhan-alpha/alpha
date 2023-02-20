<template>
    <div class="container">
      <div>
        <img src="../../../images/menu_tab.png">
      </div>
      <div id="menus">
        <span id="portfolio">포트폴리오</span>
        <button class="btn" id="create" onclick="location.href='/create';">포트폴리오 생성</button>
        <button class="btn" id="recommend" onclick="location.href='#';">포트폴리오 추천</button>
        <button class="btn" id="current" onclick="location.href='#';">포트폴리오 현황</button>
        <button class="btn" id="master" onclick="location.href='#';">고수의 포트폴리오</button>
    </div>
    </div>
  </template>
  
<script>
export default {
  name:"menu",
  data() {

  },
  methods: {

  },
};
</script>
  
<style scoped>
  /* body */
  body {
      margin: 0;
  }
  img {
      max-width: 100%;
      max-height: 100%;
      position: absolute;
      left: 0;
      top: 0;
  }
  #menus {
      position: relative;
  }
  #portfolio {
      position: absolute;
      left: 112px;
      top: 98px;

      font-family: 'Inter';
      font-style: normal;
      font-weight: 700;
      font-size: 12px;
      line-height: 15px;
      display: flex;
      align-items: center;

      color: #000000;
  }
  #create {
      position: absolute;
      left: 112px;
      top: 136px;
  }
  #recommend {
      position: absolute;
      left: 112px;
      top: 167px;
  }
  #current {
      position: absolute;
      left: 112px;
      top: 198px;
  }
  #master {
      position: absolute;
      left: 112px;
      top: 229px;
  }
  .btn {
      border: none;
      background-color: white;
  }
</style>
  