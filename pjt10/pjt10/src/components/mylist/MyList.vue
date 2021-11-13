<template>
  <div>
    <div class="title-box">
      <h4 class="py-2 mb-0 title-content">My List</h4>
      <select v-model="selected" class="select-box">
        <option value="all">전체</option>
        <option value="doing">진행중</option>
        <option value="done">완료</option>
      </select>
    </div>
    <my-list-item 
      v-for="(myMovie, idx) in selectedMovies" :key="idx"
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
  data: function() {
    return {
      selected: 'all',
    }
  },
  components: {
    MyListItem,
  },
  computed: {
    ...mapState(['myMovies']),
    selectedMovies: function() {
      return this.myMovies.filter(movie => {
        if (this.selected === 'doing') {
          return !movie.isCompleted
        }
        if (this.selected === 'done') {
          return movie.isCompleted
        }
        return true
      })
    }
  }
}
</script>

<style scoped>
.title-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color:blanchedalmond;
}
.title-content {
  display: inline-block;
  width: calc(100% - 71px);
}
.select-box {
  background-color: transparent;
  border: 0;
  width: 4.4rem;
  height: 1.2rem;
}
.item-padding {
  padding: 0.5rem 0;
}
.base-background {
  background-color: beige;
}
.toggle-background {
  background-color: cornsilk;
}
</style>