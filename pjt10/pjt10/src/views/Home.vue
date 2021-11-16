<template>
  <div class="container">
    <div class="row movies-container">
      <movie-card
        v-for="movie in topRatedMovies" :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
  // @ is an alias to /src
import {mapState} from 'vuex'
import MovieCard from '@/components/movie/MovieCard.vue'


export default {
  name: 'Home',
  data: function() {
    return {
      flag: true,
      page: 1,
    }
  },
  components: {
    MovieCard
  },
  computed: {
    ...mapState(['topRatedMovies',])
  },
  methods: {
    listenScroll: function() {
      if (this.flag) {
        const {scrollHeight, scrollTop, clientHeight} = document.documentElement
        if (scrollHeight - Math.round(scrollTop) <= 2 * clientHeight) {
          this.flag = false
          this.page += 1
          this.$store.dispatch('loadTopRatedMovies', this.page)
        }
      }
    }
  },
  updated() {
    this.flag = this.$store.state.flag
  },
  created() {
    window.addEventListener('scroll', this.listenScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.listenScroll);
  },
}
</script>

<style scoped>
.movies-container {
  display: flex;
  justify-content: center;
}
</style>