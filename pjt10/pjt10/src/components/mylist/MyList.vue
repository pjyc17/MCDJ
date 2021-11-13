<template>
  <div>
    <h3 class="mt-2 mb-0">My Movie List</h3>
    <my-list-item 
      v-for="(myMovie, idx) in myMovies" :key="idx"
      :myMovie="myMovie"
      class="base-background"
      :class="{'item-padding': true,'toggle-background': idx % 2}"
    />
  </div>
</template>

<script>
import {mapState} from 'vuex'
import MyListItem from '@/components/mylist/MyListItem.vue'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
  computed: {
    ...mapState(['myMovies']),
  }
}
</script>

<style scoped>
.item-padding {
  padding: 0.5rem 0;
}
.base-background {
  background-color: whitesmoke;
}
.toggle-background {
  background-color: lightgray;
}
</style>