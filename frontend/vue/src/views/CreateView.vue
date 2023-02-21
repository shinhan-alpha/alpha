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
                    <Pie :data="data" :options="options" />
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
                                <tr>
                                    <th><input type="checkbox" v-model="isChecked" @click="asd()"/></th>  
                                    <th><span>주식</span></th>                          
                                    <th class="question" onclick=""><font-awesome-icon icon="fa-solid fa-circle-question" /></th>
                                    <th><input type="text" class="percent" v-model="stock"  placeholder="%"></th>
                                </tr> 
                                <tr>
                                    <th><input type="checkbox"/></th>  
                                    <th><span>채권</span></th>                          
                                    <th class="question" onclick=""><font-awesome-icon icon="fa-solid fa-circle-question"/></th>
                                    <th><input type="text" class="percent" v-model="bond" placeholder="%"></th>
                                </tr>
                                <tr>
                                    <th><input type="checkbox"/></th>  
                                    <th><span>실물자산</span></th>                          
                                    <th class="question" onclick=""><font-awesome-icon icon="fa-solid fa-circle-question"/></th>
                                    <th><input type="text" class="percent" v-model="realasset" placeholder="%"></th>
                                </tr>
                                <tr>
                                    <th><input type="checkbox"/></th>  
                                    <th><span>가상화폐</span></th>                          
                                    <th class="question" onclick=""><font-awesome-icon icon="fa-solid fa-circle-question"/></th>
                                    <th><input type="text" class="percent" v-model="cryptocurrency" placeholder="%"></th>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div id="save" onclick="">
                    <span>설정 완료</span>
                </div>
            </div>
        </div>
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
        data: {
            isChecked: false,
            stock: '',
            datasets: [
            {
                backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                data: [80, 50, 50, 50]
            }
            ]
        },
        methods: {
            asd() {
                console.log(this.stock)
            }
        }
        }
    }
    }
</script>

<style scoped>
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