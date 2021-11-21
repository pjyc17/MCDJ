<template>
  <div>
    게시글작성<br>
    <label for="title">제목</label>
    <input v-model="review.title" type="text" id="title"><br>
    <label for="content">내용</label>
    <input v-model="review.content" type="text" id="content"><br>
    <button @click="createReview">작성</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateView',
  data: function() {
    return {
      review: {
        title: null,
        content: null,
      }
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    createReview: function() {
      const review = this.review
      console.log(review)
      axios({
        headers: this.setToken(),
        method: 'post',
        url: `${this.$store.state.domain}/community/`,
        data: review
      })
        .then()
    }
  }
}
</script>

<style>

</style>