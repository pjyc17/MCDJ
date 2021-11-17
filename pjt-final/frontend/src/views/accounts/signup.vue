<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="credentials.username">
      <div>
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model="credentials.password">
      </div>
      <div>
        <label for="password2">비밀번호 확인:</label>
        <input type="password" id="password2" 
          v-model="credentials.password2"
          @keyup.enter="signup"
        >
      </div>
      <button @click="signup">Signup</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        password2: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${this.$store.state.domain}/accounts/signup/`,
        data: this.credentials,
      })
        .then(() => {
          axios({
            method: 'post',
            url: `${this.$store.state.domain}/accounts/api-token-auth/`,
            data: this.credentials,
          })
            .then(res => {
              localStorage.setItem('MCDJ_jwt', res.data.token)
              this.$router.push({name: 'Home'})
            })
            .catch(err => console.log(err))
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>