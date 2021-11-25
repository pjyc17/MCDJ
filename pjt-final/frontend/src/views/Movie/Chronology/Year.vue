<template>
  <div class="container">
    <h1>{{$route.params.year}} 년도</h1>
    <div class="flex-center-wrap">
      <movie
        v-for="(movie, idx) in shownMovies" :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Movie from '@/views/Movie/Movie.vue'

export default {
  name: 'Year',
  components: {
    Movie,
  },
  data: function() {
    return {
      shownMovies: [],
      movies: [],
      cnt: 20,
    }
  },
  methods: {
    listenScroll: function() {
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) <= 2 * clientHeight) {
        this.shownMovies.push(...this.movies.splice(0, this.cnt))
      }
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/recommend/${this.$route.params.year}/`,
    })
      .then(res => {
        this.movies = res.data
        this.shownMovies.push(...this.movies.splice(0, this.cnt))
      })
    window.addEventListener('scroll', this.listenScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.listenScroll);
  },
  updated() {
  }
}
</script>

<style>
</style>