<template>
  <div class="detail-box">
    <div v-if="movie" class="row">
      <div class="col-12 col-md-8 float-left">
        <div class="video-container">
          <iframe :src="`https://www.youtube.com/embed/${movie.movies.youtube_key}?autoplay=1&mute=1`" frameborder="0"></iframe>
          <div class="title">
            <img src="@/assets/MCDJ.png" alt="" height="32px"><strong>{{movie.movies.title}}</strong>
          </div>
        </div>
        <div class="flex tomato-box">
          장르: 
          <span v-for="(genre, idx) in movie.genres" :key="idx">
            <span @click="genreMovies(genre.id)" class="click">{{genre.name}}</span>
            <span v-if="idx!==movie.genres.length - 1">, </span>
          </span>
        </div>
        <div class="flex dogerblue-box">
          출연진: 
          <span v-for="(actor, idx) in movie.actors" :key="idx">
            <span @click="actorMovies(actor.id)" class="click">{{actor.name}}</span>
            <span v-if="idx!==movie.actors.length - 1">, </span>
          </span>
        </div>
        <div>
          <star-rating v-model="rating" :star-size="20" :rounded-corners="true"></star-rating>
        </div>
      </div>
      <div class="col-12 col-md-4 text-box">
        <div>
          <i class="fas fa-comment-dots chat-btn right"></i>
        </div>
        <div>
          <p class="overview">{{movie.movies.overview}}</p>
        </div>
      </div>
    </div>
    <div class="row">
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
      rating: 0
    }
  },
  methods: {
    getMovie: function() {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/${this.$route.params.movieId}/`,
      })
        .then(res => this.movie = res.data)
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
                if (this.$store.state.allMovies.some(movie => movie.id === similarMovie.id)) {
                  this.similarMovies.push(similarMovie)
                }
                if (this.similarMovies.length === 6) {
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
        .then((res) => this.similarMovies = res.data.slice(0, 5))
    },
    actorMovies: function(actor_id) {
      axios({
        method: 'get',
        url: `${this.$store.state.domain}/movies/actor/${actor_id}/`,
      })
        .then((res) => this.similarMovies = res.data.slice(0, 5))
    },
    goToMovieDetail: function(movieId) {
      this.$router.push({name: 'MovieDetail', params: {movieId: movieId}})
      this.getMovie()
    }
  },
  created() {
    this.getMovie()
  },
}
</script>

<style scoped>
.float-left {
  float: left;
}
.detail-box {
  margin: 0 3rem;
}
.title {
  position: absolute;
  top: 0%;
  left: 50%;
  transform: translate(-50%, -0%);
}
.item {
  display: inline-block;
}
.right {
  display: block;
  margin-left: auto;
  margin-right: 0;
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
.text-box {
  text-align: left;
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
  overflow: hidden;
  text-overflow:ellipsis;
  /* display: -webkit-box;
  -webkit-line-clamp: 10;
  -webkit-box-orient: vertical; */
  border-radius: 4px;
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
}
.click {
  cursor: pointer;
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
  margin: 1rem 0;
}
.card-img-box {
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
</style>