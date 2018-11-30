import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/pages/home'
import profile from '@/components/pages/profile'
import sigmusWajima from '@/components/documents/sigmus/wajima'
import masterExperiment from '@/components/documents/master/experiment'

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
      path: '/profile',
      name: 'profile',
      component: profile
    },
    {
      path: '/documents/sigmus/2018/wajima',
      name: 'sigmusWajima',
      component: sigmusWajima
    },
    {
      path: '/documents/master/experiment',
      name: 'masterExperiment',
      component: masterExperiment
    }
  ]
})
