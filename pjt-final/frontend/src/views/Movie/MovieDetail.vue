<template>
  <div>
    <div class="row">
      <div class="col-12 col-md-6">
        <div class="video-container">
          <iframe :src="`https://www.youtube.com/embed/${movie.movies.youtube_key}?autoplay=1&mute=1`" frameborder="0"></iframe>
          <div class="title">
            <img src="@/assets/MCDJ.png" alt="" height="32px"><strong>{{movie.movies.title}}</strong>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-6">
        {{movie.genres}}
        {{movie.actors}}
        {{movie.movies.overview}}
      </div>
    </div>
    {{movie}}
    <!-- {{similarMovies}} -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieDetail',
  data: function() {
    return {
      movie: null,
      similarMovies: [],
    }
  },
  created() {
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
          .then((res) => this.similarMovies = res.data.results)
      })
      .catch(() => this.$router.push({name: 'NotFound'}))
  }
}
</script>

<style scoped>
.title {
  position: absolute;
  top: 0%;
  left: 50%;
  transform: translate(-50%, -0%);
}
.video-container {
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
</style>