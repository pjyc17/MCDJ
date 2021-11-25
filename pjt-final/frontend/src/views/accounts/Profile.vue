<template>
  <div id="app">
    <div id="gost-bg"></div>
    <header>
      <div v-if="person">
        <h1 class="yello-font inline-block">{{ person.username }}'s Profile</h1><br>
        <div v-if="$route.params.userId === $store.state.user.id && isBirthday" @click="showBirthdayForm" class="hover-btn cursor inline-block">
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 1 && person.birthday.birthday.substring(8,10) >= 20) || (person.birthday.birthday.substring(5,7) == 2 && person.birthday.birthday.substring(8,10) <= 18) ">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/물병자리.png" alt="">star : Aquarius </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 2 && person.birthday.birthday.substring(8,10) >= 19) || (person.birthday.birthday.substring(5,7) == 3 && person.birthday.birthday.substring(8,10) <= 20)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/물고기자리.png" alt="">star : Prisces </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 3 && person.birthday.birthday.substring(8,10) >= 21) || (person.birthday.birthday.substring(5,7) == 4 && person.birthday.birthday.substring(8,10) <= 19)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/양자리.png" alt=""> star : Aries </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 4 && person.birthday.birthday.substring(8,10) >= 20) || (person.birthday.birthday.substring(5,7) == 5 && person.birthday.birthday.substring(8,10) <= 20)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/황소자리.png" alt="">star : Taurus </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 5 && person.birthday.birthday.substring(8,10) >= 21) || (person.birthday.birthday.substring(5,7) == 6 && person.birthday.birthday.substring(8,10) <= 21)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt="">star : Gemini </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 6 && person.birthday.birthday.substring(8,10) >= 22) || (person.birthday.birthday.substring(5,7) == 7 && person.birthday.birthday.substring(8,10) <= 22)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/게자리.png" alt="">star : Cancer </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 7 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 8 && person.birthday.birthday.substring(8,10) <= 22)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/사자자리.png" alt="">star : Leo </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 8 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 9 && person.birthday.birthday.substring(8,10) <= 23)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/처녀자리.png" alt="">star : Virgo </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 9 && person.birthday.birthday.substring(8,10) >= 24) || (person.birthday.birthday.substring(5,7) == 10 && person.birthday.birthday.substring(8,10) <= 22)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/천칭자리.png" alt="">star : Libra </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 10 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 11 && person.birthday.birthday.substring(8,10) <= 22)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/전갈자리.png" alt="">star : Scorpio </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 11 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 12 && person.birthday.birthday.substring(8,10) <= 21)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/사수자리.png" alt="">star : Sagittarius </h3>
          <h3 class="hover-btn" v-if="(person.birthday.birthday.substring(5,7) == 12 && person.birthday.birthday.substring(8,10) >= 22) || (person.birthday.birthday.substring(5,7) == 1 && person.birthday.birthday.substring(8,10) <= 19)">age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}<br><img height="40" src="@/assets/별자리/염소자리.png" alt="">star : Capricorn </h3>
          <div class="flex-center">
          </div>
        </div>
        <br>
        <div v-if="isShow && $route.params.userId === $store.state.user.id">
          <div>
            <b-form-select v-model="y_selected" :options="y_options" multiple :select-size="1"></b-form-select>
            <b-form-select v-model="m_selected" :options="m_options" multiple :select-size="1"></b-form-select>
            <b-form-select v-model="d_selected" :options="d_options" multiple :select-size="1"></b-form-select>
          </div>
          <div>
            <div> 
              <span v-if="y_selected">{{ y_selected[0] }}년 </span> 
              <span v-if="m_selected">{{ m_selected[0] }}월 </span> 
              <span v-if="d_selected">{{ d_selected[0] }}일 </span>
              <br>
              <!-- <strong v-if="y_selected">{{ 2022 - y_selected[0] }}</strong> -->
            </div>
            <div v-if="isBirthday">
              <button @click="updateBirthday">수정</button>
            </div>
            <div v-else>
              <button @click="createBirthday">작성</button>
            </div>
          </div>
        </div>
        <!--   <h3>followings : {{  }} / followers : {{  }}</h3> -->
        <br>
        <div class="row">
          <div class="container col-12 col-sm-6 col-lg-4 col-xl-3">
            <h3 class="yello-font">genre : </h3>
            <hr>
            <div v-for="genre in genres" :key="genre.id">
              <h5 @click="goToGenre(genre.id)" class="inline-block cursor">{{ genre.name }}</h5>
              <p> 연관성 : {{ (genre.point / gpoint * 100).toFixed(1) }}% </p>
            </div>
          </div>
        <!-- <div class="box">sd</div> -->
          <div class="container col-12 col-sm-6 col-lg-4 col-xl-3">
            <h3 class="yello-font">want : </h3>
            <hr>
            <div v-for="movie in carts" :key="movie.id">
              <strong @click="goToMovie(movie.id)" class="inline-block cursor">{{ movie.title }}</strong>
            </div>
          </div>
          <div class="container col-12 col-sm-6 col-lg-4 col-xl-3 text-center">
            <h3 class="yello-font">likes  : </h3>
            <hr>
            <div v-for="like_review in like_reviews" :key=like_review.id class="container2 text-center">
              <strong @click="goToReview(like_review.id)" class="cursor">{{ like_review.title }} <i class="fas fa-thumbs-up rightway">{{ like_review.likes_cnt }}</i></strong>
            </div>
          </div>
          <!-- <div class="container" style="word-break:break-all;word-wrap:break-word;"> -->
          <div class="container col-12 col-sm-6 col-lg-4 col-xl-3">
            <h3 class="yello-font">written : </h3>
            <hr>
            <div v-for="review in reviews" :key="review.id">
              <strong @click="goToReview(review.id)" class="inline-block cursor">{{ review.title }}</strong>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>
