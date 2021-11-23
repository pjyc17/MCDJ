import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from "vuex-persistedstate";


const domain = process.env.VUE_APP_BACKEND_DOMAIN
const today = new Date()
const todayYear = today.getFullYear()
const todayMonth = today.getMonth() + 1
const todayDate = today.getDate()
const todayYMD = {
  year: todayYear,
  month: todayMonth,
  date: todayDate,
}


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    domain: domain,
    TMDB_KEY: '843ed6063914aca6ab7f2fcf47870d67',
    TMDB_URL: 'https://api.themoviedb.org/3',
    anonymousUser: {
      id: 0,
      username: '',
      // birthday: {...todayYMD,},
    },
    today: {...todayYMD,},
    user: {
      id: 0,
      username: '',
      birthday: {...todayYMD,},
    },
    allMovies: [],
    allGenres: [],
    searchedMovies: [],
    shownMovies: [],
  },
  mutations: {
    GET_ALL_MOVIES: (state, movies) => state.allMovies = movies,
    GET_ALL_GENRES: (state, genres) => state.allGenres = genres,
    SEARCH_MOVIES: (state, movies) => state.searchedMovies = movies,
    SPLICE_SEARCH_MOVIES: (state) => state.shownMovies.push(...state.searchedMovies.splice(0, 20)),
    RESET_SHOWNMOVIES: (state) => state.shownMovies = [],
    GET_USER: (state, user) => state.user = {...state.user, ...user},
    GET_BIRTHDAY: (state, birthday) => state.user.birthday = {...birthday},
  },
  actions: {
  },
  modules: {
  },
})
