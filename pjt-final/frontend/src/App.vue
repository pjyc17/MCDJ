<template>
  <div id="app">
    <nav id="nav" class="navbar navbar-expand-md navbar-light">
      <div class="container-fluid">
        <router-link :to="{name: 'Home'}"><img src="@/assets/MCDJHome.png" alt="" height="40px"></router-link>
        <div id="search-bar">
          <select v-model="selected" class="fontsize-20">
            <option value="*">전체</option>
            <option v-for="genre in $store.state.allGenres" :key="genre.id" :value="genre.id">{{genre.name}}</option>
          </select>
          <input @keyup.enter="searchMovie" v-model="keyword" type="text" class="fontsize-20">
          <button @click="searchMovie"><i class="fas fa-search cursor"></i></button>
        </div>
      </div>
      <i @click="goUp" class="fas fa-caret-up cursor" :class="{'text-primary': isLogin, 'text-secondary': !isLogin}" style="font-size: 5rem;"></i>{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}
      <button class="btn z-top" :class="{'btn-primary': isLogin, 'btn-secondary': !isLogin}" type="button" data-bs-toggle="offcanvas" data-bs-target="#myOffcanvas" aria-controls="myOffcanvas">MENU</button>

    </nav>
      <div class="offcanvas offcanvas-end text-black" data-bs-scroll="true" tabindex="-1" id="myOffcanvas" aria-labelledby="myOffcanvasLabel">
        <div v-if="isLogin" id="myOffcanvas" data-bs-dismiss="offcanvas"><router-link :to="{name: 'Profile2', params: {userId: $store.state.user.id}}" style="text-decoration-line: none;"><div class="offcanvas-item">Profile</div></router-link></div>
        <div v-if="isLogin">
          <router-link @click.native="logout" to="" data-bs-dismiss="offcanvas" style="text-decoration-line: none;"><div class="offcanvas-item">Logout</div></router-link>
        </div>
        <div v-else>
          <router-link to="" style="text-decoration-line: none;"><b id="show-btn" @click="$bvModal.show('loginModal')" data-bs-dismiss="offcanvas"><div class="offcanvas-item">Login</div></b></router-link>
        </div>
        <div data-bs-dismiss="offcanvas"><router-link :to="{name: 'Chronology'}" style="text-decoration-line: none;"><div class="offcanvas-item">Chronology</div></router-link></div>
        <div data-bs-dismiss="offcanvas"><router-link :to="{name: 'Community'}" style="text-decoration-line: none;"><div class="offcanvas-item">Community</div></router-link></div>
      </div>
    <!-- 검색바 -->
    <div style="height: 96px;"></div>
    <router-view/>

    <!-- 새로고침 방지용 -->

    <!-- Login 모달 -->
    <b-modal id="loginModal" hide-footer>
      <template #modal-title>
        <div class="text-black">로그인</div>
      </template>
      <div class="d-block text-center">
        <label class="text-black" for="username">유저 이름{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</label>
        <input type="text" id="username" v-model="credentials.username"><br> <br>
        <label class="text-black" for="password">비밀번호{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</label>
        <input type="password" id="password" v-model="credentials.password" @keyup.enter="login"><br> <br>
        <div class="rflex w-100">
          <a class="no-decoration-text" href="/signup">회원가입</a>
          <button @click="login" class="btn btn-sm btn-primary">로그인</button>
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
    <!-- <img height="250" id="helper-dog" src="@/assets/dogyawn.gif" alt="강아지 도우미"> -->
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
      selected: '*',
      keyword: null,
      isCanvas: false,
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    getUser: function() {
      axios({
        headers: this.setToken(),
        method:'get',
        url: `${this.$store.state.domain}/accounts/user/`,
      })
        .then(res => {
          this.$store.commit('GET_USER', {id: res.data.id, username: res.data.username,})
          if (res.data.birthday) {
            this.$store.commit('GET_BIRTHDAY', {year: parseInt(res.data.birthday.birthday.substring(0,4)), month: parseInt(res.data.birthday.birthday.substring(5,7)), date: parseInt(res.data.birthday.birthday.substring(8,10)),})
          }
        })
        .catch(() => {
          alert("로그아웃 되었습니다.")
          this.logout()
        })
    },
    login: function () {
      axios({
        method: 'post',
        url: `${this.$store.state.domain}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('MCDJ_jwt', res.data.token)
          this.isLogin = true
          this.getUser()
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
      this.$store.commit('GET_USER', this.$store.state.anonymousUser)
      if (this.$route.path !== '/') this.$router.push({name: 'Home'})
    },
    googleLogin: function() {
      // window.open("/", "", "_blank");
      console.log(this.$store.state)
      window.open(`${this.$store.state.domain}/accounts/google/login/`, "_blank", "width=500,height=600,top=200,left=750,")
    },
    searchMovie: function () {
      const keyword = this.keyword.trim()
      if (keyword) {
        if (this.$route.name !== 'Movies') {
          this.$router.push({name: 'Movies', params: {genreId: this.selected, keyword: keyword}})
        }
        if (this.selected === '*') {
          axios({
            method: 'get',
            url: `${this.$store.state.domain}/movies/search/${keyword}/`,
          })
            .then(res => {
              this.goUp()
              this.$store.commit('RESET_SHOWNMOVIES')
              this.$store.commit('SEARCH_MOVIES', res.data)
              this.$store.commit('SPLICE_SEARCH_MOVIES')
            })
        } else {
          axios({
            method: 'get',
            url: `${this.$store.state.domain}/movies/${this.selected}/search/${this.keyword}/`,
          })
            .then(res => {
              window.scrollTo(0, 0)
              this.$store.commit('RESET_SHOWNMOVIES')
              this.$store.commit('SEARCH_MOVIES', res.data)
              this.$store.commit('SPLICE_SEARCH_MOVIES')
            })
        }
        // window.location.href = `/movies/${this.selected}/${keyword}`
      } else {
        this.keyword = null
      }
    },
    goUp: function() {
      window.scrollTo(0, 0)
    }
  },
  computed: {
    myOffcanvas: function() {
      var myOffcanvas = window.document.getElementById('myOffcanvas')
      return myOffcanvas
    }
  },
  created() {
    if (localStorage.getItem('MCDJ_jwt')) {
      this.isLogin = true
      this.getUser()
    }
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/recommend/all/`
    })
      .then(res => this.$store.commit('GET_ALL_MOVIES', res.data))
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/genres/all/`
    })
      .then(res => this.$store.commit('GET_ALL_GENRES', res.data))
  },
  updated() {
    if (!this.isCanvas) {
      this.myOffcanvas.setAttribute('style', 'top: 96px; width: 16rem; background-color: transparent;')
      this.isCanvas = true
    }
  }
  // updated() {
  //   if (localStorage.getItem('MCDJ_jwt')) {
  //     this.isLogin = true
  //     this.getUser()
  //   }
  // },
}
</script>

<style>
#test {
  background-color:unset;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 100%;
}
/* #nav {
  padding: 30px;
} */
#nav {
  /* background-color: #141414; */
  border-bottom: 1px;
  width: 100%;
  position: fixed;
  z-index: 1000;
  top: 0;
  /* transform: translate(-50%, -0%); */
}
#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
}
/* #nav a.router-link-exact-active {
  color: #42b983;
} */
.z-top {
  z-index: 1000;
}
.no-decoration-text {
  text-decoration: none;
  /* color: black; */
}
.modal-body-box {
  width: 20rem;
  margin: 0 auto;
}
/* .offcanvas-item {
  text-align: left;
  line-height: 4rem;
  font-size: 2rem;
  height: 4rem;
  background-color:#f0f0f0;
  border-color: #141414;
  border-style: solid;
  border-width: 1px;
} */
.offcanvas-item{
  line-height: 4rem;
  background:#1AAB8A;
  color:#fff;
  margin: 1px;
  position:relative;
  height:4rem;
  font-size:1.6em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
}
.offcanvas-item:hover{
  background:#fff;
  color:#1AAB8A;
}
.offcanvas-item:before,.offcanvas-item:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #1AAB8A;
  transition:400ms ease all;
}
.offcanvas-item:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.offcanvas-item:hover:before,.offcanvas-item:hover:after{
  width:100%;
  transition:800ms ease all;
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
#search-bar {
  display: flex;
  justify-content: center;
  /* height: 40px; */
  position: fixed;
  z-index: 1000;
  top: 48px;
  left: 50%;
  transform: translate(-50%, -50%);
}
.fontsize-20 {
  font-size: 20px;
}
.fontsize-15 {
  font-size: 15px;
}
.fontsize-12 {
  font-size: 12px;
}
.fontsize-10 {
  font-size: 10px;
}
.float-left {
  float: left;
}
.flex {
  display: flex;
  flex-wrap: wrap;
}
.flex-center {
  display: flex;
  justify-content: center;
}
.flex-left {
  display: flex;
  justify-content: left;
}
.flex-right {
  display: flex;
  justify-content: right;
}
.flex-align-ceter {
  display: flex;
  align-items: center;
}
.text-center {
  text-align: center;
}
.text-left {
  text-align: left;
}
.cursor {
  cursor: pointer;
}
.disabled-cursor {
  cursor: default;
}
.inline-block {
  display: inline-block;
}
.movie-card {
  background-color: transparent;
  cursor: pointer;
  width: 10rem;
  margin: 1rem 0.5rem;
}
.card-img-box {
  background-color: #141414;
  /* background-color: transparent; */
  position: relative;
  height: 0;
  padding-top: 150%;
}
.card-img {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 100%;
}
.movie-card:hover {
  border-radius: 2px;
  border-style: solid;
  border-color:#eddc5a;
  border-width: 2px;
  -webkit-transform:scale(1.1);
  -moz-transform:scale(1.1);
  -ms-transform:scale(1.1);   
  -o-transform:scale(1.1);
  transform:scale(1.1);
}
</style>
