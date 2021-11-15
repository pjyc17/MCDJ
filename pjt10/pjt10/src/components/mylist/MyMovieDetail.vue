<template>
  <div>
    <div v-if="youtubeVideoURL" class="video-container">
      <iframe :src="youtubeVideoURL" frameborder="0"></iframe>
    </div>
    <!-- <div class="float-start w-50">
      <img :src="`https://image.tmdb.org/t/p/w500/${myMovie.poster_path}`" class="w-100" :alt="myMovie.title">
    </div> -->
    <h5 class="py-3"><strong>{{myMovie.title}}</strong></h5>
    <p v-if="myMovie.overview" class="overview">{{myMovie.overview}}</p>
  </div>
</template>

<script>
import {mapState,} from 'vuex'
import axios from 'axios'
const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
const TMDB_URL = 'https://api.themoviedb.org/3'


export default {
  name: 'MyMovieDetail',
  data: function() {
    return {
      youtubeVideoURL: null,
    }
  },
  computed: {
    ...mapState(['myMovie',]),
  },
  updated() {
    const movieId = this.$store.state.myMovie.id
    axios({
      methods: 'get',
      url: `${TMDB_URL}/movie/${movieId}/videos?api_key=${TMDB_API}`,
    })
    .then(res => res.data.results[0])
    .then(youtubeVideo => {
      this.youtubeVideoURL = `https://www.youtube.com/embed/${youtubeVideo.key}?autoplay=1&mute=1`
    })
    .catch(() => this.youtubeVideoURL=null)
  }
}
</script>

<style scoped>
.box {
  display: inline-block;
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