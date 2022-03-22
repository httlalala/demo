<template>
  <div id="app">
    <router-view></router-view>

  </div>
</template>

<script>
// // /*引入登录组件*/
// import Login from './components/loginin.vue'
export default {
  name: 'App',
  
  data() {
      return {
        activeName: 'second',
        info:null
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    },
    // components:{
    //   login:Login
    // }

}
</script>

<style>
#app {
  /* background-color: aqua; */
  display: flex;
  justify-content: flex-end;
  height: 100%;
  
}
html, body, div, ul, li, h1, h2, h3, h4, h5, h6, p, dl, dt, dd, ol, form, input, textarea, th, td, select {
    margin: 0;
    padding: 0;
}
html{
  height: 100%;
}
body{
  background: url('../src/assets/bg.png') no-repeat;
  /* background-color: rgb(237,237,237); */
  background-size: 100% 100%;
  height: 100%;
}
.title{
  margin-left: 20px;
  font-size: 100fr;
}
.container{
  background-color: #1aac74;
  width: 500px;
  height: 600px;
  margin-top: 100px;
  margin-right: 50px;
  box-sizing: border-box;
  border-radius: 20px;
  opacity: 0.9;
}
.header{
  /* height: 20px; */
  /* background-color: blueviolet; */
  font-size: 20px;
  padding: 0 40px;
  height: 200px;
}
el-tabs{
  font-size: 15px;
}
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
  padding: 0;
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
