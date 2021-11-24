<template>
  <div @click="goToMovieDetail" class="movie-card">
    <div class="card h-100">
      <div class="card-img-box">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="movie.title">
      </div>
      <div class="card-body b">
        <p class="card-title reduce-content">{{movie.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Movie',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    goToMovieDetail: function() {
      this.$router.push({name: 'MovieDetail', params: {movieId: this.movie.id}})
    }
  }
}
</script>

<style scoped>
.reduce-content {
  overflow: hidden;
  /* text-overflow:ellipsis; */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: 1.2em;
  font-weight: bold;
  color: black;
  -webkit-text-stroke: 0.1px #949597;
  margin-bottom: 0;
}
.movie-card {
  cursor: pointer;
  width: 12rem;
  margin: 1rem 0.5rem;
}
</style>