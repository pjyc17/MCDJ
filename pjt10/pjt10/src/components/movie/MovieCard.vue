<template>

<div class="col-12 col-md-6 col-xl-4 col-xxl-3 movie-card">
  <div class="card h-100">
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img-top" :alt="movie.title">
    <div class="card-body reduce-content">
      <h5 class="card-title">{{movie.title}}</h5>
      <p class="card-text">{{movie.overview}}</p>
    </div>
  </div>
</div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: {
      type:Object,
    }
  }
}
</script>

<style scoped>
.reduce-content {
  overflow: hidden;
  white-space: wrap;
  text-overflow: ellipsis;
  height: 190px;
}
.movie-card {
  margin: 1rem 0;
}

</style>