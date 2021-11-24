<template>
  <div id="app"> 
    <!-- <div class="header1"></div> -->
      <!-- <img class="header-img" src="../../assets/gorhf.png" alt="">  -->
      <!-- <h3 v-if="(person.birthday.month == 1 && person.birthday.date >= 20) || (person.birthday.month == 2 && person.birthday.date <= 18) "><img height="40" src="@/assets/별자리/물병자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 2 && person.birthday.date >= 19) || (person.birthday.month == 3 && person.birthday.date <= 20)"><img height="40" src="@/assets/별자리/물고기자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 3 && person.birthday.date >= 21) || (person.birthday.month == 4 && person.birthday.date <= 19)"><img height="40" src="@/assets/별자리/양자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 4 && person.birthday.date >= 20) || (person.birthday.month == 5 && person.birthday.date <= 20)"><img height="40" src="@/assets/별자리/황소자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 5 && person.birthday.date >= 21) || (person.birthday.month == 6 && person.birthday.date <= 21)"><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 6 && person.birthday.date >= 22) || (person.birthday.month == 7 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/게자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 7 && person.birthday.date >= 23) || (person.birthday.month == 8 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/사자자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 8 && person.birthday.date >= 23) || (person.birthday.month == 9 && person.birthday.date <= 23)"><img height="40" src="@/assets/별자리/처녀자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 9 && person.birthday.date >= 24) || (person.birthday.month == 10 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/천칭자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 10 && person.birthday.date >= 23) || (person.birthday.month == 11 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/전갈자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 11 && person.birthday.date >= 23) || (person.birthday.month == 12 && person.birthday.date <= 21)"><img height="40" src="@/assets/별자리/사수자리.png" alt=""></h3>
      <h3 v-if="(person.birthday.month == 12 && person.birthday.date >= 22) || (person.birthday.month == 1 && person.birthday.date <= 19)"><img height="40" src="@/assets/별자리/염소자리.png" alt=""></h3> -->

    <header>
      <div id="word" v-if="person">
        <h1>{{ person.username }}'s Profile</h1>
        <!--  -->
        <h3>age : {{ $store.state.today.year + 1 - parseInt(person.birthday.birthday.substring(0,4)) }}</h3>
        
        <h3 v-if="(person.birthday.month == 1 && person.birthday.date >= 20) || (person.birthday.month == 2 && person.birthday.date <= 18) "><img height="40" src="@/assets/별자리/물병자리.png" alt="">star : Aquarius </h3>
        <h3 v-if="(person.birthday.month == 2 && person.birthday.date >= 19) || (person.birthday.month == 3 && person.birthday.date <= 20)"><img height="40" src="@/assets/별자리/물고기자리.png" alt="">star : Prisces </h3>
        <h3 v-if="(person.birthday.month == 3 && person.birthday.date >= 21) || (person.birthday.month == 4 && person.birthday.date <= 19)"><img height="40" src="@/assets/별자리/양자리.png" alt=""> star : Aries </h3>
        <h3 v-if="(person.birthday.month == 4 && person.birthday.date >= 20) || (person.birthday.month == 5 && person.birthday.date <= 20)"><img height="40" src="@/assets/별자리/황소자리.png" alt="">star : Taurus </h3>
        <h3 v-if="(person.birthday.month == 5 && person.birthday.date >= 21) || (person.birthday.month == 6 && person.birthday.date <= 21)"><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt="">star : Gemini </h3>
        <h3 v-if="(person.birthday.month == 6 && person.birthday.date >= 22) || (person.birthday.month == 7 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/게자리.png" alt="">star : Cancer </h3>
        <h3 v-if="(person.birthday.month == 7 && person.birthday.date >= 23) || (person.birthday.month == 8 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/사자자리.png" alt="">star : Leo </h3>
        <h3 v-if="(person.birthday.month == 8 && person.birthday.date >= 23) || (person.birthday.month == 9 && person.birthday.date <= 23)"><img height="40" src="@/assets/별자리/처녀자리.png" alt="">star : Virgo </h3>
        <h3 v-if="(person.birthday.month == 9 && person.birthday.date >= 24) || (person.birthday.month == 10 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/천칭자리.png" alt="">star : Libra </h3>
        <h3 v-if="(person.birthday.month == 10 && person.birthday.date >= 23) || (person.birthday.month == 11 && person.birthday.date <= 22)"><img height="40" src="@/assets/별자리/전갈자리.png" alt="">star : Scorpio </h3>
        <h3 v-if="(person.birthday.month == 11 && person.birthday.date >= 23) || (person.birthday.month == 12 && person.birthday.date <= 21)"><img height="40" src="@/assets/별자리/사수자리.png" alt="">star : Sagittarius </h3>
        <h3 v-if="(person.birthday.month == 12 && person.birthday.date >= 22) || (person.birthday.month == 1 && person.birthday.date <= 19)"><img height="40" src="@/assets/별자리/염소자리.png" alt="">star : Capricorn </h3>
        <div class="flex-center">
          <!-- <profile-edit :birthday="user.birthday" /> -->
          <!-- <profile-edit /> -->
        </div>
        <!--   <h3>followings : {{  }} / followers : {{  }}</h3> -->
        <br>
        <div id="group">
          <div class="container">
            <h3>genre : {{ /*위의 본 영화 선택한 정보들 db에 저장 후 개인의 전체 비율을 고려해 %로 나타내기*/ }}</h3>
              <div v-for="genre in genres" :key="genre.id">
                <p @click="goToGenre(genre.id)" class="inline-block cursor">{{ genre.name }}</p>
              </div>
          </div>
          <div class="container">
            <h3>want : {{ /*본 영화를 체크한 것 db저장 후 제목 출력*/ }}</h3>
            <a href="">what have you seen??</a>
          </div>
          <div class="container">
            <h3>likes  : {{  }}</h3>
          </div>
          <div class="container" style="word-break:break-all;word-wrap:break-word;">
            <h3>written review : </h3>
            <p class="inline-block" v-for="review in reviews" :key="review.id"><a href="http://localhost:8080/community/">{{ review.title }},</a>&nbsp;&nbsp;&nbsp;&nbsp;</p>
          </div>
        </div>
      </div>
      <!-- <img height="30" v-if="(person.birthday.month == 3 && person.birthday.date >= 21) || (person.birthday.month == 4 && person.birthday.date <= 19)" src="@/assets/양자리.png" alt=""> -->
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
        .then(res => this.person = res.data)
        .then(() => {
          const birth = this.person.birthday.birthday.substring(5,7) + this.person.birthday.birthday.substring(8,10)
          axios({
            method: 'get',
            url: `${this.$store.state.domain}/movies/recommend/genres/${birth}/${this.$route.params.userId}/`
          })
            .then(res => this.genres = res.data.genres.splice(0,3))
        })
      // axios({
      //   method: 'get',
      //   url: `${this.$store.state.domain}/movies/recommend/genres//`
      // })
      //   .then(res => this.reviews = res.data.splice(0,3))
    },
    goToGenre: function(genreId) {
      console.log(genreId)
      this.$router.push({name: 'GenreMovies', params: {genreId: genreId}})
    }
  },
  computed: {
  },
  created() {
    this.getProfile()
  },
}
</script>

<style scoped>
.header-img {
  position: relative;
  height: 100vh;
  width: 100vw;
  /* z-index: -1; */
  /* opacity:0.3; */
}
#word{
  /* width: 100%; */
  /* height: 100%; */
  /* text-align: center; */

  position: relative;
  font-family: 'Sucrose Bold Two';
  background: url(../../assets/gorhf.png) no-repeat;
  background-size: cover;
  padding-top:20.93333333%;
  
  opacity: 0.3;
  /* z-index: -999; */
}
/* #word {
  opacity: 1;
} */
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
</style>