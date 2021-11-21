import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Movies from '@/views/Movie/Movies.vue'
import MovieDetail from '@/views/Movie/MovieDetail.vue'
import Chronology from '@/views/Movie/Chronology/Chronology.vue'
import YearMovies from '@/views/Movie/Chronology/YearMovies.vue'
import Community from '@/views/Community/Community.vue'
import ReviewDetail from '@/views/Community/ReviewDetail.vue'
import Review from '@/views/Community/Review.vue'
import Signup from '@/views/accounts/Signup.vue'
import NotFound from '@/views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movies/:keyword',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
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
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
  path: '/community/:reviewId',
  name: 'ReviewDetail',
  component: ReviewDetail
  },
  {
    path: '/community/review/:reviewId',
    name: 'Review',
    component: Review
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
