<template>
    <div class="con" style="position:relative;">
       <div class="con1" style="margin-left:140px;">
           <div>手动上传:</div>
           <div style=" margin-left: 30px;">
                <button style="background-color: rgb(1,126,82);width: 100px;height: 50px;">选择上传</button>
               <button style="background-color: rgb(1,126,82);width: 100px;height: 50px;">开始上传</button>
           </div>
           <div style=" margin-left: 30px;display:flex;align-items: center;">
               <div style="display:inline-block;height:20px;line-height:20px;"><svg t="1646820587902" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2691" width="25" height="25"><path d="M260.924 861.293a30.275 30.275 0 0 1-17.814-5.782c-54.847-39.702-100.368-92.343-131.641-152.231-32.329-61.907-49.417-131.781-49.417-202.066 0-116.756 45.468-226.523 128.026-309.082C272.637 109.573 382.404 64.106 499.16 64.106c116.755 0 226.522 45.467 309.082 128.026 82.558 82.559 128.026 192.326 128.026 309.082 0 130.068-57.349 252.485-157.344 335.862-12.903 10.761-32.089 9.023-42.849-3.883-10.761-12.905-9.023-32.09 3.882-42.85 86.089-71.783 135.464-177.166 135.464-289.129 0-207.47-168.79-376.26-376.26-376.26-207.471 0-376.26 168.79-376.26 376.26 0 120.327 58.276 234.349 155.89 305.009 13.61 9.852 16.657 28.873 6.804 42.484-5.951 8.219-15.245 12.586-24.671 12.586z" fill="#E75934" p-id="2692"></path><path d="M498.5 759.124c-16.803 0-30.5-13.621-30.5-30.424V371.223c0-16.803 13.697-30.424 30.5-30.424S529 354.42 529 371.223V728.7c0 16.803-13.697 30.424-30.5 30.424z" fill="#E75934" p-id="2693"></path><path d="M499.159 888.542m-68.695 0a68.695 68.695 0 1 0 137.39 0 68.695 68.695 0 1 0-137.39 0Z" fill="#E75934" p-id="2694"></path></svg></div>
               <span style="margin-top:5px;">请确保上传课表与模板格式相同</span>
           </div>
       </div>
       <div class="con2" style="margin-left:140px;">上传状态：</div>
       <div class="con3" style="margin-left:110px;">课表实施周次：</div>
       <div class="con4" style="margin-left:110px;">课表实施时间：</div>
       <div class="con5" style="margin-left:140px;">课表模板：</div>
       <div style="display:flex;flex-direction:column;position:absolute;top:120px;right:100px;">
           <img @mouseenter="onMouseoverEnvDelBtn($event)"
                @mouseleave="onMouseleaveEnvDelBtn($event)"
            src="../assets/xcx1.jpg" alt="" style="width:70px;height:80px;margin-right:80px;">
           <img  class="xcx" src="../assets/xcx2.jpg" alt="" style="width:150px;height:150px;margin-top:20px;display:none;">
       </div>
       <div><el-button type="success" style="width: 100px;height: 50px;background-color: rgb(133,159,62);">确认</el-button></div>
    </div>
</template>

<script>
    export default {
        name:'Kbgx',
        data(){
            return{
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
.con5{
    display: flex;
    align-items: center;
    margin-left: 10%;
}
</style>