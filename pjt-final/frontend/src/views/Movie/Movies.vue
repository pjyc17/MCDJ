<template>
  <div class="container">
    <div class="flex">
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
  name: 'Movies',
  components: {
    Movie,
  },
  data: function() {
    return {
      movies: [],
      shownMovies: [],
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
    if (this.$route.params.genreId === '*') {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/search/${this.$route.params.keyword}/`,
      })
        .then(res => {
          this.movies = res.data
          this.shownMovies.push(...this.movies.splice(0, this.cnt))
        })
    } else {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/${this.$route.params.genreId}/search/${this.$route.params.keyword}/`,
      })
        .then(res => {
          this.movies = res.data
          this.shownMovies.push(...this.movies.splice(0, this.cnt))
        })
    }
    window.addEventListener('scroll', this.listenScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.listenScroll);
  },
}
</script>

<style>

</style>