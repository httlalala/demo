<template>
  <el-container style="height:100%;">
  <el-header>
      <div class="left" style="color:rgb(0,156,63); font-size:30px;"><img src="../../src/assets/logo3.jpg" alt="" style="width:;200px;height:65px;"></div>
      <div class="middle" style="margin-left:-200px;">
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" 
          background-color="rgb(195,231,255)"
          text-color="#fff"
          active-text-color="#fff">
            <el-menu-item index="1" style="border-radius:20px;">代课管理</el-menu-item>
            <el-menu-item index="2" style="border-radius:20px;">申请信息</el-menu-item>
            <el-menu-item index="3" style="border-radius:20px;">历史记录</el-menu-item>
            <el-menu-item index="4" style="border-radius:20px;">年级管理</el-menu-item>
         </el-menu>
         <div class="line"></div>
      </div>
      <div class="right">
          <div style=" padding: 5px;">
              <i class="el-icon-question"></i>帮助
          </div>
          <div  style=" padding: 5px;">
              <i class="el-icon-s-tools"></i>设置
          </div>
          <div style=" padding: 5px;">
              <i class="el-icon-s-comment"></i>消息
          </div>
          <div style=" padding: 5px;display:flex;align-items: center;">
              <img src="@/assets/bg.jpg" style="width:20px;height:20px;border-radius:20px;,margin-right:10px;background-color:#ccc"/>
              <span style="margin-left:3px">张三</span>
          </div>
      </div>
  </el-header>
  <el-container>
    <el-aside width="200px" style="background-color:#859F3E">
        <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse"
        background-color="#859F3E"
          text-color="#fff"
          active-text-color="#fff">
            <el-submenu index="1" style="margin-left:-50px;">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span slot="title">教务管理</span>
                </template>
                <el-menu-item index="1-1" @click="clickkbgx" style="margin-left:35px;">课表更新</el-menu-item>
                <el-menu-item index="1-2" @click="clickkbdc" style="margin-left:35px;">课表导出</el-menu-item>
                <el-menu-item index="1-3" @click="clickxqrqsd" style="margin-left:55px;">学期日期设定</el-menu-item>
                <el-menu-item index="1-4" @click="clicknjglysd" style="margin-left:60px;">年级管理员设定</el-menu-item>
            </el-submenu>
            <el-submenu index="2" style="margin-left:-50px;">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span slot="title" @click="clickdpgl">大屏管理</span>
                </template>
            </el-submenu>
         <!-- <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title" @click="clickdpgl">大屏管理</span>
         </el-menu-item> -->
    </el-menu>
    </el-aside>
    <el-container>
      <el-main><router-view></router-view></el-main>
      <el-footer style="height:150px; line-height:150px" class="main_footer">
        <div>Copyright©Copyright©https:luoxilimt.com</div>
        <div class="footer_right">
          <div><svg style="width:30px;height:60px" t="1647262760439" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5557" width="200" height="200"><path d="M896 96L896 928a53.393333 53.393333 0 0 1-53.333333 53.333333L181.333333 981.333333a53.393333 53.393333 0 0 1-53.333333-53.333333l0-832a53.393333 53.393333 0 0 1 53.333333-53.333333l661.333334 0a53.393333 53.393333 0 0 1 53.333333 53.333333zM170.666667 927.99999999a10.666667 10.666667 0 0 0 10.666666 10.66666701l661.333334 0a10.666667 10.666667 0 0 0 10.666666-10.66666701l0-831.99999998a10.666667 10.666667 0 0 0-10.666666-10.66666701L181.333333 85.333333a10.666667 10.666667 0 0 0-10.666666 10.66666701z" fill="#bfbfbf" p-id="5558"></path></svg></div>
          <div >公众号</div>
        </div>
         <div class="footer_right">
          <div><svg style="width:30px;height:60px" t="1647262760439" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5557" width="200" height="200"><path d="M896 96L896 928a53.393333 53.393333 0 0 1-53.333333 53.333333L181.333333 981.333333a53.393333 53.393333 0 0 1-53.333333-53.333333l0-832a53.393333 53.393333 0 0 1 53.333333-53.333333l661.333334 0a53.393333 53.393333 0 0 1 53.333333 53.333333zM170.666667 927.99999999a10.666667 10.666667 0 0 0 10.666666 10.66666701l661.333334 0a10.666667 10.666667 0 0 0 10.666666-10.66666701l0-831.99999998a10.666667 10.666667 0 0 0-10.666666-10.66666701L181.333333 85.333333a10.666667 10.666667 0 0 0-10.666666 10.66666701z" fill="#bfbfbf" p-id="5558"></path></svg></div>
          <div >微博</div>
        </div>
         <div class="footer_right">
          <div><svg style="width:30px;height:60px" t="1647262760439" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5557" width="200" height="200"><path d="M896 96L896 928a53.393333 53.393333 0 0 1-53.333333 53.333333L181.333333 981.333333a53.393333 53.393333 0 0 1-53.333333-53.333333l0-832a53.393333 53.393333 0 0 1 53.333333-53.333333l661.333334 0a53.393333 53.393333 0 0 1 53.333333 53.333333zM170.666667 927.99999999a10.666667 10.666667 0 0 0 10.666666 10.66666701l661.333334 0a10.666667 10.666667 0 0 0 10.666666-10.66666701l0-831.99999998a10.666667 10.666667 0 0 0-10.666666-10.66666701L181.333333 85.333333a10.666667 10.666667 0 0 0-10.666666 10.66666701z" fill="#bfbfbf" p-id="5558"></path></svg></div>
          <div >15639115236</div>
        </div>
         <div class="footer_right">
          <div><svg style="width:30px;height:60px" t="1647262760439" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5557" width="200" height="200"><path d="M896 96L896 928a53.393333 53.393333 0 0 1-53.333333 53.333333L181.333333 981.333333a53.393333 53.393333 0 0 1-53.333333-53.333333l0-832a53.393333 53.393333 0 0 1 53.333333-53.333333l661.333334 0a53.393333 53.393333 0 0 1 53.333333 53.333333zM170.666667 927.99999999a10.666667 10.666667 0 0 0 10.666666 10.66666701l661.333334 0a10.666667 10.666667 0 0 0 10.666666-10.66666701l0-831.99999998a10.666667 10.666667 0 0 0-10.666666-10.66666701L181.333333 85.333333a10.666667 10.666667 0 0 0-10.666666 10.66666701z" fill="#bfbfbf" p-id="5558"></path></svg></div>
          <div >微信小程序</div>
        </div>
      </el-footer>
    </el-container>
  </el-container>
