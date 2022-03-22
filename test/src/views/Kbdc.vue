<template>
    <div class="con" style="position:relative;">
       <div class="con1" style="margin-left:110px;">
           <div>选出导课周次:</div>
            <div style=" margin-left: 30px;">
               <div class="block" style="display:inline">
                <el-date-picker
                v-model="value3"
                type="date"
                placeholder="开始时间">
                </el-date-picker>
                </div>
                <div style="display:inline">至</div>
                <div class="block" style="display:inline">
                <el-date-picker
                v-model="value4"
                type="date"
                placeholder="结束时间">
                </el-date-picker>
                </div>
           </div>
           <div style=" margin-left: 30px;"><el-button type="success" style="background-color: rgb(195,231,255);border:none">全部周次</el-button></div>
       </div>
       <div class="con2" style="margin-left:140px;">
           <div>导出课表：</div>
           <el-switch
            v-model="value1"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>

       </div>
       <div class="con3" style="margin-left:60px;">
           <div>导出调代课历史记录：</div>
           <el-switch
            v-model="value2"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
       </div>
       <div class="con4" style="margin-left:140px;">点击下载：<a href="https://c-ssl.duitang.com/uploads/blog/202108/21/20210821113422_38b30.thumb.1000_0.jpg_webp" download="template"><svg t="1646822323176" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3553" width="50" height="50"><path d="M1024 748.544q0 25.6-8.704 48.128t-24.064 40.96-36.352 30.208-45.568 15.872l0 2.048-21.504 0-1.024 0-664.576 0q-2.048 0-2.56 0.512t-2.56 0.512-3.072-0.512-3.072-0.512l-6.144 0 0-1.024q-43.008-2.048-80.384-19.456t-65.024-46.592-43.52-67.584-15.872-81.408 15.872-80.896 43.008-66.56 63.488-47.104 78.336-21.504q7.168-66.56 36.864-124.416t76.288-100.864 107.008-67.584 129.024-24.576q72.704 0 137.216 27.648t112.128 75.776 75.264 112.128 27.648 136.704q0 32.768-6.144 64t-17.408 59.904q2.048 0 4.608-0.512t4.608-0.512q28.672 0 53.248 10.752t43.008 29.184 29.184 43.52 10.752 53.76zM687.104 596.992q12.288-20.48 7.168-23.552t-25.6-3.072q-12.288 0-34.304-0.512t-33.28-0.512q-16.384 0-20.992-13.312t-4.608-36.864q0-32.768-0.512-52.736t-0.512-43.52q0-26.624-3.584-38.912t-29.184-12.288q-18.432 0-27.648 0.512t-25.6 0.512q-27.648 0-34.304 15.872t-6.656 31.232l0 32.768q0 13.312 0.512 25.6t0.512 25.6l0 29.696q0 16.384-4.096 25.088t-19.456 8.704q-6.144 1.024-16.896 1.536t-22.016 1.024-21.504 0.512l-16.384 0q-21.504 0-25.6 13.312t13.312 33.792q17.408 21.504 37.376 46.592t39.424 50.688 37.376 49.664 33.28 41.472q27.648 30.72 53.248-1.024 15.36-17.408 35.84-45.056t41.984-57.856 40.96-58.368 31.744-46.592z" p-id="3554" fill="#4E7708"></path></svg></a></div>
        <div style="display:flex;flex-direction:column;position:absolute;top:120px;right:100px;">
           <img @mouseenter="onMouseoverEnvDelBtn($event)"
                @mouseleave="onMouseleaveEnvDelBtn($event)"
            src="../assets/xcx1.jpg" alt="" style="width:70px;height:80px;margin-right:80px;">
           <img  class="xcx" src="../assets/xcx2.jpg" alt="" style="width:150px;height:150px;margin-top:20px;display:none;">
       </div>
    </div>
    
</template>

<script>
    export default {
        name:'Kbdc',
        data() {
            return {
                value1: true,//导出课表
                value2: true,//导出调代课记录
                value3:'',//开始时间
                value4:'',//结束时间
                 
            }
        },
        methods:{
            onMouseoverEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:block"
            },
            onMouseleaveEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:none"
            },
        }
    }
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}
.con{
    display: flex;
    /* justify-content: flex-start; */
    flex-direction: column;
}
.con1{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
.con2{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
.con3{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
.con4{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
</style>