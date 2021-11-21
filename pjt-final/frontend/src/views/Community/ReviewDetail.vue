<template>
  <div v-if="review">
    <h2>제목: {{review.title}}</h2>
    <div v-if="review.user.id === $store.state.user.id">
      <button @click="goToUpdate">수정</button>
      <button @click="deleteReview">삭제</button>
    </div>
    <p>작성: {{convertDate(review.created)}} / 수정: {{convertDate(review.updated)}}</p>
    <p>작성자: {{review.user.username}}</p>
    <p>내용: {{review.content}}</p>
    <div><i class="fas fa-thumbs-up cursor" @click="likeReview"></i> {{review.likes_cnt}}</div>
    <button @click="goToCommunity">뒤로가기</button>
    <hr>
    <review-comment :comments="review.comments" />
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
    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    goToUpdate: function() {
      if (this.review.user.id === this.$store.state.user.id) {
        this.$router.push({name: 'Review', params: {reviewId: this.$route.params.reviewId}})
      }
    },
    deleteReview: function() {
      if (this.review.user.id === this.$store.state.user.id) {
        axios({
          headers: this.setToken(),
          method: 'delete',
          url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`
        })
          .then(() => this.$router.push({name: 'Community'}))
          .catch(() => this.notFound())
      }
    },
    likeReview: function() {
      axios({
        
      })
    },
    goToCommunity: function() {
      this.$router.push({name: 'Community'})
    },
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`
    })
      .then(res => this.review = res.data)
      .catch(() => this.notFound())
  }
}
</script>

<style>

</style>