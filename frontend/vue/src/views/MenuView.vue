<template>
    <div class="container">
      <div>
        <img src="../../../images/menu_tab.png">
      </div>
      <div id="menus">
        <span id="portfolio">포트폴리오</span>
        <button class="btn" id="create" onclick="location.href='create.html';">포트폴리오 생성</button>
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

  /* menubar */
  #menu-wrapper {
      overflow-x: auto;  
      position: fixed;
      left: 0;
      bottom: 0;
      border-collapse: collapse;
      height: 43px;
  }
  #menu-tab {
      background-color: #393D46;
  }
  #menu-tab i {
      font-size: 20px;
  }
  table {
      background-color: #333;
      border-collapse: collapse;
      width: 200%;
      height: 43px;
  }
  th, td {
      text-align: center;
  }
  th {
      background-color: #333;
      color: #fff;
      text-transform: uppercase;
      letter-spacing: 1px;
      width: auto;
  }
  tr:nth-child(even) {
      background-color: #f2f2f2;
  }
  a {
      color: white;
      text-decoration: none;
      font-weight: bold;
      font-size: 13px;
  }
</style>
  