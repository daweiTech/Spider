import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history', //去掉链接的#号
  base: '/', //去掉链接的/杠
  // 路由的懒加载
  routes: [
    {// 重定向
      path: '/',
      redirect: '/login'
     },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/HelloWorld',
      name: 'hello',
      component: HelloWorld
    },
  ]
})

