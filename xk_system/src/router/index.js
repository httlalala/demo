import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Main from '../views/Main'
import Kbgx from '../views/Kbgx'
import Kbdc from '../views/Kbdc'
import Xqrqsd from '../views/Xqrqsd'
import Njglysd from '../views/Njglysd'
import Dpgl from '../views/Dpgl'
import Login from '../views/Login'

Vue.use(Router)

const router= new Router({
  routes: [
    {
      path: '/',
      // name: 'HelloWorld',
      // component: HelloWorld
      redirect:'/Login'
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main,
      children:[
        {
          path: 'Kbgx',
          name: 'Kbgx',
          component: Kbgx
        },
        {
          path: 'Kbdc',
          name: 'Kbdc',
          component: Kbdc
        },
        {
          path: 'Xqrqsd',
          name: 'Xqrqsd',
          component: Xqrqsd 
        },
        {
          path: 'Njglysd',
          name: 'Njglysd',
          component: Njglysd
        },
        {
          path: 'Dpgl',
          name: 'Dpgl',
          // component: Dpgl 
          component: ()=>
          import ("../views/Dpgl"), 
        },

      ]
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },


  ]
})
//挂载路由导航守卫
router.beforeEach((to,from,next)=>{
  //to将要访问的路径
  //from代表从哪个路径跳转而来
  //next是一个函数，表示放行
  if (to.path=='/login') return next();
  //获取token
  const tokenStr=window.sessionStorage.getItem('token')
  if(!tokenStr) return next('/login')
  next()
})
export default router