<script>
import axios from 'axios'
// import ProfileEdit from '@/views/accounts/ProfileEdit.vue'
// import Profile from '@/accounts/Profile.vue'

export default {
  name: 'Profile',
  components: {
    // ProfileEdit,
  },
  data: function() {
    const y_options = []
    const m_options = []
    const d_options = []
    for (let y_index = 1938; y_index < 2022; y_index++) {
      y_options.push({value: y_index, text: y_index})
    }
    for (let m_index = 1; m_index < 13; m_index++) {
      m_options.push({value: m_index, text: m_index})
    }
    for (let d_index = 1; d_index < 32; d_index++) {
      d_options.push({value: d_index, text: d_index})
    }
    return {
      person: null,
      genres: [],
      carts: [],
      like_reviews: [],
      reviews: [],
      isBirthday: false,
      isShow: false,
      y_selected: [this.$store.state.user.birthday.year], // Array reference
      m_selected: [this.$store.state.user.birthday.month], // Array reference
      d_selected: [this.$store.state.user.birthday.date], // Array reference
      y_options,
      m_options,
      d_options,
    }
  },
  methods: {
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    getProfile: function() {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/accounts/${this.$route.params.userId}/`
      })
        .then(res => {this.person = res.data
          return res})
        .then((res) => {
          if (res.data.birthday) {
            const birth = this.person.birthday.birthday.substring(5,7) + this.person.birthday.birthday.substring(8,10)
            // console.log(birth.month)
            this.isBirthday = true
            this.isShow = false
            axios({
              method: 'get',
              url: `${this.$store.state.domain}/movies/recommend/genres/${birth}/${this.$route.params.userId}/`
            })
              .then(res => this.genres = res.data.genres.splice(0,3))
              // .then(res => console.log(res.data))
          } else {
            const birth = this.$store.state.today.month * 100 + this.$store.state.today.date
            const birthday = `${this.$store.state.today.year}-${this.$store.state.today.month}-${this.$store.state.today.date}`
            this.person = {...this.person, birthday: {birthday: birthday}}
            this.isBirthday = false
            this.isShow = true
            axios({
              method: 'get',
              url: `${this.$store.state.domain}/movies/recommend/genres/${birth}/${this.$route.params.userId}/`
            })
              .then(res => this.genres = res.data.genres.splice(0,3))
          }
        })
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/user_cart/${this.$route.params.userId}/`
      })
        .then(res => this.carts = res.data)
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/community/liked_review/${this.$route.params.userId}/`
      })
        .then(res => this.like_reviews = res.data)
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/community/review/${this.$route.params.userId}/`
      })
        // .then(res => console.log(res.data))
        .then(res => this.reviews = res.data)
    },

    goToGenre: function(genreId) {
      // console.log(genreId)
      this.$router.push({name: 'GenreMovies', params: {genreId: genreId}})
    },
    goToMovie: function (movieId) {
      this.$router.push({name: 'MovieDetail', params: {movieId: movieId}})
    },  
    goToReview: function (reviewId) {
      this.$router.push({name: 'ReviewDetail', params: {reviewId: reviewId}})
    },
    goToHome: function() {
      this.$router.push({name:'Home'})
    },
    showBirthdayForm: function() {
      this.isShow = !this.isShow
    },
    updateBirthday: function() {
      const birthday = {
        year: this.y_selected[0],
        month: this.m_selected[0],
        date: this.d_selected[0],
      }
      axios({
        headers: this.setToken(),
        method: 'put',
        url: `${this.$store.state.domain}/accounts/birthday/`,
        data: {birthday: `${birthday.year}-${birthday.month}-${birthday.date}`},
      })
        .then()
      this.$store.commit('GET_BIRTHDAY', birthday)
      this.isShow=false
    },
    createBirthday: function() {
      const birthday = {
        year: this.y_selected[0],
        month: this.m_selected[0],
        date: this.d_selected[0],
      }
      if (birthday.year !== this.$store.state.today.year || birthday.month !== this.$store.state.today.month || birthday.date !== this.$store.state.today.date) {
        axios({
          headers: this.setToken(),
          method: 'put',
          url: `${this.$store.state.domain}/accounts/birthday/`,
          data: {birthday: `${birthday.year}-${birthday.month}-${birthday.date}`},
        })
          .then()
        this.$store.commit('GET_BIRTHDAY', birthday)
        this.isShow=false
        this.isBirthday = true
      } else {alert("유효하지 않은 값입니다.")}
    },
  },
  computed: {
    gpoint: function () {
      let gpoint = 0
      for (let genre of this.genres) {
        gpoint += genre.point
      }
      return gpoint
    }
  },
  created() {
    this.getProfile()
  },
}
</script>

