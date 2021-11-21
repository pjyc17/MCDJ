import Vue from 'vue'
import Vuex from 'vuex'
// const domain = process.env.BACKEND_DOMAIN

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // domain: 'http://127.0.0.1:8000',
    domain: 'http://121.178.32.250:8000',
    TMDB_KEY: '843ed6063914aca6ab7f2fcf47870d67',
    TMDB_URL: 'https://api.themoviedb.org/3',
    allMovies: [],
    allReviews: [],
  },
  mutations: {
    GET_ALL_MOVIES: (state, movies) => state.allMovies = movies,
    GET_ALL_REVIEWS: (state, reviews) => state.allReviews = reviews,
  },
  actions: {
  },
  modules: {
  }
})
