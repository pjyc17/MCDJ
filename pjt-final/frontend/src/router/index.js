import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Home2 from '@/views/Home2.vue'
import Movies from '@/views/Movie/Movies.vue'
import MovieDetail from '@/views/Movie/MovieDetail.vue'
import MovieDetail2 from '@/views/Movie/MovieDetail2.vue'
import GenreMovies from '@/views/Movie/GenreMovies.vue'
import Chronology from '@/views/Movie/Chronology/Chronology.vue'
import Chronology2 from '@/views/Movie/Chronology/Chronology2.vue'
import ChronologyYear from '@/views/Movie/Chronology/ChronologyYear.vue'
import Year from '@/views/Movie/Chronology/Year.vue'
import Recommend from '@/views/Movie/Recommend/Recommend.vue'
import Recommend2 from '@/views/Movie/Recommend/Recommend2.vue'
import Community from '@/views/Community/Community.vue'
import Community2 from '@/views/Community/Community2.vue'
import ReviewDetail from '@/views/Community/ReviewDetail.vue'
import Review from '@/views/Community/Review.vue'
import Profile from '@/views/accounts/Profile.vue'
import Profile2 from '@/views/accounts/Profile2.vue'
import ProfileEdit from '@/views/accounts/ProfileEdit.vue'
import ProfileEdit2 from '@/views/accounts/ProfileEdit2.vue'
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
    path: '/',
    name: 'Home2',
    component: Home2
  },
  {
    path: '/movies/:genreId/:keyword',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail2',
    component: MovieDetail2
  },
  {
    path: '/genre/:genreId',
    name: 'GenreMovies',
    component: GenreMovies
  },
  {
    path: '/chronology',
    name: 'Chronology',
    component: Chronology
  },
  {
    path: '/chronology',
    name: 'Chronology2',
    component: Chronology2
  },
  {
    path: '/chronology/:year',
    name: 'ChronologyYear',
    component: ChronologyYear
  },
  {
    path: '/year/:year',
    name: 'Year',
    component: Year
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/recommend',
    name: 'Recommend2',
    component: Recommend2
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community',
    name: 'Community2',
    component: Community2
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
    path: '/profile/:userId',
    name: 'Profile',
    component:Profile
  },
  {
    path: '/profile/:userId',
    name: 'Profile2',
    component:Profile2
  },  
  {
    path: '/profile/edit/:userId',
    name: 'ProfileEdit',
    component:ProfileEdit
  },
  {
    path: '/profile/edit2/:userId',
    name: 'ProfileEdit2',
    component:ProfileEdit2
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
