<template>
  <div class="flex-col">
    <div v-if="$store.state.user.id !== 0" class="comment-input-box">
      <!-- <label for="comment">댓글</label> -->
      <textarea v-model="comment" type="text" rows="2" style="width:100%;" />
      <button @click="createComment">입력</button>
    </div>
    <div v-for="comment in comments" :key="comment.id" class="comment-box">
      <div>
        {{comment.content}}{{'\u00a0'}}{{'\u00a0'}}
        <div class="delete-comment" @click="deleteComment(comment)" v-if="comment.user.id === $store.state.user.id">X</div>
      </div>
      <div class="fontsize-12">
        {{comment.user.username}}가 {{convertDate(comment.created)}}에 작성함
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewComment',
  props: {
    comments: {
      type: Array,
    }
  },
  data: function() {
    return {
      comment: '',
    }
  },
  methods: {
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    createComment: function() {
      const comment = this.comment.trim()
      if (comment) {
        axios({
          headers: this.setToken(),
          method: 'post',
          url: `${this.$store.state.domain}/community/${this.$route.params.reviewId}/comment/`,
          data: {content: this.comment,},
        })
          .then((res) => this.comments.push(res.data))
          .catch(() => this.$router.push({name: 'NotFound'}))
      } else {alert("빈칸이 있어요!")}
      this.comment = ''
    },
    deleteComment: function(deletedComment) {
      if (deletedComment.user.id === this.$store.state.user.id) {
        axios({
          headers: this.setToken(),
          method: 'delete',
          url: `${this.$store.state.domain}/community/comment/${deletedComment.id}/`,
        })
          .then(() => {
            this.comments.splice(this.comments.indexOf(deletedComment), 1)
          })
          .catch(() => this.$router.push({name: 'NotFound'}))
      }
    },
    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },
  },
}
</script>

<style scoped>
.flex-col {
  width: 95%;
  display: flex;
  flex-direction: column;
  justify-items: stretch;
  align-items: center;
}
.comment-input-box {
  width: 100%;
  display: flex;
  /* justify-content: center; */
}
.comment-box {
  width: 100%;
  border-radius: 2px;
  border-style: solid; 
  border-width: 1px; 
  border-color: #949597;
  background-color: #35363a;
}
.fontsize-12 {
  font-size: 12px;
}
.delete-comment {
  font-size: 10px;
  color: #949597;
  display: inline-block;
  cursor: pointer;
  padding: 0 3px;
  border-radius: 2px;
  border-style: solid; 
  border-width: 1px; 
  border-color: #949597;
}
</style>