<template>
  <div v-if="review">
    <h2>제목: {{review.title}}</h2>
    <p>작성: {{review.created}} / 수정: {{review.updated}}</p>
    <p>작성자: {{review.user.username}}</p>
    <p>내용: {{review.content}}</p>
    <div><i class="fas fa-thumbs-up cursor"></i> {{review.likes_cnt}}</div>
    <hr>
    <review-comment/>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewComment from '@/views/Community/ReviewComment.vue'

export default {
  name: 'ReviewDetail',
  components: {
    ReviewComment,
  },
  data: function() {
    return {
      review: null,
    }
  },
  methods: {

  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`
    })
      .then(res => this.review = res.data)
  }
}
</script>

<style>

</style>