<template>
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
</template>

<script scoped>
//存在跨域问题需要使用token来维持登录状态，不存在则用cookie和seesion
    export default {
        name:'Login'
    }
</script>

<style>
.isform{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  /* background-color: yellow; */
  width: 400px;
}
.input{
  border: 1px solid #cccccc;
  background-color: white;
  padding-left: 5px;
  margin-top: 20px;
  width: 300px;
}
input:focus{   
	border:none;
  outline: none;
}
.mima{
  display: flex;
  align-content: space-between;
  /* background-color: violet; */
  margin-top: 20px;
  float: left;
  width: 300px;
  font-size: 15px;

}

.mimaleft{
  margin-right: 110px;
  float:right;
}
.loginbtn{
  width: 300px;
  background-color: blue;
  margin-top: 20px;
  color: white;
}
</style>