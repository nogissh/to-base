import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import sigmusWajima from '@/components/documents/sigmus/wajima'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/documents/sigmus/2018/wajima',
      name: 'sigmusWajima',
      component: sigmusWajima
    }
  ]
})
