<template>
  <div class="item">
    <p class="mb-0 reduce-content">{{myMovie.title}}</p>
    <div class="btn-box">
      <button>V</button>
      <button @click="confirm">X</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyListItem',
  props: {
    myMovie: {
      type: Object,
    }
  },
  methods: {
    confirm: function() {
      if (confirm(`선택하신 "${this.myMovie.title}"를\n정말 삭제하시겠습니까?`)) {
        this.$store.commit("REMOVE_MYMOVIE", this.myMovie)
      }
    },
  }
}
</script>

<style scoped>
.item {
  display: flex;
  justify-content: space-between;
  text-decoration: none;
}
.item-content {
  display: inline-block;
}
.btn-box {
  display: inline-block;
  width: 3.5rem;
}
.reduce-content {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  width: calc(100% - 3.5rem);
  /* display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient:vertical; */
}
</style>