<template>
    <div class="login_container">
        <!-- <div class="t">课程管理系统</div> -->
        <div class="ti"><img src="../../src/assets/logo1.jpg" alt=""></div>
        <div class="tii"><img src="../../src/assets/logo2.jpg" alt=""></div>
       <div class="login_box">
           <h1 align="center" style="margin-bottom:5px">课程管理系统</h1>
            <el-tabs v-model="activeName" @tab-click="handleClick"  type="border-card">
                <el-tab-pane label="  教师登录  " name="first">
                    <span slot="label">
                        <div style="margin:0 60px 0 60px">教师登录 </div>
                    </span>
                    <div style="margin：20px 20px;">
                        <el-form :model="form" :rules="rules" ref="ruleForm" label-width="0px" class="login_form">
                            <el-form-item prop="username">
                                <el-input v-model="form.username" prefix-icon="el-icon-user"></el-input>
                            </el-form-item>
                            <el-form-item prop="password">
                                <el-input v-model="form.password" type="password" prefix-icon="el-icon-star-off"></el-input>
                            </el-form-item>
                            <el-form-item prop="school">
                                <!-- <el-dropdown split-button type="primary" style="width:100%; background-color:white;">
                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;请选择学校&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                    <el-dropdown-menu slot="dropdown">
                                        <el-dropdown-item>黄金糕</el-dropdown-item>
                                        <el-dropdown-item>狮子头</el-dropdown-item>
                                        <el-dropdown-item>螺蛳粉</el-dropdown-item>
                                    </el-dropdown-menu>
                                </el-dropdown> -->
                                <input id="type" type="text" list="typelist" placeholder="请选择学校" style="width:96%; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;" >
                                    <datalist id="typelist">
　　                                    <option>Dimond</option>
　　                                    <option>vertical</option>
                                    </datalist>
                                <!-- <el-input v-model="form.password" type="password" prefix-icon="el-icon-star-off" list="typelist"></el-input>
                                    <datalist id="typelist">
　　                                    <option>Dimond</option>
　　                                    <option>vertical</option>
                                    </datalist> -->
            

                            </el-form-item>
                            <div class="mima">
                                <div class="mimaleft">
                                    <input v-model="form.remember" type="checkbox" id="remember" checked>记住密码
                                </div>
                                <div class="mimaright">
                                    忘记密码？
                                </div>
                            </div>
                            <el-button type="primary" style="width:100%;" @click="login">登录</el-button>
                        </el-form>
                    </div>
                </el-tab-pane>
                <!-- <div class=""></div> -->
                <el-tab-pane label="管理员登录" name="second">
                    <span slot="label">
                        <div style="margin:0 60px 0 60px">管理员登录 </div>
                    </span>
                    <div style="margin：20px 20px;">
                        <el-form :model="form" :rules="rules" ref="ruleForm" label-width="0px" class="login_form">
                            <el-form-item prop="username">
                                <el-input v-model="form.username" prefix-icon="el-icon-user"></el-input>
                            </el-form-item>
                            <el-form-item prop="password">
                                <el-input v-model="form.password" type="password" prefix-icon="el-icon-star-off"></el-input>
                            </el-form-item>
                            <el-form-item prop="school">
                                <!-- <el-dropdown split-button type="primary" style="width:100%; background-color:white;">
                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;请选择学校&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                    <el-dropdown-menu slot="dropdown">
                                        <el-dropdown-item>黄金糕</el-dropdown-item>
                                        <el-dropdown-item>狮子头</el-dropdown-item>
                                        <el-dropdown-item>螺蛳粉</el-dropdown-item>
                                    </el-dropdown-menu>
                                </el-dropdown> -->
                                <input id="type" type="text" list="typelist" placeholder="请选择学校" style="width:96%; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;" >
                                    <datalist id="typelist">
　　                                    <option>Dimond</option>
　　                                    <option>vertical</option>
                                    </datalist>
                                <!-- <el-input v-model="form.password" type="password" prefix-icon="el-icon-star-off" list="typelist"></el-input>
                                    <datalist id="typelist">
　　                                    <option>Dimond</option>
　　                                    <option>vertical</option>
                                    </datalist> -->
            

                            </el-form-item>
                            <div class="mima">
                                <div class="mimaleft">
                                    <input v-model="form.remember" type="checkbox" id="remember" checked>记住密码
                                </div>
                                <div class="mimaright">
                                    忘记密码？
                                </div>
                            </div>
                            <el-button type="primary" style="width:100%;" @click="login">登录</el-button>
                        </el-form>
                    </div>
                </el-tab-pane>
            </el-tabs>
            <div class="login_foot">
                <div style="margin-right:20px">帮助</div>
                <div  style="margin-right:20px">隐私</div>
                <div>条款</div>
            </div>
            <div class="login_footer">
                <div>copyright</div>
                <div>2022无锡洛希极限科技有限公司</div>
            </div>
       </div>
    </div>
</template>

