<template>
  <div id="my-movie-list">
    <header>
      <h2>My Movie List</h2>
      <my-list-form/>
    </header>
    <section>
      <my-list/>
    </section>
  </div>
</template>

<script>
import MyList from '@/components/mylist/MyList.vue'
import MyListForm from '@/components/mylist/MyListForm.vue'

export default {
  name: 'MyMovieList',
  components: {
    MyList,
    MyListForm
  }
}
</script>

<style>
#my-movie-list header {
  display: inline-block;
  background-color:lightsteelblue;
  width: 90vw;
  border-top-left-radius: 1vw;
  border-top-right-radius: 1vw;
  padding: 1.5rem 0 1rem 0;
}
#my-movie-list section {
  display: inline-block;
  width: 90vw;
}
</style>