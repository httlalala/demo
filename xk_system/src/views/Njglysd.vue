<template>
    <div style="position:relative;">
        <div class="container">
        <div class="head">教师搜索</div>
        <div class="mid">
            <div class="mid1">搜索姓名<el-input v-model="inputxm" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div>搜索学校<el-input v-model="inputxx" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div  class="mid2">搜索手机号<el-input @blur="get_school" id="getphone" v-model="inputsj" placeholder="请输入内容" style="width:200px;margin-left:20px;"></el-input></div>
            <div>
                <el-button type="primary" @click="sousuo">搜索</el-button>
                <el-button type="primary" @click="qingchu" style="color:#cccccc;background-color:white;border:1px solid #cccccc;">清除</el-button>
            </div>
        </div>
        <div class="foot">
             <el-table
                :data="tableData.slice((currpage - 1) * pagesize, currpage * pagesize)"
                border
                style="width: 100%">
                <el-table-column
                prop="username"
                label="用户名"
                width="150">
                </el-table-column>
                <el-table-column
                prop="school_name"
                label="学校"
                width="200">
                </el-table-column>
                <el-table-column
                prop="identity"
                label="当前身份"
                width="136">
                </el-table-column>
                <el-table-column
                prop="phone"
                label="手机号"
                width="120">
                </el-table-column>
                <el-table-column
                prop="create_time"
                label="注册日期"
                width="300">
                </el-table-column>
                <el-table-column
                label="操作"
                width="220">
                <template slot-scope="scope">
                    <el-button @click="chakan(scope.row)" type="text" size="small" >查看信息</el-button>
                    <el-button @click="quanxian(scope.row)" type="text" size="small">权限编辑</el-button>
                </template>
                </el-table-column>
            </el-table>
            <div style="margin-top:20px;">
                <el-pagination
                background
                layout="prev, pager, next"
                :page-size="pagesize"
                @current-change="handleCurrentChange" 
			    @size-change="handleSizeChange" 
                :total="tableData.length">
                </el-pagination>
            </div>
        </div>
         <div style="display:flex;flex-direction:column;position:absolute;top:120px;right:100px;">
           <img @mouseenter="onMouseoverEnvDelBtn($event)"
                @mouseleave="onMouseleaveEnvDelBtn($event)"
            src="../assets/xcx1.jpg" alt="" style="width:70px;height:80px;margin-right:80px;">
           <img  class="xcx" src="../assets/xcx2.jpg" alt="" style="width:150px;height:150px;margin-top:20px;display:none;">
       </div>
       <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
       <div style="margin-top:-20px">
            <input id="power" type="text" list="quanxianlist" placeholder="请选择身份" style="margin-top:-30px;width:96%; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;" >
                <datalist id="quanxianlist" style="width:500px;">
　　                <option>一年级管理员</option>
　　                <option>二年级管理员</option>
                    <option>三年级管理员</option>
                    <option>四年级管理员</option>
                    <option>五年级管理员</option>
                    <option>六年级管理员</option>
                    <option>总管理员</option>
                    <option>教师</option>
                </datalist>
       </div>
        <span slot="footer" class="dialog-footer">
            <el-button @click="quanxiancancel">取 消</el-button>
            <el-button type="primary" @click="quanxianconfirm">确 定</el-button>
        </span>
        </el-dialog>
        <el-dialog
            title="详细信息"
            :visible.sync=" dialogTableVisible"
            width="30%"
            :before-close="handleClose">
            <div class="xiangxi">
                <div class="xiangxi_left">
                    <div class="xingming"><div>姓名：{{xiangxi_username}}</div></div>
                    <div>创建时间：{{xiangxi_create_time}}</div>
                    
                </div>
                <div class="xiangxi_right">
                    <div class="yonghuleixing">用户类型：{{xiangxi_identity}}</div>
                    <div>电话：{{xiangxi_phone}}</div>
                </div>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogTableVisible=false">取 消</el-button>
                <el-button type="primary" @click="dialogTableVisible=false">确 定</el-button>
            </span>
        </el-dialog>
       <!-- <div class="quanxian popContainer" v-if="isShow">
            <input id="power" type="text" list="quanxianlist" placeholder="请选择身份" style="width:96%; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;" >
                <datalist id="quanxianlist">
　　                <option>一年级管理员</option>
　　                <option>二年级管理员</option>
                    <option>三年级管理员</option>
                    <option>四年级管理员</option>
                    <option>五年级管理员</option>
                    <option>六年级管理员</option>
                    <option>总管理员</option>
                    <option>教师</option>
                </datalist>
            <el-button type="primary" @click="quanxianconfirm">确定</el-button>
            <el-button  @click="quanxiancancel">取消</el-button>
       </div> -->
        </div>
    </div>
</template>

