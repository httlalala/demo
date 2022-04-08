<template>
    <div class="dpgl">
        <div class="dpgl1"><span style="margin-left:200px;">蒋王小学智慧屏</span></div>
        <div class="dpgl2">
            <div style="margin-left:60px;">
                <table border="1" cellpadding="10" width="100%">
                    <tr style="height: 20px; line-height: 20px;">
                        <th colspan="2">时间\日期</th>
                        <th>一</th>
                        <th>二</th>
                        <th>三</th>
                        <th>四</th>
                        <th>五</th>
                    </tr>

                    <tr style="height: 20px; line-height: 20px;">
                        <th rowspan="5">上午</th>
                        <th style="height:10px;line-height: 10px;">08:20-08:30</th>
                        <th colspan="5" style="height:5px;line-height: 5px;">晨会</th>
                    </tr>
                     <tr style="height: 20px; line-height: 20px;">
                       <th>9:30-10:15</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>

                    <tr style="height: 20px; line-height: 20px;">
                        <th>10:25-11:10</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>
                     <tr style="height: 20px; line-height: 20px;">
                        <th  style="height:5px;line-height: 5px;">10:25-11:10</th>
                        <th colspan="5"  style="height:5px;line-height: 5px;">大课间活动</th>
                    </tr>
                     <tr style="height: 20px; line-height: 20px;">
                        <th>10:25-11:10</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>

                    <tr style="height: 5px; line-height: 5px;">
                    <th colspan="7">阅读、午休</th>
                    </tr>

                    <tr style="height: 20px; line-height: 20px;">
                        <th rowspan="3">下午</th>
                        <th>14:30-15:15</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>

                    <tr style="height: 20px; line-height: 20px;">
                        <th>15:25-16:10</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>
                    <tr style="height: 20px; line-height: 20px;">
                        <th>15:25-16:10</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>
                     <tr style="height: 20px; line-height: 20px;">
                        <th></th>
                        <th>15:25-16:10</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>
                    <tr style="height: 20px; line-height: 20px;">
                        <th></th>
                        <th></th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                        <th>语文</th>
                    </tr>
                </table>
            </div>
            <div style="margin-left:40px;margin-top:-73px;">
                <div>
                    <h4 style="margin-left:-300px;">班级公告栏：</h4>
                    <div style="background-color:rgb(234,234,234);width:550px;height:200px;margin-top:-60px;border:1px solid #aaa"></div>
                </div>
                <div>
                    <h4 style="margin-left:-300px;margin-top:-69px;">班级值日表：</h4>
                    <div style="background-color:rgb(234,234,234);width:550px;height:200px;margin-top:-60px;border:1px solid #aaa"></div>
                </div>
            </div>
        </div>
    </div>        
</template>

<script>
    export default {
        name:'Dpgl'
    }
</script>

<style scoped>
.dpgl{
    width: 100%;
    height: 100%;
    background-color: white;
    display: grid;
    justify-content: start;
    grid-template-rows: 20% 80%;
    border:1px solid #aaa
}
.dpgl1{
    font-size: 30px;
    color: #859F3E;
    font-weight: bolder;
}
.dpgl2{
    display: flex;
    justify-content: space-between;

}
tr{ width: 100px;
    /* height: 20px;
    line-height: 20px; */
}
table{
    border-collapse:collapse;
    border:none;
    font-size: 5px;
    /* margin-top: 10px; */
}
tr{
    border: 1px solid #0094ff;
}
th{
    padding: 10px 20px;
    border: 1px solid #ccc;
}
</style>