</el-container>
</template>

<script>

    export default {
        name:'Main',
        data(){
          return{
            activeIndex:'4'
          }
        },
        methods: {
            handleOpen(key, keyPath) {
            console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
            console.log(key, keyPath);
            },
            clickkbgx(){
                this.$router.push({
                    name:'Kbgx'
                })
            },
            clickkbdc(){
                this.$router.push({
                    name:'Kbdc'
                })
            },
            clickxqrqsd(){
                this.$router.push({
                    name:'Xqrqsd'
                })
            },
             
            clicknjglysd(){
                this.$router.push({
                    name:'Njglysd'
                })
            },
             clickdpgl(){
                this.$router.push({
                    name:'Dpgl'
                })
            },

        }
    }
</script>

<style>
 html,body {
      margin: 0;
      height: 100%;
    }
.el-header{
    background-color: rgb(195,231,255);
    color: #333;
    text-align: center;
    line-height: 60px;
    display: flex;
    justify-content:  space-between ;
    
  }
  .el-footer {
    background-color: white;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
 .el-menu {
      border: none;
    }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
    height: 800px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
  .right{
      display: flex;
      justify-content: center;
      align-items: center;
      color: #666;
  }
  .el-menu-item.is-active {
      background-color: #859F3E !important;
      color: #fff;
    }
.main_footer{
  display: grid;
  grid-template-columns: 500px 100px 100px 100px 100px;
  justify-items:stretch;
  column-gap:40px;
  justify-content:space-between;
}
.footer_right{
  display: grid;
   grid-template-rows: 10px 30px;
   justify-content:center;
}
</style>
