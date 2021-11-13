<template>
  <div>
    <div class="float-start w-50">
      <img :src="`https://image.tmdb.org/t/p/w500/${myMovie.poster_path}`" class="w-100" :alt="myMovie.title">
    </div>
    <h5 class="py-3"><strong>{{myMovie.title}}</strong></h5>
    <p v-if="myMovie.overview" class="overview">{{myMovie.overview}}</p>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'MyMovieDetail',
  computed: {
    ...mapState(['myMovie',]),
  }
}
</script>

<style scoped>
.box {
  display: inline-block;
}
</style>