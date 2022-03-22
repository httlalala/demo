<template>
  <div class="container">
       <div class="header">
         <el-tabs v-model="activeName" @tab-click="handleClick" >
          <el-tab-pane label="教师登录" name="first" style="width:50%">
            <form action="" class="isform">
              <div class="input">
                 <i class="el-icon-user"></i>
              <input type="text" placeholder=" 账户" style="border:none;height:100%">
              </div>
              <div class="input">
                 <i class="el-icon-star-off"></i>
              <input type="password" placeholder="密码" style="border:none;height:100%">
              </div>
              <div class="input">
                 <i class="el-icon-location-outline"></i>
              <input type="text" placeholder=" 学校" style="border:none;height:100%">
              </div>
              <div class="mima">
                <div class="mimaleft">
                  <input type="checkbox" id="remember">记住密码
                </div>
                <div class="mimaright">
                  忘记密码？
                </div>
              </div>
              <div class="loginbtn">
                <button style="width:100%;height:34px;background-color: blue;color:white;">登录</button>
              </div>
            </form>
          </el-tab-pane>
          <el-tab-pane label="管理员登录" name="second" ><login></login></el-tab-pane>
         </el-tabs>
       </div>
      <div class="middle"></div>
      <div class="footer"></div>
    </div>
</template>

<script>
// /*引入登录组件*/
import Login from '@/components/loginin.vue'
export default {
  name: 'HelloWorld',
  data () {
    return {
     
    }
  },
  components:{
    login:Login
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
  

