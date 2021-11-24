import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Movies from '@/views/Movie/Movies.vue'
import MovieDetail from '@/views/Movie/MovieDetail.vue'
import GenreMovies from '@/views/Movie/GenreMovies.vue'
import Chronology from '@/views/Movie/Chronology/Chronology.vue'
import ChronologyYear from '@/views/Movie/Chronology/ChronologyYear.vue'
import Year from '@/views/Movie/Chronology/Year.vue'
import Community from '@/views/Community/Community.vue'
import ReviewDetail from '@/views/Community/ReviewDetail.vue'
import Review from '@/views/Community/Review.vue'
import Profile from '@/views/accounts/Profile.vue'
import Profile2 from '@/views/accounts/Profile2.vue'
import ProfileEdit from '@/views/accounts/ProfileEdit.vue'
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
