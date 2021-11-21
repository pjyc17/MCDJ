<template>
  <div>
    여기는 커뮤니티
    <button v-if="$store.state.user.id !== 0" @click="goToCreate">Create</button>
    <div class="cursor" @click="goToDetail(review.id)" v-for="review in reviews" :key="review.id">
      <hr>
      <h2>{{review.title}}</h2>
      <p>{{review.user.username}}</p>
      <p>수정: {{convertDate(review.updated)}}</p>
      <p>좋아요: {{review.likes_cnt}} / 댓글: {{review.reviews_cnt}}</p>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community',
  data: function() {
    return {
      reviews: [],
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    goToDetail: function(reviewId) {
      this.$router.push({name: 'ReviewDetail', params: {reviewId: reviewId}})
    },
    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },
    goToCreate: function() {
      if (this.$store.state.user.id !== 0) {
        this.$router.push({name: 'Review', params: {reviewId: 'create'}})
      }
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/community/all/`
    })
      .then(res => this.reviews = res.data)
  }
}
</script>

<style scoped>
.cursor {
  cursor: pointer;
}
</style>