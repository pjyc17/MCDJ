<template>
  <div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail2",
  created() {
    this.$router.push({name: 'MovieDetail', params: {movieId: this.$route.params.movieId}})
  }
}
</script>

<style>

</style>