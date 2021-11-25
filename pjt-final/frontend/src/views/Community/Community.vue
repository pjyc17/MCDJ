<template>
  <div class="container">
    <div class="flex-right">
      <button v-if="$store.state.user.id !== 0" @click="goToCreate">Create</button>
    </div>
    <div class="rl-line"></div>
    <!-- <div class="cursor" @click="goToDetail(review.id)" v-for="review in reviews" :key="review.id">
      <h2>{{review.title}}</h2>
      <div class="fontsize-10">
        <span>{{review.user.username}}(이)가 </span>
        <span v-if="review.updated !== review.created">
          {{convertDate(review.updated)}}에 수정함
        </span>
        <span v-else>
          {{convertDate(review.created)}}에 작성함
        </span>
      </div>
      <div class="fontsize-12">좋아요: {{review.likes_cnt}}개 / 댓글: {{review.reviews_cnt}}개</div>
      <div class="rl-line"></div>
    </div> -->
    <table border="1" bordercolor="#949597" width="100%" height="100%">
      <th class="fontsize-20 py-2">작성자</th><th class="fontsize-20" width="50%">제목</th><th class="fontsize-20">좋아요</th><th class="fontsize-20">댓글</th><th class="fontsize-20">작성</th>
      <tr class="table-row" v-for="review in shownReviews" :key="review.id">
        <td class="py-2 cursor hover-btn" @click="goToProfile(review.user.id)">{{review.user.username}}</td><td class="cursor" @click="goToDetail(review.id)">{{review.title}}</td><td>{{review.likes_cnt}}</td><td>{{review.reviews_cnt}}</td><td class="fontsize-10">{{convertDate(review.created)}}</td>
      </tr>
    </table>
    <div class="flex-center mt-3">
      <i @click="moveOnePage(-1)" class="fas fa-caret-left mx-3 cursor" style="font-size: 2rem;"></i>
      <input @keyup.enter="movePage" type="text" style="width: 5rem; text-align: center;" v-model="page2">
      <i @click="moveOnePage(1)" class="fas fa-caret-right mx-3 cursor" style="font-size: 2rem;"></i>
    </div>
    <div class="flex-center">{{page}} of {{maxPage}}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community',
  data: function() {
    return {
      reviews: [],
      shownReviews: [],
      cnt: 15,
      page: 1,
      page2: 1,
      maxPage: 1,
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    goToDetail: function(reviewId) {
      this.$router.push({name: 'ReviewDetail', params: {reviewId: reviewId}})
    },
    goToProfile: function(userId) {
      this.$router.push({name: 'Profile', params: {userId: userId}})
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
    },
    movePage: function() {
      if (isNaN(this.page2)) {this.page2 = this.page}
      this.page2 = parseInt(this.page2)
      if (this.page2 < 1) {this.page2 = 1} 
      else if(this.page2 > this.maxPage) {this.page2 = this.maxPage}
      this.page = this.page2
      this.shownReviews = this.reviews.slice(this.cnt * (this.page - 1), this.cnt * this.page)
    },
    moveOnePage: function(num) {
      this.page += num
      if (this.page < 1) {this.page = 1} 
      else if(this.page > this.maxPage) {this.page = this.maxPage}
      this.page2 = this.page
      this.shownReviews = this.reviews.slice(this.cnt * (this.page - 1), this.cnt * this.page)
    },
  },
  created() {
    window.scrollTo(0, 0)
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/community/all/`
    })
      .then(res => {
        this.reviews = res.data
        // this.cnt = parseInt((window.innerHeight - 260) / 41)
        this.maxPage = parseInt((this.reviews.length - 0.1) / this.cnt) + 1
        this.shownReviews = this.reviews.slice(this.cnt * (this.page - 1), this.cnt * this.page)
      })
  },
  destroyed() {
    window.scrollTo(0, 0)
  }
}
</script>

<style scoped>
.rl-line {
  width: 100%;
  height: 2px;
  background-color: #949597;
  margin: 1rem 0;
}
.hover-btn:hover {
  z-index: 999;
  color: #eddc5a;
}
.table-row {
  border-color: #949597;
  border-width: 1px;
}
</style>