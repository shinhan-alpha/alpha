<template>
  <Pie :data="data" :options="options" />
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
      data: {
          labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
      datasets: [
          {
          backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
          data: [40, 20, 80, 10]
          }
      ]
      }
    }
  }
}
</script>

<style scoped>
  table {
      border-collapse: collapse;
      width: 100%;
  }

  th,td {
      text-align: left;
      padding: 8px;
  }

  th {
      background-color: #333;
      color: white;
  }

  tr:nth-child(even) {
      background-color: #f2f2f2;
  }
  input[type='checkbox'] {
      cursor: pointer;
  }
</style>