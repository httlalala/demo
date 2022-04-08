<template>
    <div class="con" style="position:relative;">
       <div class="con1" style="margin-left:140px;position:relative;background-color:white;width:60%">
           <div style="width:50px"></div>
           <div>手动上传:</div>
           <div style=" margin-left: 30px;z-index:3;">
               <el-upload
                class="upload-demo"
                ref="upload"
                action="doUpload"
                :limit="1"
                :file-list="fileList"
                :http-request="uptimetable"
                :before-upload="beforeUpload">
                <el-button slot="trigger" size="medium" type="primary" style="height:50px;width:90px;">选取文件</el-button>
                <el-button type="primary" @click="submitUpload()" style="height:50px;width:90px;">开始上传</el-button>
                <!-- <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button> -->
                <div slot="tip" class="el-upload-list__item-name">{{fileName}}</div>
                </el-upload> 
           </div>
           <div slot="tip" class="el-upload__tip" style="postion:absolute;margin-top:80px;margin-left:-190px;">只能上传excel文件，且不超过500KB</div>
           <!-- <div style="postion:absolute;margin-top:80px;margin-left:-210px;">仅支持xsxl格式，文件大小不超过500kb</div> -->
           <div style=" margin-left: 30px;display:flex;align-items: center;">
               <div style="display:inline-block;height:20px;line-height:20px;"><svg t="1646820587902" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2691" width="25" height="25"><path d="M260.924 861.293a30.275 30.275 0 0 1-17.814-5.782c-54.847-39.702-100.368-92.343-131.641-152.231-32.329-61.907-49.417-131.781-49.417-202.066 0-116.756 45.468-226.523 128.026-309.082C272.637 109.573 382.404 64.106 499.16 64.106c116.755 0 226.522 45.467 309.082 128.026 82.558 82.559 128.026 192.326 128.026 309.082 0 130.068-57.349 252.485-157.344 335.862-12.903 10.761-32.089 9.023-42.849-3.883-10.761-12.905-9.023-32.09 3.882-42.85 86.089-71.783 135.464-177.166 135.464-289.129 0-207.47-168.79-376.26-376.26-376.26-207.471 0-376.26 168.79-376.26 376.26 0 120.327 58.276 234.349 155.89 305.009 13.61 9.852 16.657 28.873 6.804 42.484-5.951 8.219-15.245 12.586-24.671 12.586z" fill="#E75934" p-id="2692"></path><path d="M498.5 759.124c-16.803 0-30.5-13.621-30.5-30.424V371.223c0-16.803 13.697-30.424 30.5-30.424S529 354.42 529 371.223V728.7c0 16.803-13.697 30.424-30.5 30.424z" fill="#E75934" p-id="2693"></path><path d="M499.159 888.542m-68.695 0a68.695 68.695 0 1 0 137.39 0 68.695 68.695 0 1 0-137.39 0Z" fill="#E75934" p-id="2694"></path></svg></div>
               <span style="margin-top:5px;">请确保上传课表与模板格式相同</span>
           </div>
       </div>
        <div class="con2" style="margin-left:140px;background-color:white;margin-top:10px;width:60%">
             <div style="width:50px"></div>
             <div>上传状态:</div>
             <el-progress style="width:300px;margin-left:20px" :text-inside="true" :stroke-width="24" :percentage="progressPercent" status="success"></el-progress>
        </div>
       <div class="con3" style="margin-left:140px;background-color:white;margin-top:10px;width:60%">
           <div style="width:20px;"></div>课表实施周次：
           <div>
               <input id="week" type="text" v-model="week_Val" @blur="get_week" list="uplist" placeholder="请选择周次" style="width:200px; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;" >
                <datalist id="uplist">
