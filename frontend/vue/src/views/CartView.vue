<template>
    <div id="app">
      <h1>알파카트(일괄매수)</h1>
      <div class="my-box" v-for="(stock, index) in stocks" :key="index">
        <input type="checkbox" v-model="selectedStocks[index]" @change="updateChart" />
        <span>{{ stock.name }} 현재가: {{ stock.price }} 수량: {{ stock.quantity }}</span>
        <p>{{ selectedStocks[index] ? 'Selected' : '' }}</p>
      </div>
  
      <h1>주식 포트폴리오</h1>
      <div class="chart-container" style="position: relative; height:40vh; width:30vw">
        <canvas id="myChart"></canvas>
      </div>
  
      <h2>주문금액(합계) <span>{{ totalValue }}</span></h2>
      <button type="button"><img src="images/매수버튼.PNG" alt="매수버튼" /></button>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js';
  
  export default {
    data() {
      return {
        stocks: [
          { name: 'LG전자', price: 113000, quantity: 1 },
          { name: '현대차', price: 179200, quantity: 1 },
          { name: '삼성전자', price: 62600, quantity: 1 },
          { name: '대우중공업', price: 100000, quantity: 1 },
        ],
        selectedStocks: [false, false, false, false],
        chartData: {
          labels: ['LG전자', '현대차', '삼성전자', '대우중공업'],
          datasets: [
            {
              data: [0, 0, 0, 0],
              backgroundColor: [
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16),
              ],
            },
          ],
        },
        myChart: null,
      };
    },
    computed: {
      totalValue() {
        return this.chartData.datasets[0].data.reduce((a, b) => a + b, 0);
      },
    },
    mounted() {
      const ctx = document.getElementById('myChart').getContext('2d');
      this.myChart = new Chart(ctx, {
        type: 'pie',
        data: this.chartData,
      });
    },
    methods: {
      updateChart() {
        this.chartData.datasets[0].data = this.selectedStocks.map((selected, index) => {
          if (selected) {
            const stock = this.stocks[index];
            return stock.price * stock.quantity;
          } else {
            return 0;
          }
        });
        this.myChart.update();
      },
    },
  };
  </script>
  
  <style>
  .my-box {
    width: 330px;
    border: 1px solid;
    padding: 5px;
  }
  </style>
  