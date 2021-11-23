<template>
  <div>
    <h1>{{ profile.user.username }}'s Profile</h1>
    <label for="birthday">생년월일</label>
    <input type="text" id="birthday" v-model="credentials.birthday">
  <div class="flex-right">
      <div v-if="profile.user.birthday === $store.state.user.birthday">
        <button @click="goToUpdate">수정</button>
        <button @click="deleteBirthday">삭제</button>
      </div>
      <button @click="goToProfile">뒤로가기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileEdit',
  props: {
    birthday: {
      type: Object,
    }
  },
  data: function () {
    return {
      credentials: {
        birthday: null,
      }
    }
  },
  methods: {
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    // setToken: function() {
    //   return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    // },
    goToUpdate: function() {
      if (this.profile.user.birthday === this.$store.state.user.birthday) {
        this.$router.push({name: 'Profile', params: {userId: this.$route.params.userId}})
      }
    },
    deleteBirthday: function () {
      if (this.profile.user.birthday === this.$store.state.user.birthday) {
        axios({
          method: 'delete',
          url: `${this.$store.state.domain}/accounts/${this.$route.params.userId}`
        })
          .then(() => this.$router.push({name: 'Profile'}))
          .catch(() => this.notFound())
      }
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/accounts/${this.$store.state.birthday.month}${this.$store.state.birthday.date}/`,
    })
      .then(res => {
        this.birthday = res.birthday
      
      })
      .catch(() => this.notFound())
  }
}
</script>

<style>

</style>