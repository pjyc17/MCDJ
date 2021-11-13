<template>
  <div class="container">
    <div class="row movies-container">
      <searched-list-item
        v-for="searchedMovie in searchedMovies" :key="searchedMovie.id"
        :movie="searchedMovie"
      />
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import SearchedListItem from '@/components/mylist/SearchedListItem.vue'

export default {
  name: 'SearchedList',
  components: {
    SearchedListItem,
  },
  computed: {
    ...mapState(['searchedMovies',]),
  }
}
</script>

<style scoped>
.movies-container {
  display: flex;
  justify-content: center;
}
</style>