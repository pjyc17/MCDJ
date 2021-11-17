<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{name: 'Home'}">Home</router-link> | 
      <span v-if="isLogin">
        <router-link @click.native="logout" to="">Logout</router-link>
      </span>
      <span v-else>
        <router-link data-bs-toggle="modal" data-bs-target="#loginModal" to="">Login</router-link>
      </span>
    </div>
    <router-view/>

    <!-- Login 모달 -->
    <div class="modal fade" id="loginModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">로그인</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body modal-body-box">
            <label for="username">유저 이름{{'\u00a0'}}{{'\u00a0'}}</label>
            <input type="text" id="username" v-model="credentials.username"><br> <br>
            <label for="password">비밀번호{{'\u00a0'}}{{'\u00a0'}}</label>
            <input type="password" id="password" v-model="credentials.password" @keyup.enter="login"><br> <br>
            <div class="rflex w-100">
              <a class="no-decoration-text" href="/signup">회원가입</a>
              <div @click="login" class="btn btn-sm btn-primary" data-bs-dismiss="modal">로그인</div>
            </div>
          </div>
          <hr>
          <div class="mb-3">
            <img class=btn @click="googleLogin" src="@/assets/googlelogo.png" alt="구글로그인">
            <img class=btn @click="googleLogin" src="@/assets/naverlogo.png" alt="네이버로그인">
            <img class=btn @click="googleLogin" src="@/assets/kakaologo.png" alt="카카오로그인">
          </div>
        </div>
      </div>
    </div>
    <!--  -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      isLogin: false,
    }
  },
  created() {
    if (localStorage.getItem('MCDJ_jwt')) {
      this.isLogin = true
    }
  },
  updated() {
    if (localStorage.getItem('MCDJ_jwt')) {
      this.isLogin = true
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${this.$store.state.domain}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('MCDJ_jwt', res.data.token)
          this.isLogin = true
          // this.$router.push({name: 'Home'}).catch(() => {})
          if (this.$route.path !== '/') this.$router.push({name: 'Home'})
        })
        .catch(err => console.log(err))
    },
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('MCDJ_jwt')
      if (this.$route.path !== '/') this.$router.push({name: 'Home'})
    },
    googleLogin: function() {
      // window.open("/", "", "_blank");
      console.log(this.$store.state)
      window.open(`${this.$store.state.domain}/accounts/google/login/`, "_blank", "width=500,height=600,top=200,left=750,")
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.no-decoration-text {
  text-decoration: none;
  /* color: black; */
}
.modal-body-box {
  width: 20rem;
  margin: 0 auto;
}
.rflex {
  display: flex;
  justify-content: space-between;
}
</style>
