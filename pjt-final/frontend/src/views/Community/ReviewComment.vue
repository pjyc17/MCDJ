<template>
  <div>
    <div v-if="$store.state.user.id !== 0">
      <!-- <label for="comment">댓글</label> -->
      <input type="text"><button>입력</button>
    </div>
    <div v-for="comment in comments" :key="comment.id">
      {{comment.content}}
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'ReviewComment',
  data: function() {
    return {
      comments: [],
    }
  },
  methods: {
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
  },
}
</script>

<style>

</style>