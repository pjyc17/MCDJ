<template>
  <div class="h1tag">
    <h1>회원가입</h1>
    <div>
      <div>
        <input type="text" id="username" v-model="credentials.username" placeholder="사용자이름" class="input">
      </div>
      <div>
        <input type="password" id="password" v-model="credentials.password" placeholder="비밀번호" class="input">
      </div>
      <div>
        <input type="password" id="password2" placeholder="비밀번호 확인" class="input"
          v-model="credentials.password2"
          @keyup.enter="signup"
        >
      </div>
      <div @click="signup" class="signup-btn">회원가입</div>
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
        username: '',
        password: '',
        password2: '',
      },
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
        })
        .catch(() => {
          alert("잘못 입력하셨어요!")
          this.credentials.password = ''
          this.credentials.password2 = ''
        })
    }
  }
}
</script>

<style>
.h1tag {
  position: relative;
  top: calc(50vh - 220px);
  text-align: center;
}
.input {
  font-size: 1rem;
  height: 2.5rem;
  width: 30rem;
}
.signup-btn {
  cursor: pointer;
  margin: 1rem 0 0 0;
  height: 2.5rem;
  line-height: 2.5rem;
  display: inline-block;
  width: 30rem;
  background-color: #1AAB8A;
  font-weight: bold;
  font-size:1.2rem;
  border-radius: 0.3rem;
}
@font-face {
  font-family: 'Sucrose Bold Two';
  src: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/sucrose.woff2') format('woff2');
}
</style>