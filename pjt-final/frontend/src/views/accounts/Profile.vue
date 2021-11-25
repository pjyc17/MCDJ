<template>
  <div id="app">
    <div id="gost-bg"></div>
    <header>
      <div id="word" v-if="is_birthday">
        <h1 >{{ person.username }}'s Profile</h1>
        <h3>age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}</h3>
        <router-link :to="{name: 'ProfileEdit2', params: {userId: $store.state.user.id}}">Edit Birthday</router-link>

        <h3 v-if="(person.birthday.birthday.substring(5,7) == 1 && person.birthday.birthday.substring(8,10) >= 20) || (person.birthday.birthday.substring(5,7) == 2 && person.birthday.birthday.substring(8,10) <= 18) "><img height="40" src="@/assets/별자리/물병자리.png" alt="">star : Aquarius </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 2 && person.birthday.birthday.substring(8,10) >= 19) || (person.birthday.birthday.substring(5,7) == 3 && person.birthday.birthday.substring(8,10) <= 20)"><img height="40" src="@/assets/별자리/물고기자리.png" alt="">star : Prisces </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 3 && person.birthday.birthday.substring(8,10) >= 21) || (person.birthday.birthday.substring(5,7) == 4 && person.birthday.birthday.substring(8,10) <= 19)"><img height="40" src="@/assets/별자리/양자리.png" alt=""> star : Aries </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 4 && person.birthday.birthday.substring(8,10) >= 20) || (person.birthday.birthday.substring(5,7) == 5 && person.birthday.birthday.substring(8,10) <= 20)"><img height="40" src="@/assets/별자리/황소자리.png" alt="">star : Taurus </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 5 && person.birthday.birthday.substring(8,10) >= 21) || (person.birthday.birthday.substring(5,7) == 6 && person.birthday.birthday.substring(8,10) <= 21)"><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt="">star : Gemini </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 6 && person.birthday.birthday.substring(8,10) >= 22) || (person.birthday.birthday.substring(5,7) == 7 && person.birthday.birthday.substring(8,10) <= 22)"><img height="40" src="@/assets/별자리/게자리.png" alt="">star : Cancer </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 7 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 8 && person.birthday.birthday.substring(8,10) <= 22)"><img height="40" src="@/assets/별자리/사자자리.png" alt="">star : Leo </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 8 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 9 && person.birthday.birthday.substring(8,10) <= 23)"><img height="40" src="@/assets/별자리/처녀자리.png" alt="">star : Virgo </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 9 && person.birthday.birthday.substring(8,10) >= 24) || (person.birthday.birthday.substring(5,7) == 10 && person.birthday.birthday.substring(8,10) <= 22)"><img height="40" src="@/assets/별자리/천칭자리.png" alt="">star : Libra </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 10 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 11 && person.birthday.birthday.substring(8,10) <= 22)"><img height="40" src="@/assets/별자리/전갈자리.png" alt="">star : Scorpio </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 11 && person.birthday.birthday.substring(8,10) >= 23) || (person.birthday.birthday.substring(5,7) == 12 && person.birthday.birthday.substring(8,10) <= 21)"><img height="40" src="@/assets/별자리/사수자리.png" alt="">star : Sagittarius </h3>
        <h3 v-if="(person.birthday.birthday.substring(5,7) == 12 && person.birthday.birthday.substring(8,10) >= 22) || (person.birthday.birthday.substring(5,7) == 1 && person.birthday.birthday.substring(8,10) <= 19)"><img height="40" src="@/assets/별자리/염소자리.png" alt="">star : Capricorn </h3>
        <div class="flex-center">
          <!-- <profile-edit :birthday="user.birthday" /> -->

        </div>
        <!--   <h3>followings : {{  }} / followers : {{  }}</h3> -->
        <br>
        <div id="group">
          <div class="container">
            <h3>genre : </h3>
            <div v-for="genre in genres" :key="genre.id">
              <h5 @click="goToGenre(genre.id)" class="inline-block cursor">{{ genre.name }}</h5>
              <p> 연관성 : {{ (genre.point / gpoint * 100).toFixed(1) }}% </p>
            </div>
          </div>
        <!-- <div class="box">sd</div> -->
          <div class="container">
            <h3>want : {{ }} </h3>
            <div v-for="movie in carts" :key="movie.id">
              <strong @click="goToMovie(movie.id)" class="inline-block cursor">{{ movie.title }}</strong>
            </div>
          </div>
          <div class="container">
            <h3>likes  : </h3>
            <div v-for="like_review in like_reviews" :key=like_review.id>
              <strong @click="goToReview(like_review.id)" class="cursor">{{ like_review.title }} <i class="fas fa-thumbs-up"></i> {{ like_review.likes_cnt }}</strong>
            </div>
          </div>
          <!-- <div class="container" style="word-break:break-all;word-wrap:break-word;"> -->
          <div class="container">
            <h3>written : </h3>
            <div v-for="review in reviews" :key="review.id">
              <strong @click="goToReview(review.id)" class="inline-block cursor">{{ review.title }}</strong>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <img src="@/assets/dogyawn.gif" @click="goToHome" class="cursor" alt="">
        <h1 @click="goToHome" class="cursor">
          생년월일 입력해줭
        </h1>
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
    return {
      is_birthday: false,
      person: null,
      genres: [],
      carts: [],
      like_reviews: [],
      reviews: [],
    }
  },
  methods: {
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
            console.log(birth.month)
            this.is_birthday = true
            axios({
              method: 'get',
              url: `${this.$store.state.domain}/movies/recommend/genres/${birth}/${this.$route.params.userId}/`
            })
              .then(res => this.genres = res.data.genres.splice(0,3))
              .then(res => console.log(res.data))
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
      console.log(genreId)
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
    }
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
.btw {
  display: flex;
  justify-content: space-between;
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
  display: flex;
  justify-content: space-evenly;

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