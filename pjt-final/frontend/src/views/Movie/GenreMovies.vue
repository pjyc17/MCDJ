<template>
  <div class="container">
    <h1>추천하는 {{genreTitle}} 장르의 영화들입니다.</h1>
    <div class="flex">
      <movie
        v-for="movie in shownMovies" :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import Movie from '@/views/Movie/Movie.vue'

export default {
  name: 'GenreMovies',
  components: {
    Movie,
  },
  data: function() {
    return {
      genreTitle: null,
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
    this.movies = this.$store.state.userMoviesByGenres.find(genre => genre.id === this.$route.params.genreId).movies
    this.shownMovies.push(...this.movies.splice(0, this.cnt))
    this.genreTitle = this.$store.state.allGenres.find(genre => genre.id === this.$route.params.genreId).name
    window.addEventListener('scroll', this.listenScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.listenScroll);
  },
}
</script>

<style>

</style>