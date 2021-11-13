<template>

<div class="col-12 col-md-6 col-xl-4 col-xxl-3 movie-card">
  <div class="card h-100">
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img-top" :alt="movie.title">
    <div class="card-body">
      <h5 class="card-title"><strong>{{movie.title}}</strong></h5>
      <p v-if="movie.overview" class="card-text reduce-content">{{movie.overview}}</p>
      <p v-else class="card-text reduce-content">내용 없음</p>
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

</style>