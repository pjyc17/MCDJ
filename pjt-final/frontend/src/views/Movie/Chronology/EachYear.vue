<template>
<div>
  <div @click="goToYear" class="movie-card">
    <div class="card h-100">
      <div class="card-img-box">
        <img :src="`https://image.tmdb.org/t/p/w500/${eachYear.poster_path}`" class="card-img" :alt="eachYear.year">
      </div>
      <div class="year-box">
        <p class="year"><strong>{{eachYear.year}}</strong></p>
      </div>
    </div>
  </div>
</div>
  
</template>

<script scoped>
export default {
  name: 'EachYear',
  props: {
    eachYear: {
      type: Object,
    }
  },
  methods: {
    goToYear: function() {
      this.$router.push({name: 'YearMovies', params: {year: this.eachYear.year}})
    }
  }
}
</script>

<style>
.movie-card {
  cursor: pointer;
  width: 10rem;
  margin: 1rem 0.5rem;
}
.year-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.year {
  font-size: 4em;
  -webkit-text-stroke: 1.5px black;
  margin-bottom: 0;
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