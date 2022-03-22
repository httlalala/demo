// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
/*引入element-ui*/
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
/*引入axios*/
import axios from 'axios'
//配置请求的根路径
axios.defaults.baseURL='https://luoxilimit/exchangecourse'
Vue.prototype.$axios = axios;      //把axios挂载到vue上
Vue.use(ElementUI)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
