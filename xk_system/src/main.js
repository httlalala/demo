// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
/*引入element-ui*/
import ElementUI from 'element-ui';
import { Message } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
/*引入axios*/
import axios from 'axios'
//引入vant
// import Vant from 'vant';
// import 'vant/lib/index.css';
//引入vuex
// import storeConfig from './vuex/store'
//配置请求的根路径
// axios.defaults.baseURL='http://47.97.193.46:8001'
// Vue.prototype.$axios = axios;      //把axios挂载到vue上
Vue.prototype.$http=axios
//警告窗口
Vue.prototype.$message= Message
Vue.use(ElementUI)
// Vue.use(Vant);

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // store,//使用store
  components: { App },
  template: '<App/>'
})
