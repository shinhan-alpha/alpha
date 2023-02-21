<template>
    <div class="container">
        <div id="top-wrapper">
            <font-awesome-icon icon="fa-solid fa-chevron-left" onclick=""/>
            <span>백테스트</span>
        </div>
        <!-- 메인 -->
        <div id="main">
            <div id="date">
                <span>기간:</span>
                <input type="text" value="날짜"/>

            </div>
            <div class="port">
                <table>
                    <thead>
                        <tr>
                            <th>자산명</th>
                            <th>자산비율</th>
                            <th>자산보유액</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>한국주식</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>미국주식</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>채권</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>현금</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>금</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>부동산</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                        <tr>
                            <td>가상화폐</td>
                            <td><input type="text"></td>
                            <td><input type="text"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {

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
    #date {
        text-align: left;
    }
    table, th, td {
        border: 1px solid #bcbcbc;
    }
    table {
        width: 320px;
    }
</style>