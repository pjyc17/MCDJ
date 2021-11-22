<template>
  <div class="container review-box">
    <input v-model="review.title" type="text" maxlength="100" placeholder="제목" class="title"><br>
    <hr>
    <textarea v-model="review.content" type="text" placeholder="내용" class="content" /><br>
    <button v-if="$route.params.reviewId !== 'create'" @click="createOrUpdate">수정</button>
    <button v-else @click="createOrUpdate">작성</button>
    <button @click="goToCommunity">취소</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Review',
  data: function() {
    return {
      review: {
        title: '',
        content: '',
      }
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    goToCommunity: function() {
      this.$router.push({name: 'Community'})
    },
    createOrUpdate: function() {
      const review = {title: this.review.title.trim(), content: this.review.content.trim()}
      if (this.$store.state.user.id === 0) {this.$router.push({name: 'Community'})}
      if (review.title && review.content) {
        if (this.$route.params.reviewId === 'create') {
          axios({
            headers: this.setToken(),
            method: 'post',
            url: `${this.$store.state.domain}/community/`,
            data: review,
          })
            .then(res => this.$router.push({name: 'ReviewDetail', params: {reviewId: res.data.id}}))
        } else {
          axios({
            headers: this.setToken(),
            method: 'put',
            url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`,
            data: review,
          })
            .then(res => this.$router.push({name: 'ReviewDetail', params: {reviewId: res.data.id}}))
            .catch(() => this.$router.push({name: 'NotFound'}))
        }
      } else {alert("빈칸이 있어요!")}
      this.review.title = ''
      this.review.content = ''
    }
  },
  created() {
    if (this.$store.state.user.id === 0) {
      this.$router.push({name: 'Community'})
    } else {
      if (this.$route.params.reviewId !== 'create') {
        axios({
          headers: this.setToken(),
          method: 'get',
          url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`
        })
          .then(res => {
            if (res.data.user.id !== this.$store.state.user.id) {
              this.$router.push({name: 'ReviewDetail', params: {reviewId: this.$route.params.reviewId}})
            } else {
              this.review.title = res.data.title
              this.review.content = res.data.content
            }
          })
          .catch(() => this.$router.push({name: 'NotFound'}))
      }
    }
  }
}
</script>

<style scoped>
.review-box {
  border-radius: 1rem;
  border-style: solid; 
  border-width: 2px; 
  padding: 12px; 
  word-break: break-all;
  border-color: LightGray; 
  background-color:#141414;
  opacity: 100%;
  color: white;
}
.title {
  width: 100%;
  height: 3rem;
  font-size: 2rem;
  background-color:#141414;
  opacity: 100%;
  color: white;
  border: 0;
}
.content {
  min-height: calc((100vh - 250px));
  /* overflow-y: hidden;
  resize: none; */
  width: 100%;
  background-color:#141414;
  opacity: 100%;
  color: white;
  border: 0;
}
</style>