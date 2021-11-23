<template>
  <div class="container review-box text-left" v-if="review">
    <hr>
    <h2>{{review.title}}</h2>
    <div class="fontsize-12">
      <span>{{review.user.username}}가 </span>
      <span v-if="review.created === review.updated">{{convertDate(review.created)}}에 작성함</span>
      <span v-else>{{convertDate(review.updated)}}에 수정함 <br>({{convertDate(review.created)}}에 작성됨)</span>
    </div>
    <br>
    <div><pre>{{review.content}}</pre></div>
    <br>
    <div class="text-center">
      <i class="fas fa-thumbs-up" @click="likeReview"
        :class="{'cursor': $store.state.user.id, 'is-liked': isLiked}"
      >
      </i>
       {{review.likes_cnt}}
    </div>
    <div class="flex-right">
      <div v-if="review.user.id === $store.state.user.id">
        <button @click="goToUpdate">수정</button>
        <button @click="deleteReview">삭제</button>
      </div>
      <button @click="goToCommunity">뒤로가기</button>
    </div>
    <hr>
    <div class="flex-center">
      <review-comment :comments="review.comments" />
    </div>
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
      isLiked: false,
    }
  },
  methods: {
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
    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },
    likeReview: function() {
      if (this.$store.state.user.id !== 0) {
        axios({
          headers: this.setToken(),
          method: 'put',
          url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/like/`
        })
          .then(res => {
            this.review.likes_cnt = res.data.likes_cnt
            this.isLiked = res.data.isLiked
          })
          .catch(() => this.notFound())
      }
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
      .then(res => {
        this.review = res.data
        if (this.$store.state.user.id !== 0) {
          axios({
            headers: this.setToken(),
            method: 'get',
            url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/like/`
          })
          .then(res => this.isLiked = res.data.isLiked)
        }
      })
      .catch(() => this.notFound())
  }
}
</script>

<style>
.is-liked {
  color: royalblue;
}
.text-left {
  text-align: left;
}
.text-center {
  text-align: center;
}
.fontsize-12 {
  font-size: 12px;
}
.flex-right {
  display: flex;
  justify-content: right;
}
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
.flex-center {
  display: flex;
  justify-content: center;
}
</style>