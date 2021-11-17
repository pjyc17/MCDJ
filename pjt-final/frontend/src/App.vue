<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{name: 'Home'}">Home</router-link> | 
      <span v-if="isLogin">
        <router-link @click.native="logout" to="">Logout</router-link>
      </span>
      <span v-else>
        <router-link to=""><b id="show-btn" @click="$bvModal.show('loginModal')">Login</b></router-link>
      </span>
    </div>
    <router-view/>

    <!-- Login 모달 -->
    <b-modal id="loginModal" hide-footer>
      <template #modal-title>
        <div class="text-black">로그인</div>
      </template>
      <template button>
        O
      </template>
      <div class="d-block text-center">
        <label class="text-black" for="username">유저 이름{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</label>
        <input type="text" id="username" v-model="credentials.username"><br> <br>
        <label class="text-black" for="password">비밀번호{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</label>
        <input type="password" id="password" v-model="credentials.password" @keyup.enter="login"><br> <br>
        <div class="rflex w-100">
          <a class="no-decoration-text" href="/signup">회원가입</a>
          <div @click="login" class="btn btn-sm btn-primary">로그인</div>
        </div>
      </div>
      <hr>
      <div class="SLbox">
        <img class=btn @click="googleLogin" src="@/assets/googlelogo.png" alt="구글로그인">
        <img class=btn @click="googleLogin" src="@/assets/naverlogo.png" alt="네이버로그인">
        <img class=btn @click="googleLogin" src="@/assets/kakaologo.png" alt="카카오로그인">
      </div>
    </b-modal>
    <!--도우미 개-->
    <img height="250" id="helper-dog" src="@/assets/dogyawn.gif" alt="강아지 도우미">
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
          // const loginModal = new bootstrap.Modal(document.getElementById('loginModal'))
          // loginModal.hide()
          // this.$router.push({name: 'Home'}).catch(() => {})
          this.$root.$emit('bv::hide::modal', 'loginModal', '#btnShow')
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
  /* color: #2c3e50; */
  height: 100%;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
}

/* #nav a.router-link-exact-active {
  color: #42b983;
} */

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
  justify-content:space-around;
}
#helper-dog {
  cursor: url(assets/bone.png), pointer;
  position: fixed;
  right: 0;
  bottom: 0;
}
.text-black {
  color: black;
}
.SLbox {
  display: flex;
  justify-content: center;
  margin: 0 auto;
}
</style>
