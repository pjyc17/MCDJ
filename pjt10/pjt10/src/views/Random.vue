<template>
  <div class="random-card">
    <div @click="pickMovie" class="btn btn-success w-100">PICK</div>
    <div v-if="selectedMovie" class="card w-100">
      <img :src="`https://image.tmdb.org/t/p/w500/${selectedMovie.poster_path}`" class="card-img-top" :alt="selectedMovie.title">
      <div class="card-body">
        <h5 class="card-title title-box"><strong>{{selectedMovie.title}}</strong></h5>
      </div>
    </div>
    <div v-else class="card w-100">
      <img src="@/assets/pickamovie.jpg" class="card-img-top" alt="...">
      <div class="card-body">
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Random',
  data: function() {
    return {
      selectedMovie: null,
    }
  },
  methods: {
    pickMovie: function() {
      this.selectedMovie = _.sample(this.$store.state.topRatedMovies)
    }
  }
}
</script>

<style scoped>
.random-card {
  display: inline-block;
  width: 20rem;
}
</style>