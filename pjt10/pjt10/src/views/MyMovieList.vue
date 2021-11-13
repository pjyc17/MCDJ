<template>
  <div id="my-movie-list">
    <header>
      <my-list-form/>
    </header>
    <section class="section-box">
      <div class="main-section">
        <searched-list
          v-if="myListFlag"
        />
        <my-movie-detail
          v-else
        />
      </div>
      <div class="udline"></div>
      <my-list class="side-bar"/>
    </section>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import MyListForm from '@/components/mylist/MyListForm.vue'
import SearchedList from '@/components/mylist/SearchedList.vue'
import MyList from '@/components/mylist/MyList.vue'
import myMovieDetail from '@/components/mylist/MyMovieDetail.vue'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    SearchedList,
    MyList,
    myMovieDetail,
  },
  computed: {
    ...mapState(['myListFlag',]),
  }
}
</script>

<style scoped>
#my-movie-list {
  display: inline-block;
  width: 90vw;
}
#my-movie-list header {
  background-color:lightsteelblue;
  border-top-left-radius: 1vw;
  border-top-right-radius: 1vw;
  padding: 1.5rem 0 1rem 0;
}

.section-box {
  display: flex;
  justify-content: space-between;
}
.main-section {
  width: 75%;
}
.side-bar {
  width: 25%
}
.udline {
  background: black;
  width: 1px;
}
</style>