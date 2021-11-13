<template>
<div class="col-6 col-md-4 col-xl-3 col-xxl-2 movie-card">
  <div class="card h-100">
    <div class="card-img-box">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="movie.title">
    </div>
    <div class="card-body">
      <h5 class="card-title mb-0"><strong>{{movie.title}}</strong></h5>
    </div>
    <div @click="addMyMovieList(movie)" class="btn btn-success btn-sm">Add My Movie List</div>
  </div>
</div>
</template>

<script>
import {mapMutations} from 'vuex'
export default {
  name: 'SearchedListItem',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    ...mapMutations({
      addMyMovieList: 'ADD_TO_MY_MOVIES',
    }),
  }
}
</script>

<style scoped>
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