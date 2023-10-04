import Vue from 'vue'
import App from './App.vue'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(Element)

// 安装路由
import router from './router'
import VueRouter from 'vue-router'
Vue.use(VueRouter);


Vue.config.productionTip = false

new Vue({
  router, 
  render: h => h(App),
}).$mount('#app')