<script>
    export default {
        name:'Njglysd',
        data(){
            return{
                inputxm:'',
                inputxx:'11',
                inputsj:'',
                tableData:'',
                item:1,
                isShow:false,
                change_id:'',
                dialogVisible:false,
                dialogTableVisible: false,
                gridData:'',//详细信息
                //详细信息
                xiangxi_username:'',
                xiangxi_create_time:'',
                xiangxi_identity:'',
                xiangxi_phone:'',
                pagesize: 3,
				currpage: 1,

                
            }
        },
        methods:{
            onMouseoverEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:block"
            },
            onMouseleaveEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:none"
            },
            get_school(){
                const phone=document.getElementById("getphone").value
                console.log(phone)
            },
             //搜索教师信息
            sousuo(){
                console.log(111111)
                const username=this.$data.inputxm
                const iphone=this.$data.inputsj
                const token=window.sessionStorage.getItem("token")
                this.$http.get('http://47.97.193.46:8001/users/',{
                headers:{
                    'Authorization':'JWT '+ token
                },
                params:{
                    username:username,
                    phone:iphone
                }
                }).then(res=>{
                    console.log(res.data.results)
                    this.$data.tableData=res.data.results
                    // this.$data.gridData=res.data.results
        
                })
            },
            //分页
            handleCurrentChange(cpage) {
                this.currpage = cpage;
			},
			handleSizeChange(psize) {
				this.pagesize = psize;
            },
            qingchu(){
                this.$data.tableData=''
            },
            //权限编辑
            handleClose(done) {
                this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
            },
            chakan(row) {
                console.log(row)
                this.$data.xiangxi_username=row.username
                this.$data.xiangxi_create_time=row.create_time
                this.$data.xiangxi_identity=row.identity
                this.$data.xiangxi_phone=row.phone
                this.$data.dialogTableVisible=true
                console.log(row.xiangxi_create_time)
                
            },
            quanxian(row) {
                this.$data.change_id=row.id
                this.$data.isShow=true
                this.$data.dialogVisible=true
                // this.$alert('<el-tag>标签一</el-tag>', '标题名称', {
                //     confirmButtonText: '确定',
                //     callback: action => {
                //         this.$message({
                //         type: 'info',
                //         message: `action: ${ action }`
                //         });
                //     }
                // });
            },
            quanxianconfirm(){
                var quanxian=document.getElementById('power').value
                const token=window.sessionStorage.getItem("token")
                const change_id=this.$data.change_id
                console.log(change_id)
                console.log(quanxian)
                if(quanxian=='一年级管理员'){
                    quanxian=1
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }else if(quanxian=='二年级管理员'){
                    quanxian=2
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }else if(quanxian=='三年级管理员'){
                    quanxian=3
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }
                else if(quanxian=='四年级管理员'){
                    quanxian=4
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }
                else if(quanxian=='五年级管理员'){
                    quanxian=5
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }
                else if(quanxian=='六年级管理员'){
                    quanxian=6
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }
                else if(quanxian=='总管理员'){
                    quanxian=1
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_super:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }else if(quanxian=='教师'){
                    quanxian=0
                    this.$http.put('http://47.97.193.46:8001/users/'+change_id+'/',
                    {
                        is_grade:quanxian
                    },
                    {
                        headers:{
                            'Authorization':'JWT '+ token
                        },
                    }
                        ).then(res=>{
                            console.log(res)
                    })
                }
                console.log(quanxian)
                 this.$data.dialogVisible=false
                this.$data.isShow=false
                  this.$message({
                    message:  '操作成功',
                    type: 'success'
                });

            },
            quanxiancancel(){
                this.$data.dialogVisible=false
            },
        },

        mounted(){
            const token=window.sessionStorage.getItem("token")
            const user_id=window.sessionStorage.getItem("user_id")
            const username=this.$data.inputxm
            const iphone=this.$data.inputsj

            const school_name=this.$data.inputxx
            this.$http.get('http://47.97.193.46:8001/users/'+user_id+'/',{
            headers:{
                'Authorization':'JWT '+ token
            },
            params:{
                'pk':user_id
            },
            }).then(res=>{
                console.log(res.data)
                console.log(res.data.school_name)
                console.log(this.$data.inputxx)
                this.$data.inputxx=res.data.school_name
            })
        }
        
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
    margin-left: 20px;
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
    margin-left: 40px;
}
.mid2{
    display: flex;
    justify-content: flex-start;
    margin-left: 40px;
}
.quanxian{
    background-color: white;
    width: 250px;
    height: 400px;
    position: fixed;
    margin: 10% 25%;
    border: 1px solid #ccc;
    padding: 30px;
    /* display: none; */
}
.el-dialog__body{
    margin-top: -100px;
    padding: 0;
    /* background-color: yellow; */
    height: 300px;
}
.xiangxi{
    /* padding: 0 20px; */
    display: flex;
    justify-content: space-around;
    /* background-color: red; */
    /* font-size: 15px; */
}
.xiangxi:nth-child(1){
    /* background-color: yellow; */
    /* display: flex;
    flex-direction: column;
    justify-content: center; */

}
.xingming{
    /* background-color: violet; */
    text-align: left;
}
.yonghuleixing{
    text-align: center;
    /* background-color: tomato; */
}
.xiangxi_right{
    /* background-color: tomato; */
    text-align: right;
}

.el-main{
    /* line-height: 100px; */
}
/* 设置table header的背景颜色 */

.el-table__header th, .el-table__header tr {
background-color: #17B3A3;
line-height: 20px;

}

/* 设置表主体的高度 */

.el-table__body td,.el-table__body th{
padding:1px;

}

/* 设置表头的高度 */

.el-table__header td,.el-table__header th{
padding:6px 0px;

}

/* 设置分页器的高度 */

.site-wrapper .el-pagination {
margin-top: 5px;

text-align: right;

}

.el-pager li.active {
color: #080909;

cursor: default;

background-color: #17B3A3;

border-radius: 2px;

}
</style>