<script>
    // 引入base64
    const Base64 = require('js-base64').Base64
    export default {
        name:'Login',
        data() {
            return {
                activeName: 'second',
                form: {
                    username: '',
                    password: '',
                    school: '',
                    remember:''
                },
                rules: {
                    username: [
                    { required: true, message: '请输入名字', trigger: 'blur' },
                     { min:1, max: 11, smessage: '长度在 11 到 11 个字符', trigger: 'blur' }
                    ],
                    password: [
                    { required: true, message: '请输入密码', trigger: 'blur' },
                    { min: 1, max: 15, message: '长度在 1 到 15 个字符', trigger: 'blur' }
                    ],
                }
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
             // 获取cookie
            getCookie: function (key) {
                if (document.cookie.length > 0) {
                var start = document.cookie.indexOf(key + '=')
                if (start !== -1) {
                    start = start + key.length + 1
                    var end = document.cookie.indexOf(';', start)
                    if (end === -1) end = document.cookie.length
                    return unescape(document.cookie.substring(start, end))
                }
                }
                return ''
            },
            // 保存cookie
            setCookie: function (cName, value, expiredays) {
                var exdate = new Date()
                exdate.setDate(exdate.getDate() + expiredays)
                document.cookie = cName + '=' + decodeURIComponent(value) +
                ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString())
            },
            // 储存表单信息
            setUserInfo: function () {
                // 判断用户是否勾选记住密码，如果勾选，向cookie中储存登录信息，
                // 如果没有勾选，储存的信息为空
                if(this.form.remember){
                    console.log(this.form.username)
                    this.setCookie("username",this.form.username)
                    // base64加密密码
                    let passWord = Base64.encode(this.form.password)
                    this.setCookie("remember",passWord)    
                }else{
                    this.setCookie("username","")
                    this.setCookie("password","") 
                } 
            },
            login(){
                
                this.$refs.ruleForm.validate(valid=>{
                    // console.log(valid)
                    // console.log(this.form.scool)
                    if(!valid) return;
                    // //记住密码功能实现
                    // const result=await this.$http.post('http://47.97.193.46:8001/users/login/',{username:this.form.username,password:this.form.password})
                    // // console.log(result.data)
                    // if(result ==null) return;
                    // this.$message.success("登录成功");
                    // //储存到cookie中
                    // this.setCookie('token',result.data.token)
                    // //将token存储到sessionStorage中
                    // window.sessionStorage.setItem("token",result.data.token);
                    // window.sessionStorage.setItem("username",result.data.username);
                    // window.sessionStorage.setItem("user_id",result.data.user_id);
                    // //通过编程式导航跳转到后台主页
                    // this.$router.push('/Main')
                    // // 储存登录信息
                    // this.setUserInfo()
                    this.$http.post('http://47.97.193.46:8001/users/login/',{username:this.form.username,password:this.form.password})
                    .then(result=>{
                        if(result ==null) return;
                        this.$message.success("登录成功");
                        //储存到cookie中
                        this.setCookie('token',result.data.token)
                        // this.setCookie('username',result.data.username)
                        //将token存储到sessionStorage中
                        window.sessionStorage.setItem("token",result.data.token);
                        window.sessionStorage.setItem("username",result.data.username);
                        window.sessionStorage.setItem("user_id",result.data.user_id);
                        //通过编程式导航跳转到后台主页
                        this.$router.push('/Main')
                        // 储存登录信息
                        this.setUserInfo()
                    }).catch(err=>{
                        this.$message.error('用户名或密码错误')
                    })


                     
                })
            },
        },
        mounted(){
                let account = this.getCookie("username")
                let password = Base64.decode(this.getCookie("remember"))
                // 如果存在赋值给表单，并且将记住密码勾选
                console.log(11)
                if(account){
                    this.form.username = account
                    this.form.password = password
                    this.form.remember = true
                }
            }
    }
</script>

<style scoped>
.login_container{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    align-self: flex-start;
}
/* .t{
    position: absolute;
    top: 80px;
    right: 250px;
    font-size: 40px;
} */
.ti img{
    position: absolute;
    left: 100px;
    top: 50px;
    width: 700px;
    height: 550px;
}
.tii img{
    position: absolute;
    bottom: 50px;
    left:10px;
    width: 160px;
    height: 50px;
}
.login_box{
    margin-top: -40px;
    /* background-color: #1aac74; */
    opacity: 0.9;
    width: 450px;
    height: 500px;
    position: absolute;
    top:17%;
    left: 60%;
    /* margin-top: 120px;
    margin-right: 150px; */
    border-radius: 20px;
    padding: 20px 30px;
}
.login_form{
    padding: 20px 60px;
}
.el-dropdown {
    vertical-align: top;
    background-color: white;
}
.mima{
  display: flex;
  align-content: space-between;
  /* background-color: violet; */
  float: left;
  width: 300px;
  font-size: 15px;
  margin-top: -5px;
  margin-bottom: 20px;

}

.mimaleft{
  margin-right: 150px;
  float:right;
}
.mimaright{
    color: rgb(115,183,253);
}
.login_foot{
    display: flex;
    justify-content: center;
    margin-top: 20px;
    align-items: center;
    color: #aaaaaa;

}
.login_footer{
    display: flex;
    justify-content: center;
    margin-top: 20px;
    align-items: center;
    color: #aaaaaa;
}
</style>