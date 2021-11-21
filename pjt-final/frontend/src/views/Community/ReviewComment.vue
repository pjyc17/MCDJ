<template>
  <div>
    <div v-if="$store.state.user.id !== 0">
      <!-- <label for="comment">댓글</label> -->
      <input v-model="comment" type="text"><button @click="createComment">입력</button>
    </div>
    <div v-for="comment in comments" :key="comment.id">
      {{comment.content}} - {{comment.user.username}} <br> {{convertDate(comment.created)}} <br>
      <button @click="deleteComment(comment)" v-if="comment.user.id === $store.state.user.id">X</button>
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

<style>

</style>