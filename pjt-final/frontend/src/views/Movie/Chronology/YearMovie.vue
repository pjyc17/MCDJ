<template>
  <div @click="goToMovieDetail" class="movie-card">
    <div class="card h-100">
      <div class="card-img-box">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="movie.title">
      </div>
      <div class="card-body">
        <p class="card-title reduce-content">{{movie.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'YearMovie',
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
  font-size: 1.5em;
  color: #949597;
  -webkit-text-stroke: 0.5px #eddc5a;
  margin-bottom: 0;
}
.movie-card {
  cursor: pointer;
  width: 16rem;
  margin: 1rem 0.5rem;
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