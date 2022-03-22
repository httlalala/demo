<template>
    <div style="position:relative;">
        <div class="container">
        <div class="head">教师搜索</div>
        <div class="mid">
            <div class="mid1">搜索姓名<el-input v-model="inputxm" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div>搜索学校<el-input v-model="inputxx" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div  class="mid2">搜索手机号<el-input v-model="inputsj" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div>
                <el-button type="primary">搜索</el-button>
                <el-button type="primary" style="color:#cccccc;background-color:white;border:1px solid #cccccc;">清除</el-button>
            </div>
        </div>
        <div class="foot">2</div>
         <div style="display:flex;flex-direction:column;position:absolute;top:120px;right:100px;">
           <img @mouseenter="onMouseoverEnvDelBtn($event)"
                @mouseleave="onMouseleaveEnvDelBtn($event)"
            src="../assets/xcx1.jpg" alt="" style="width:70px;height:80px;margin-right:80px;">
           <img  class="xcx" src="../assets/xcx2.jpg" alt="" style="width:150px;height:150px;margin-top:20px;display:none;">
       </div>
        </div>
    </div>
</template>

<script>
    export default {
        name:'Njglysd',
        data(){
            return{
                inputxm:'',
                inputxx:'',
                inputsj:''
            }
        },
        methods:{
            onMouseoverEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:block"
            },
            onMouseleaveEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:none"
            },
        },
        
    }
</script>

<style>
.container{
    background-color: white;
    width: 70%;
    height: 80%;
    display: flex;
    flex-direction: column;
    margin:20px 30px;
    padding: 10px;
}
.head{
    /* background-color: yellow; */
    width: 100%;
    height: 50px;
    display: flex;
    align-content: flex-start;
    align-items: center;
    font: bolder;
    font-size: 20px;
}
.mid{
    display: grid;
    grid-template-columns: 40% 40%;
    grid-template-rows: 40% 40%;
    grid-column-gap: 20px;

}
.mid1{
    display: flex;
    justify-content: flex-start;
}
.mid2{
    display: flex;
    justify-content: flex-start;
}
</style>