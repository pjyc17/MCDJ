<template>
  <div>
    <h1>{{$route.params.year}}</h1>
    <div class="flex">
      <year-movie
        v-for="(movie, idx) in shownMovies" :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import YearMovie from '@/views/Movie/Chronology/YearMovie.vue'

export default {
  name: 'YearMovies',
  components: {
    YearMovie,
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
      url: `${this.$store.state.domain}/movies/annual_movies/${this.$route.params.year}/`,
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
}
</script>

<style>

</style>