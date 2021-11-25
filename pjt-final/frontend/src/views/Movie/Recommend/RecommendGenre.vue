<template>
  <div class="my-container">
    <hr>
    <div class="text-left my-font">{{genre.name}}</div>
    <div class="flex-nowrap">
      <movie 
        v-for="movie in genre.movies.slice(0, cnt)" :key="movie.id" 
        :movie="movie"
      />
    </div>
    <!-- {{genre}} -->
  </div>
</template>

<script>
import Movie from '@/views/Movie/Movie.vue'

export default {
  name: 'RecommendGenre',
  components: {
    Movie
  },
  props: {
    genre: {
      type: Object,
    }
  },
  data: function() {
    return {
      movies: [],
      cnt: parseInt((window.innerWidth - 160) / 192) + 1,
    }
  },
  created() {
    window.addEventListener('resize', () => {
      this.cnt = parseInt((window.innerWidth - 160) / 192) + 1
    }, true)
    window.addEventListener('scroll', () => {
      this.cnt = parseInt((window.innerWidth - 160) / 192) + 1
    })
  },
}
</script>

<style>

</style>