<style scoped>
.yello-font {
  color: #eddc5a;
}
h3 {
  color: #949597;
}
h5 {
  font-weight: bold;
  color: #949597;
}
h5:hover {
  z-index: 999;
  color: #eddc5a;
}
strong {
  color: white;
  font-weight: bold;

}
strong:hover {
  z-index: 999;
  color: #eddc5a;
}
p {
  color: white;  font-weight: bold;
}
.btw {
  display: flex;
  justify-content: space-between;
}
.container2 {
  padding: 0px 60px;
}
/* .header-img { */
  /* position: relative; */
  /* height: 100vh;
  width: 100vw; */
  /* z-index: -1; */
  /* opacity:0.3; */
/* } */
#word{
  /* width: 100%; */
  /* height: 100%; */
  /* text-align: center; */
  position: relative;
  top: -10rem;
  font-family: 'Sucrose Bold Two';
  /* background: url(../../assets/gorhf.png) center 0  no-repeat; */
  background-size: cover;
  padding-top: 30vh;
  
  /* opacity: 0.3; */
  /* z-index: -999; */
}
/* #word {
  opacity: 1;
} */
#gost-bg{
  position: fixed;
  z-index: -1;
  top: 0;
  font-family: 'Sucrose Bold Two';
  background: url(../../assets/gorhf.png) center 0  no-repeat;
  background-size: cover;
  /* padding-top:450px; */
  height: 100vh;
  opacity: 0.2;
  animation-duration: 5s;
  animation-name: slidein5;
  animation-fill-mode: forwards;
}
@keyframes slidein5 {
  from {
    margin-top: -200%;
    margin-left: -400%;
    height: 1000%;
    width: 1000%
  }

  to {
    margin-top: 0%;
    margin-left: 0%;
    height: 100%;
    width: 100%;
  }
}

#group {
  width: 90vw;
  text-align: center;
  display: flex;
  justify-content:space-between;
}


h1 {
  animation-duration: 4s;
  animation-name: slidein;
  /* animation-name: slidein2; */
}
@keyframes slidein {
  from {
    margin-top: 100%;
    width: 500%
  }

  to {
    margin-top: 0%;
    width: 100%;
  }
}
@keyframes slidein2 {
  from {
    margin-top: -20%;
    width: 100%;
  }
  to {
    margin-top: 0%;
    width: 100%;
  }
}
/* #jagan {
  word-spacing: 2em;
} */
/* header::after {
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: "";
  position: absolute;
  z-index: -1;
  
} */
.hover-btn:hover {
  z-index: 999;
  color: #eddc5a;
}
.cursor {
  cursor: pointer;
}
/* .box:hover {
    transform: rotate(3600deg);
    -webkit-transform: rotate(270deg);
    width: 50px;
    height: 50px;
    background-color: blue;
    color: yellow;
    font-size: 18px;
    left: 500px;
    top: 250px;
    position: absolute;
    -webkit-transition-property: width height background-color font-size left top transform -webkit-transform color;
    -webkit-transition-duration: 1s;
    -webkit-transition-timing-function: ease-in-out;
    transition-property: width height background-color font-size left top transform -webkit-transform color;
    transition-duration: 1s;
    transition-timing-function: ease-in-out;
} */
/* .box {
    width: 100px;
    height: 100px;
    background-color: red;
    font-size: 20px;
    left: 800px;
    top: 600px;
    position: absolute; */
    /* -webkit-transition-property: width height background-color font-size left top transform -webkit-transform color;
    -webkit-transition-duration: 4s;
    -webkit-transition-timing-function: ease-in-out; */
    /* transition-property: width height background-color font-size left top transform -webkit-transform color;
    transition-duration: 1s;
    transition-timing-function: ease-in-out;
} */
</style>