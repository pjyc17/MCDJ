<template>
  <div class="container review-box text-left" v-if="review">
    <div class="row">
      <div class="box col-12 col-xl-8">
        <h2 class="my-3 mx-3">{{review.title}}</h2>
        <hr>
        <div class="content-box mx-3"><pre>{{review.content}}</pre></div>
        <br>
        <div class="text-center">
          <i class="fas fa-thumbs-up" @click="likeReview"
            :class="{'cursor': $store.state.user.id, 'is-liked': isLiked}"
          >
          </i>
          {{review.likes_cnt}}
        </div>
        <div class="review-bottom mx-3">
          <div class="additional-info fontsize-12">
            <span>작성자 : <span @click="goToProfile" class="fontsize-15 cursor hover-btn">{{review.user.username}}</span></span> <br>
            <span v-if="review.created === review.updated">{{convertDate(review.created)}}에 작성됨</span>
            <span v-else>{{convertDate(review.updated)}}에 수정됨 <br>({{convertDate(review.created)}}에 작성됨)</span>
          </div>
          <div class="inline-block">
            <div class="inline-block" v-if="review.user.id === $store.state.user.id">
              <button @click="goToUpdate">수정</button>
              <button @click="deleteReview">삭제</button>
            </div>
            <button @click="goToCommunity">뒤로가기</button>
          </div>
        </div>
      </div>
      <div class="box col-12 col-xl-4">
        <div class="flex-center">
          <review-comment :comments="review.comments" />
        </div>
      </div>
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
    goToProfile: function() {
      this.$router.push({name: 'Profile', params: {userId: this.review.user.id}})
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
      url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/`,
      // console.log(`${this.$route.params.reviewId}`)
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

<style scoped>
.is-liked {
  color: royalblue;
}
.review-box {
  border-radius: 1rem;
  border-style: solid; 
  border-width: 2px; 
  padding: 12px 24px; 
  word-break: break-all;
  border-color: LightGray; 
  background-color:#141414;
  opacity: 100%;
  color: white;
}
.box {
  padding: 0;
  border-radius: 5px;
  border-style: solid; 
  border-width: 1px; 
  border-color: LightGray; 
}
/* .content-box {
  min-height: 30vh;
} */
.review-bottom {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: flex-end;
}
.additional-info {
  display: inline-block;
  padding: 3px;
  /* border-radius: 3px;
  border-style: solid;
  border-width: 1px;
  border-color: #949597; */
}
.hover-btn:hover {
  color: #eddc5a;
}
</style>