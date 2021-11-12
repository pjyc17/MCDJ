import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate";

const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
const TMDB_URL = 'https://api.themoviedb.org/3'
''
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
    paths: ['myMovies',]
  })],
  state: {
    topRatedMovies: [],
    myMovies: [],
  },
  mutations: {
    LOAD_TOP_RATED_MOVIES: (state, movies) => {
      state.topRatedMovies = movies
    },
    ADD_TO_MY_MOVIES: ({topRatedMovies, myMovies}, movieTitle) => {
      if (myMovies.every(myMovie => myMovie.title !== movieTitle)) {
        const myMovie = topRatedMovies.find(topRatedMovie => topRatedMovie.title === movieTitle)
        if (myMovie) {
          myMovies.push(myMovie)
        }
      }
    },
  },
  getters: {
  },
  actions: {
    loadTopRatedMovies: ({commit}) => {
      axios({
        methods: 'get',
        url: `${TMDB_URL}/movie/top_rated`,
        params: {
          api_key: TMDB_API,
          language: 'ko-kr'
        }
      })
        .then((res) => commit('LOAD_TOP_RATED_MOVIES', res.data.results))
    }
  },
  modules: {
  }
})
