<template>
  <div class="container">
    <div class="row movies-container">
      {{cnt}}
      <!-- <movie-card/> -->
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
  components: {
    MovieCard
  },
  computed: {
    ...mapState(['topRatedMovies', 'cnt'])
  },
}
</script>

<style scoped>
.movies-container {
  display: flex;
  justify-content: center;
}
</style>