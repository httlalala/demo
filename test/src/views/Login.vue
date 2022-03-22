<template>
    <div class="login_container">
        <div class="t">课程管理系统</div>
        <div class="ti"><img src="../../src/assets/logo1.jpg" alt=""></div>
        <div class="tii"><img src="../../src/assets/logo2.jpg" alt=""></div>
       <div class="login_box">
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
                                    <input type="checkbox" id="remember" checked>记住密码
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
                <el-tab-pane label="管理员登录" name="second" style="width:30%">
                     <span slot="label">
                        <div style="margin:0 60px 0 60px">管理员登录 </div>
                    </span>
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
    export default {
        name:'Login',
        data() {
            return {
                activeName: 'second',
                form: {
                    username: '',
                    password: '',
                    school: '',
                },
                rules: {
                    username: [
                    { required: true, message: '请输入名字', trigger: 'blur' },
                     { min: 11, max: 11, message: '长度在 11 到 11 个字符', trigger: 'blur' }
                    ],
                    password: [
                    { required: true, message: '请输入密码', trigger: 'blur' },
                    { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
                    ],
                }
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
            login(){
                this.$refs.ruleForm.validate(async valid=>{
                    console.log(valid)
                    if(!valid) return;
                    const reslut=await this.$axios.post("login",this.form);
                    console.log(reslut)
                })
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
.t{
    position: absolute;
    top: 80px;
    right: 250px;
    font-size: 40px;
}
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
    margin-top: 10px;
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