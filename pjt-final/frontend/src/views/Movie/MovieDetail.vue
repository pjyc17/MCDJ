<template>
  <div>
    {{movie}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieDetail',
  data: function() {
    return {
      movie: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/${this.$route.params.movieId}/`,
    })
      .then(res => this.movie = res.data)
  }
}
</script>

<style>

</style>