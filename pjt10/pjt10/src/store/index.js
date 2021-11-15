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
    myMovie: null,
    searchedMovies: [],
    myListFlag: true,
  },
  mutations: {
    LOAD_TOP_RATED_MOVIES: (state, movies) => state.topRatedMovies = movies,
    ADD_TO_MY_MOVIES: (state, movie) => {
      if (state.myMovies.every(myMovie => myMovie.title !== movie.title)) {
        const newmovie = {
          ...movie,
          isCompleted: false,
        }
        state.myMovies.push(newmovie)
      } else {
        alert("이미 추가한 영화입니다.")
      }
    },
    SEARCHED_MOVIES: (state, movies) => {
      state.searchedMovies = movies
      state.myListFlag = true
    },
    REMOVE_MYMOVIE: ({myMovies}, movie) => myMovies.splice(myMovies.indexOf(movie), 1),
    COMPLETE_MYMOVIE: ({myMovies}, movie) => myMovies.find(myMovie => myMovie.title === movie.title).isCompleted = !movie.isCompleted,
    SHOW_MYMOVIE: (state, movie) => {
      state.myMovie = movie
      state.myListFlag = false
    }
  },
  getters: {},
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
    },
    searchMovie: ({commit,}, keyword) => {
      axios({
        methods: 'get',
        url: `${TMDB_URL}/search/movie`,
        params: {
          api_key: TMDB_API,
          language: 'ko-kr',
          query: keyword,
        }
      })
        .then((res) => {
          if (res.data.results.length !== 0) {
            commit('SEARCHED_MOVIES', res.data.results)
          } else {
            alert('검색결과가 없습니다.')
            commit('SEARCHED_MOVIES', res.data.results)
          }
        })
        .catch(() => alert('뭘 입력하신거죠??'))
    },
  },
  modules: {
  }
})
