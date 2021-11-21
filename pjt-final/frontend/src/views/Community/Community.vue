<template>
  <div>
    여기는 커뮤니티
    <create-review/>
  </div>
</template>

<script>
import axios from 'axios'
import CreateReview from '@/views/Community/CreateReview.vue'

export default {
  name: 'Community',
  components: {
    CreateReview,
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
  },
  created() {
    axios({
      headers: this.setToken(),
      method: 'get',
      url: `${this.$store.state.domain}/community/all/`
    })
      .then(res => this.$store.commit('GET_ALL_REVIEWS', res.data))
  }
}
</script>

<style>

</style>