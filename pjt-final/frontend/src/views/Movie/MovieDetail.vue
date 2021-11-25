<template>
  <div class="detail-box">
    <div v-if="movie" class="row">
      <div class="col-12 col-md-8 float-left">
        <div class="video-container">
          <iframe :src="`https://www.youtube.com/embed/${movie.youtube_key}?autoplay=1&mute=1`" frameborder="0"></iframe>
          <div class="title">
            <img src="@/assets/MCDJ.png" alt="" height="32px"><strong>{{movie.title}}</strong>
          </div>
        </div>
        <div class="genre-actor-cart-box">
          <i v-if="$store.state.user.id" :class="{'selected-cart-btn': isCart}" @click="putInCart" class="fas fa-shopping-cart cart-btn inline-block"></i>
          <div>
            <div class="flex tomato-box">
              장르: 
              <span v-for="(genre, idx) in movie.genres" :key="idx">
                <span @click="genreMovies(genre.id)" class="cursor">{{genre.name}}</span>
                <span v-if="idx!==movie.genres.length - 1">, </span>
              </span>
            </div>
            <div class="flex dogerblue-box">
              출연진: 
              <span v-for="(actor, idx) in movie.actors" :key="idx">
                <span @click="actorMovies(actor.id)" class="cursor">{{actor.name}}</span>
                <span v-if="idx!==movie.actors.length - 1">, </span>
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-4">
        <div class="flex-right">
          <i @click="showChats" class="fas fa-comment-dots chat-btn inline-block"></i>
        </div>
        <div class="text-center">
          <div class="overview">{{movie.overview}}</div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="flex-center-wrap">
        <div v-for="movie in similarMovies" :key="movie.key" @click="goToMovieDetail(movie.id)" class="col-6 col-sm-4 col-md-3 col-xl-2 movie-card">
          <div class="card h-100">
            <div class="card-img-box">
              <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img" :alt="movie.title">
            </div>
            <div class="card-body">
              <p class="card-title reduce-content">{{movie.title}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div @mouseleave="notShown" class="chats col-11 col-sm-7 col-md-6 col-lg-5 col-xl-4" :class="{'hidden-chat': !isShown}">
      <div id="chat-box-content" class="chat-content">
        <div v-for="chat in chats" :key="chat.id">
          <div v-if="chat.user.id === $store.state.user.id" class="flex-right">
            <div class="inline-block">
              <div class="chat-box-content">
                {{chat.content}}<br>
                <star-rating :inline="true" :rating="chat.rating" :read-only="true" :star-size="10" :rounded-corners="true" :show-rating="false" />
              </div>
              <div class="fontsize-10">{{convertDate(chat.created)}} <div class="delete-chat" @click="deleteChat(chat)" v-if="chat.user.id === $store.state.user.id">X</div></div>
            </div>
            <div class="chat-box-user">{{chat.user.username}}</div>
          </div>
          <div v-else class="flex-left">
            <div class="chat-box-user">{{chat.user.username}}</div>
            <div class="inline-block">
              <div class="chat-box-content">
                {{chat.content}}<br>
                <star-rating :inline="true" :rating="chat.rating" :read-only="true" :star-size="10" :rounded-corners="true" :show-rating="false" />
              </div>
              <div class="fontsize-10">{{convertDate(chat.created)}} <div class="delete-chat" @click="deleteChat(chat)" v-if="chat.user.id === $store.state.user.id"><i class="fas fa-times"></i></div></div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="$store.state.user.id !== 0" class="chat-input">
        <star-rating :inline="true" v-model="rating" :star-size="20" :rounded-corners="true"></star-rating>
        <div class="flex-align-ceter">
          <textarea v-model="chat" style="width:70%;" rows="2" />
          <button @click="writeChat">작성</button>
        </div>
      </div>
      <div v-else class="chat-input">
        <div class="flex-align-ceter">
          <textarea disabled style="width:70%;" rows="2">로그인 후 이용해주세요.</textarea>
          <button class="disabled-cursor">작성</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieDetail',
  components: {
    StarRating
  },
  data: function() {
    return {
      movie: null,
      similarMovies: [],
      chats: [],
      isShown: false,
      rating: 3,
      chat: '',
      isCart: false,
    }
  },
  methods: {
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    getMovie: function() {
      if (this.$store.state.user.id === 0) {
        axios({
          method: 'post',
          url: `${this.$store.state.domain}/movies/log/${this.$route.params.movieId}/`
        })
      } else {
        axios({
          headers: this.setToken(),
          method: 'post',
          url: `${this.$store.state.domain}/movies/log/${this.$route.params.movieId}/`
        })
          .then(res => this.isCart = res.data.isCart)
      }
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/${this.$route.params.movieId}/`,
      })
        .then(res => {this.movie = res.data; this.chats.push(...this.movie.chats)})
        .then(() => {
          axios({
            method: 'get',
            url: `${this.$store.state.TMDB_URL}/movie/${this.$route.params.movieId}/similar`,
            params: {
              api_key: this.$store.state.TMDB_KEY,
              language: 'ko-KR'
            },
          })
            .then((res) => {
              this.similarMovies = []
              for (let similarMovie of res.data.results) {
                if (this.$store.state.allMovies.some(movie => movie.id === similarMovie.id && movie.id !== this.movie.id)) {
                  this.similarMovies.push(similarMovie)
                }
                if (this.similarMovies.length === 10) {
                  break
                }
              }
              // this.similarMovies = res.data.results.slice(0, 5)
            })
        })
        .catch(() => window.location.href = '/404')
    },
    genreMovies: function(genre_id) {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/genre/${genre_id}/`,
      })
        .then((res) => {
          this.similarMovies = []
          for (let similarMovie of res.data) {
            if (similarMovie.id !== this.movie.id) {
              this.similarMovies.push(similarMovie)
            }
            if (this.similarMovies.length === 10) {
              break
            }
          }
          // this.similarMovies = res.data.slice(0, 5)
        })
    },
    actorMovies: function(actor_id) {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/actor/${actor_id}/`,
      })
        .then((res) => {
          this.similarMovies = []
          for (let similarMovie of res.data) {
            if (similarMovie.id !== this.movie.id) {
              this.similarMovies.push(similarMovie)
            }
            if (this.similarMovies.length === 10) {
              break
            }
          }
          // this.similarMovies = res.data.slice(0, 5)
        })
    },
    goToMovieDetail: function(movieId) {
      this.$router.push({name: 'MovieDetail', params: {movieId: movieId}})
      this.getMovie()
    },
    putInCart: function() {
      axios({
        headers: this.setToken(),
        method: 'put',
        url: `${this.$store.state.domain}/movies/cart/${this.$route.params.movieId}/`,
      })
        .then(res => this.isCart = res.data.isCart)
    },
    showChats: function() {this.isShown = !this.isShown},
    notShown: function() {this.isShown = false},
    writeChat: function() {
      const chat = this.chat.trim()
      if (chat) {
        axios({
          headers: this.setToken(),
          method: 'post',
          url: `${this.$store.state.domain}/movies/${this.$route.params.movieId}/chat/`,
          data: {
            content: chat,
            rating: this.rating,
          },
        })
          .then((res) => this.chats.push(res.data))
      } else {alert("빈칸이 있어요!")}
      this.chat = ''
    },
    deleteChat: function(deletedChat) {
      if (deletedChat.user.id === this.$store.state.user.id) {
        axios({
          headers: this.setToken(),
          method: 'delete',
          url: `${this.$store.state.domain}/movies/delete/${deletedChat.id}/`,
        })
          .then(() => {
            this.chats.splice(this.chats.indexOf(deletedChat), 1)
          })
          .catch(() => this.$router.push({name: 'NotFound'}))
      }
    },
    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },
    eventFunction: function() {
      if (window.innerWidth < 768) {document.querySelector("#app > div.detail-box > div:nth-child(1) > div.col-12.col-md-4 > div.flex-right > i").setAttribute('style', 'position: fixed; top: 60px; right: 0; z-index:1000')}
      else {document.querySelector("#app > div.detail-box > div:nth-child(1) > div.col-12.col-md-4 > div.flex-right > i").removeAttribute('style', 'position: fixed; top: 60px; right: 0; z-index:1000')}
    },
  },
  created() {
    window.scrollTo(0, 0)
    this.getMovie()
    window.addEventListener('resize', this.eventFunction)
  },
  destroyed() {
    window.scrollTo(0, 0)
    window.removeEventListener('resize', this.eventFunction)
  },
  updated() {
    window.document.getElementById('chat-box-content').scrollTop = window.document.getElementById('chat-box-content').scrollHeight;
  }
}
</script>

<style scoped>
.detail-box {
  margin: 0 3rem;
}
.title {
  position: absolute;
  top: 0%;
  left: 50%;
  transform: translate(-50%, -0%);
}
.video-container {
  float: inline-start;
  position: relative;
  padding-top: 56.25%;
  height: 0;
}
.video-container iframe{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.tomato-box {
  border-style: solid; 
  border-width: 0 0 0 8px; 
  padding: 0; 
  word-break: break-all;
  border-color: Tomato; 
  background-color:rgba(255, 99, 71, 0.2);
}
.dogerblue-box {
  border-style: solid; 
  border-width: 0 0 0 8px; 
  padding: 0; 
  word-break: break-all;
  border-color: DodgerBlue; 
  background-color:rgba(30, 144, 255, 0.2);
}
.overview {
  height: calc(100vw / 3);
  overflow: auto;
  text-overflow:ellipsis;
  /* display: -webkit-box; */
  /* -webkit-line-clamp: 10;
  -webkit-box-orient: vertical; */
  border-radius: 0px;
  border-style: solid; 
  border-width: 2px; 
  padding: 12px; 
  word-break: break-all;
  border-color: LightGray; 
  background-color:#141414;
  opacity: 50%;
}
.overview:hover {
  background-color: black;
  border-color: white;
  opacity: 100%;
}
.genre-actor-cart-box {
  position: relative;
}
.cart-btn {
  position: absolute;
  right: 0;
  top:25%;
  right: 0.5rem;
  /* transform: translate(-50%, -50%); */
  font-size: 1.5em;
  cursor: pointer;
  /* 좌우 대칭 */
  -moz-transform: scale(-1, 1);
  -webkit-transform: scale(-1, 1);
  -o-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.cart-btn:hover {
  color: #eddc5a;
}
.selected-cart-btn {
  color: #eddc5a;
}
.chat-btn {
  font-size: 2em;
  cursor: pointer;
  /* 좌우 대칭 */
  -moz-transform: scale(-1, 1);
  -webkit-transform: scale(-1, 1);
  -o-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.chat-btn:hover {
  color: #eddc5a;
}
.reduce-content {
  overflow: hidden;
  /* text-overflow:ellipsis; */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: 1.5em;
  color: #949597;
  -webkit-text-stroke: 0.5px #eddc5a;
  margin-bottom: 0;
}
.movie-card {
  margin: 1rem;
  padding: 0;
  /* background-color: transparent;
  cursor: pointer;
  width: 10rem;
  margin: 1rem 0.5rem; */
}
.chats {
  position: fixed;
  background-color: royalblue;
  /* margin: 3rem; */
  top: 9rem;
  right: 1rem;
  height: 60%;
  /* width: calc((100% - 6rem) / 3); */
  transform: translate(-0%, -0%);
  border-radius: 1rem;
  /* border-bottom-left-radius: 16px;
  border-bottom-right-radius: 16px; */
  border-style: solid; 
  border-width: 2px; 
  border-color: #141414; 
}
.hidden-chat {
  visibility: hidden;
}
.chat-content {
  overflow: auto;
  height: 80%;
}
.flex-right {
  display: flex;
  justify-content: right;
  align-items: center;
}
.flex-left {
  display: flex;
  justify-content: left;
  align-items: center;
}
.chat-box-user {
  display: inline-block;
  overflow: hidden;
  text-overflow:ellipsis;
  border-radius: 16px;
  border-style: solid; 
  border-width: 2px; 
  word-break: break-all;
  border-color: LightGray; 
  background-color:#141414;
}
.chat-box-content {
  text-align: left;
  color: black;
  display: inline-block;
  overflow: hidden;
  text-overflow:ellipsis;
  border-radius: 4px;
  border-style: solid; 
  border-width: 1px; 
  word-break: break-all;
  border-color: #141414;
  background-color: LightGray;
}
.delete-chat {
  font-size: 10px;
  color: #141414;
  display: inline-block;
  cursor: pointer;
  padding: 0 3px;
  border-radius: 2px;
  border-style: solid; 
  border-width: 1px; 
  border-color: #141414;
}
.chat-input-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-items: stretch;
  align-items: center;
}
.chat-input {
  height: 20%;
}
.flex-align-ceter {
  display: flex;
  justify-content: center;
  align-items: stretch;
}
</style>