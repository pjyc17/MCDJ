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
        title: "",
        content: "",
      }
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    createReview: function() {
      const review = {title: this.review.title.trim(), content: this.review.content.trim()}
      if (review.title && review.content) {
        axios({
          headers: this.setToken(),
          method: 'post',
          url: `${this.$store.state.domain}/community/`,
          data: review
        })
          .then()
      } else {alert("제대로 입력하세요!")}
      this.review.title = ""
      this.review.content = ""
    }
  }
}
</script>

<style>

</style>