<template>

<div class="col-12 col-md-6 col-xl-4 col-xxl-3 movie-card">
  <div class="card h-100">
    <div class="card-img-box">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="movie.title">
    </div>
    <div class="card-body">
      <h5 class="card-title"><strong>{{movie.title}}</strong></h5>
      <p v-if="movie.overview" class="card-text reduce-content">{{movie.overview}}</p>
      <p v-else class="card-text reduce-content"><br><br><br></p>
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
  /* text-overflow:ellipsis; */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
.movie-card {
  margin: 1rem 0;
}
.card-img-box {
  position: relative;
  height: 0;
  padding-top: 150%;
}
.card-img {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 100%;
}

</style>