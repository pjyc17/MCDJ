<template>
<div>
  <div @click="goToYear">
    <div class="card h-100 movie-card">
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
      this.$router.push({name: 'Year', params: {year: this.eachYear.year}})
    }
  }
}
</script>

<style>
</style>