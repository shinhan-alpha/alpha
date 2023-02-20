<template>
    <div id="app">
        <h1>알파카트(일괄매수)</h1>
        <table>
            <thead>
            <tr>
                <th>선택</th>
                <th>종목</th>
                <th>현재가</th>
                <th>수량</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(stock, index) in stocks" :key="index">
                <td><input type="checkbox" v-model="stock.checked" @click="stockClick(stock)"></td>
                <td>{{ stock.name }}</td>
                <td>{{ stock.price }}</td>
                <td>{{ stock.quantity }}</td>
            </tr>
            </tbody>
        </table>
        <h1>주식 포트폴리오</h1>
        <Pie :data="data" :options="options" />
        <h2>주문금액(합계) <span id="myValue">0</span></h2>
        <button type="button"><img src="../../../images/buy.png" alt="매수버튼"
                onclick="modal"></button>
    </div>

  </template>
  
  <script lang="js">
  import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
  import { Pie } from 'vue-chartjs'
  
  ChartJS.register(ArcElement, Tooltip, Legend)
  
  export default {
    name: 'App',
    components: {
      Pie
    },
    data() {
      return {
        stocks: [
        { name: "LG전자", price: "113,000", quantity: "1", checked: false },
        { name: "현대차", price: "179,200", quantity: "1", checked: false },
        { name: "삼성전자", price: "62,600", quantity: "1", checked: false },
        { name: "대우중공업", price: "100,000", quantity: "1", checked: false },
        ],
        data: {
            labels: stocks.filter(stock => stock.checked).map(stock => stock.name),
            datasets: [
                {
                backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                data: [40, 20, 80, 10]
                }
            ]
        }
      }
    },
    computed:{
        checkedStocks() {
      return this.stocks.filter(stock => stock.checked);
    },
    chartData() {
      const checkedStocks = this.checkedStocks;
      const checkedStockNames = checkedStocks.map(stock => stock.name);
      const checkedStockPrices = checkedStocks.map(stock => Number(stock.price.replace(',', '')));
      return {
        labels: checkedStockNames,
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
            data: checkedStockPrices
          }
        ]
      };
    }
    },
    methods: {
        stockClick(stock) {
             stock.checked = true;
        }
    }
  }
  </script>
<style scoped>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        td {
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #333;
            color: white;
        }
        tr:nth-child(odd) {
            background-color: #a5a5a5;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        input[type=checkbox] {
            cursor: pointer;
        }
</style>