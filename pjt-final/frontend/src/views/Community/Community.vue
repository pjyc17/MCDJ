<template>
  <div class="container">
    <div class="flex-right">
      <button v-if="$store.state.user.id !== 0" @click="goToCreate">Create</button>
    </div>
    <hr>
    <div class="cursor" @click="goToDetail(review.id)" v-for="review in reviews" :key="review.id">
      <h2>{{review.title}}</h2>
      <div class="fontsize-12">
        <span>{{review.user.username}}가 </span>
        <span v-if="review.updated !== review.created">
          {{convertDate(review.updated)}}에 수정함
        </span>
        <span v-else>
          {{convertDate(review.created)}}에 작성함
        </span>
      </div>
      <p>좋아요: {{review.likes_cnt}}개 / 댓글: {{review.reviews_cnt}}개</p>
      <hr>
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
.flex-right {
  display: flex;
  justify-content: right;
}
.fontsize-12 {
  font-size: 12px;
}
</style>