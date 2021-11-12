<template>
  <div>
    <input v-model="wantedMovieTitle" @keyup.enter="onWantedMovie" type="text">
    <button @click="onWantedMovie" class="btn btn-sm btn-secondary">Add</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function() {
    return {
      wantedMovieTitle: null,
    }
  },
  methods: {
    onWantedMovie: function() {
      this.wantedMovieTitle = this.wantedMovieTitle.trim()
      this.$store.commit('ADD_TO_MY_MOVIES', this.wantedMovieTitle)
      this.wantedMovieTitle = null
    },
  }
}
</script>

<style>

</style>