　　                 <option  v-for="index of zhoushu" :key="index">{{index}}</option>
                </datalist>
           </div>
       </div>
       <div class="con4" style="margin-left:140px;background-color:white;width:60%">
            <div style="width:10px;"></div>课表实施时间：
            <input id="week_data" v-model="weekdata" type="text" placeholder="实施时间" style="width:200px; height:35px;border-radius:3px;border:1px solid rgb(196,200,207);padding-left:10px;">
       </div>
       <div class="con5" style="margin-left:140px;background-color:white;width:60%">
           <div style="width:50px;"></div>课表模板：
           <a href="http://47.97.193.46:8001/files/download/template/" download="课表模板">
               <div><svg t="1648613114091" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4271" width="16" height="16"><path d="M938.855808 638.776382l0 270.299169c0 27.41028-22.210861 49.634444-49.621141 49.634444l-754.442728 0c-27.41028 0-49.647747-22.224164-49.647747-49.634444L85.144192 638.776382c0-27.41028 22.224164-49.634444 49.634444-49.634444s49.634444 22.224164 49.634444 49.634444l0 220.664725 655.17384 0L839.58692 638.776382c0-27.41028 22.224164-49.634444 49.634444-49.634444S938.855808 611.366102 938.855808 638.776382zM476.55165 701.027168c9.335622 9.534144 22.116717 14.905478 35.46063 14.905478 13.344936 0 26.121937-5.371334 35.461653-14.905478l198.014866-202.167442c19.179828-19.583011 18.85544-51.006697-0.732687-70.190619-19.587104-19.175735-51.016931-18.85544-70.196759 0.731664l-112.924909 115.285676L561.634444 114.924449c0-27.41028-22.224164-49.634444-49.634444-49.634444-27.41028 0-49.634444 22.224164-49.634444 49.634444l0 429.754834L349.473393 429.40077c-19.179828-19.583011-50.590212-19.902282-70.186526-0.731664-19.583011 19.179828-19.910469 50.603515-0.730641 70.190619L476.55165 701.027168z" p-id="4272" fill="#859F3E"></path></svg>
            <span style="color:#859F3E">课表模板.docx</span></div>
           </a>
       </div>
       <div style="display:flex;flex-direction:column;position:absolute;top:120px;right:100px;">
           <img @mouseenter="onMouseoverEnvDelBtn($event)"
                @mouseleave="onMouseleaveEnvDelBtn($event)"
            src="../assets/xcx1.jpg" alt="" style="width:70px;height:80px;margin-right:80px;">
           <img  class="xcx" src="../assets/xcx2.jpg" alt="" style="width:150px;height:150px;margin-top:20px;display:none;">
       </div>
       <div><el-button type="success" @click.native="uptimetable()" style="width: 100px;height: 50px;background-color: rgb(133,159,62);">确认</el-button></div>
       <el-dialog
  title="提示"
  :visible.sync="kbdialogVisible"
  width="30%"
  :before-close="handleClose">
  <span>课表上传成功</span>
  <span slot="footer" class="dialog-footer">
    <el-button @click="kbdialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="kbdialogVisible = false">确 定</el-button>
  </span>
</el-dialog>
    </div>
</template>

