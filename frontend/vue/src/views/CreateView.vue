<template>
    <div class="container">
        <div id="top-wrapper">
            <font-awesome-icon icon="fa-solid fa-chevron-left" onclick=""/>
            <span>포트폴리오 생성</span>
        </div>
        <!-- 메인 -->
        <div id="main">
            <div class="main-top">
                <span>문민제</span>님의 목표 자산 포트폴리오
                <div class="pie-chart">
                    <Pie :data="chartData" :options="options" />
                </div>
                <hr>
            </div>
            <div id="port-select">
                    <button>목표 비율 설정</button>
                    <button>내 자산 입력</button>
            </div>  
            <div class="main-bottom">      
                <div>
                    <div class="my-box">
                        <table>
                            <thead>
                                <colgroup>
                                    <col width="10%" />
                                    <col width="40%" />
                                    <col width="10%" />
                                    <col width="40%" />
                                </colgroup>
                            </thead>
                            <tbody>
                                <tr v-for="(asset, index) in assets" :key="index">
                                    <td>{{ asset.name }}</td>
                                    <td><input type="text" class="percent" v-model="asset.percent" placeholder="%" /></td>
                                </tr>                          
                            </tbody>
                        </table>
                    </div>
                </div>
                <div id="save" @click=updatePort()>
                    <span>설정 완료</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script >
import axios from 'axios';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
    name: 'CreateView',
    components: {
        Pie
    },
    data() {
        return {
            assets: [
                { name: "주식", percent: "" },
                { name: "채권", percent: "" },
                { name: "실물자산", percent: "" },
                { name: "가상화폐", percent: "" },
            ],
            stock: '',
            bond: '',
            real_asset: '',
            crypto:'',
        }
    },
    computed:{
        chartData() {
            const assetNames = this.assets.map(asset => asset.name);
            const assetPrices = this.assets.map(asset => Number(asset.percent));
            return {
                labels: assetNames,
                datasets: [
                    {
                    backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                    data: assetPrices
                    }
                ],
            };
        },
    },
    methods: {
        updatePort() {
            const data = {
                stock: Number(this.stock),
                bond: Number(this.bond),
                real_asset: Number(this.real_asset),
                crypto: Number(this.crypto),
            };
            axios
                .post("http://127.0.0.1:8000/api/portfolio/", data)
                .then(() => {
                    alert('포트폴리오 반영');
                })
                .catch((error) => {
                    let errorMsg = "";
                });
        }
    }
    }
</script>

<style scoped>
tr:nth-child(odd) {
          background-color: #a5a5a5;
      }
    /* topbar */
    #top-wrapper {
        text-align: left;
        height: 30px;
        font-size: 15px;
        padding-left: 5px;
    }

    /* main */
    #main div {
        padding-top: 5px;
        font-size: 16px;
    }
    #main div span {
        font-weight: bold;
    }
    .main-top {
        text-align: center;
        height: 200px;
    }
    .pie-chart {
        display: inline-block;
        height: 150px;
        margin: 0;
    }
    .main-bottom {
        width: 100%;
    }
    #port-select  {
        text-align: center;
    }
    #port-select button {
        float: left;
        border-radius: 8px;
        background-color: transparent;
        font-size: 12px;
        width: 100px;
        height: 30px;
        margin-right: 10px;
    }
    .my-box table {
        width: 100%;
    }
    .my-box table th {
        text-align: left;
        padding-top: 10px;
    }

    .question {
        padding-right: 10px;
    }
    .percent {
        width: 100px;
        height: 25px;
    }
    #save {
        position: fixed;
        width: 100%;
        bottom: 43px;
        left: 0px;
        text-align: center;
        padding-bottom: 8px;
        background-color: #4868E1;
        margin-top: 15px;
        color: white;
    }
</style>