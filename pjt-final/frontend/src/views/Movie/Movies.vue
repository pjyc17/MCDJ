<template>
  <div class="container">
    <div class="flex-center-wrap">
      <movie
        v-for="(movie, idx) in $store.state.shownMovies" :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import Movie from '@/views/Movie/Movie.vue'

export default {
  name: 'Movies',
  components: {
    Movie,
  },
  data: function() {
    return {
      // movies: [],
      // shownMovies: [],
      // cnt: 20,
    }
  },
  methods: {
    listenScroll: function() {
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) <= 2 * clientHeight) {
        // this.shownMovies.push(...this.$store.commit('SPLICE_SEARCH_MOVIES', this.cnt))
        this.$store.commit('SPLICE_SEARCH_MOVIES')
      }
    }
  },
  created() {
    window.addEventListener('scroll', this.listenScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.listenScroll);
  },
}
</script>

<style>

</style>