<script>
    export default {
        name:'Kbgx',
        data(){
            return{
                a:1,
                upfilename:'',
                week_Val:'',
                weekdata:'',
                zhoushu:'',
                kbdialogVisible:false,
                progressPercent:0,
                progress:'progress',
                
            }
        },
        methods:{
            handleClose(done) {
                this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
            },
            onMouseoverEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:block"
            },
            onMouseleaveEnvDelBtn(event) {
            event.target.parentElement.querySelector(".xcx").style.cssText += "display:none"
            },
            //上传周次
            get_week(){
                const weeknum=document.getElementById("week").value
                // this.$data.weekdata=Number(weeknum) 
                const token=window.sessionStorage.getItem("token")
                console.log(token)
                const weektodata=document.getElementById("week_data").value
                this.$http.post('http://47.97.193.46:8001/week2date/',
                {
                    week: Number(weeknum),
                },
                {
                    headers:{
                        'Authorization':'JWT '+ token
                    },
                }
                ).then(res=> {
                    this.$data.weekdata=res.data
                    console.log(res)
                })
            },
            //更新课表
            uptimetable(){
                var startDate = new Date()
                console.log(startDate.getTime())
                const token=window.sessionStorage.getItem("token")
                console.log(token)
                //文件
                console.log(this.$data.upfilename=this.files.name)
                console.log('上传'+this.files.name)
                if(this.fileName == ""){
                    this.$message.warning('请选择要上传的文件！')
                    return false
                }
                let fileFormData = new FormData();
                console.log(typeof(parseInt(this.$data.week_Val)))
                fileFormData.append('file', this.files, this.fileName);
                fileFormData.append('week_start',parseInt(this.$data.week_Val));//filename是键，file是值，就是要传的文件，test.zip是要传的文件名
                let requestConfig = {
                    
                    headers: {
                    'Authorization':'JWT '+ token,
                    // 'Content-Type': 'multipart/form-data'
                    },
                    onUploadProgress: progressEvent => {
                    // progressEvent.loaded:已上传文件大小
                    // progressEvent.total:被上传文件的总大小
                    console.log(1111)
                    var that=this
                     var cnt=0
                    var time=1
                    this.progressPercent = Number((progressEvent.loaded / progressEvent.total * 100).toFixed(2)-70)
                    if(this.progressPercent !=100){
                       var progress=setInterval(function(){
                           cnt=cnt+time
                           time=time+1
                           if(that.progressPercent+cnt<100){
                               that.progressPercent=that.progressPercent+cnt
                           }
                        },4000);
                    }
                    }
                }

                this.$http.post('http://47.97.193.46:8001/files/upload/courses/',fileFormData,requestConfig).then(res=> {
                    window.clearInterval(this.$data.progress);
                    console.log(res)
                    this.$data.kbdialogVisible=true
                    this.$data.progressPercent=100
                })
            },
            beforeUpload(file){
                console.log(file,'文件');
                this.files = file;
                const extension = file.name.split('.')[1] === 'xls'
                const extension2 = file.name.split('.')[1] === 'xlsx'
                // const isLt2M = file.size / 1024 / 1024 < 5 //<5mb
                const isLt2M = file.size / 1024  < 500 //500kb
                if (!extension && !extension2) {
                        this.$message.warning('上传模板只能是 xls、xlsx格式!')
                    return
                }
                if (!isLt2M) {
                    this.$message.warning('上传模板大小不能超过 500kB!')
                    return
                }
                this.fileName = file.name;
                return false // 返回false不会自动上传
            },
            submitUpload() {
                const token=window.sessionStorage.getItem("token")
                console.log(this.$data.upfilename=this.files.name)
                console.log('上传'+this.files.name)
                if(this.fileName == ""){
                    this.$message.warning('请选择要上传的文件！')
                    return false
                }
                let fileFormData = new FormData();
                fileFormData.append('file', this.files, this.fileName);//filename是键，file是值，就是要传的文件，test.zip是要传的文件名
                let requestConfig = {
                    week_start: this.$data.week_Val,
                    headers: {
                    'Authorization':'JWT '+ token,
                    'Content-Type': 'multipart/form-data'
                    },
                }
                this.$http.post('http://47.97.193.46:8001/files/upload/courses/', fileFormData, requestConfig).then((res) => {
                if (data && data.code === 0) {
                    this.$message({
                        message: '操作成功',
                        type: 'success',
                        duration: 1500,
                        onClose: () => {
                        this.visible = false
                        this.$emit('refreshDataList')
                        }
                    })
                } else {
                    this.$message.error(data.msg)
                }
                }) 
                },
        },
        created(){
            const token=window.sessionStorage.getItem("token")
        },
        mounted(){
            const token=window.sessionStorage.getItem("token")
            console.log(111111)
            this.$http.get('http://47.97.193.46:8001/schools/weeknum/',{
            headers:{
            'Authorization':'JWT '+ token
            },
            }).then(res=>{
            console.log(res.data)
            this.$data.zhoushu=res.data
           })
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
    flex-direction: row;
    justify-content: flex-start;
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
.con5{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
</style>