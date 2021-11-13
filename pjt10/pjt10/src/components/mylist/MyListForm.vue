<template>
  <div>
    <h2>Search Movies</h2>
    <input v-model="keyword" @keyup.enter="searchMovie(keyword)" type="text">
    <button @click="searchMovie(keyword)" class="btn btn-sm btn-secondary">Search</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MyListForm',
  data: function() {
    return {
      keyword: null,
    }
  },
  methods: {
    // onWantedMovie: function() {
    //   this.wantedMovieTitle = this.wantedMovieTitle.trim()
    //   this.$store.commit('ADD_TO_MY_MOVIES', this.wantedMovieTitle)
    //   this.wantedMovieTitle = null
    // },
    ...mapActions(['searchMovie',]),
  }
}
</script>

<style>

</style>