<template>
    <div id="menu-wrapper">
            <table>
                <tr>
                    <th id="menu-tab"><a href=""><font-awesome-icon icon="fa-solid fa-bars" /></a></th>
                    <th><a href="#">홈</a> </th>
                    <th><a href="#">관심<br>종목</a></th>
                    <th><a href="current.html">현재가</a></th>
                    <th><a href="#">주식<br>주문</a></th>
                    <th><a href="#">주식<br>잔고</a></th>
                    <th><a href="#">종합<br>차트</a></th>
                    <th><a href="#">지수환율<br>시장지표</a></th>
                    <th><a href="#">매매<br>동향</a></th>
                    <th><a href="#">즉시<br>이체</a></th>
                    <th><a href="#">총자산<br>현황</a></th>
                </tr>
            </table>
    </div>
</template>

<script>
    export default { }
</script>


<style>
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