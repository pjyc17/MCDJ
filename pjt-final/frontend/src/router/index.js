import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Chronology from '@/views/Movie/Chronology/Chronology.vue'
import YearMovies from '@/views/Movie/Chronology/YearMovies.vue'
import MovieDetail from '@/views/Movie/MovieDetail.vue'
import Signup from '@/views/accounts/signup.vue'
import NotFound from '@/views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/chronology',
    name: 'Chronology',
    component: Chronology
  },
  {
    path: '/chronology/:year',
    name: 'YearMovies',
    component: YearMovies
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/404',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
