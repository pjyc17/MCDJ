<template>
  <div>
    <!-- <carousel class="width-100" :value="10" :perPageCustom="[[320, 2], [480, 3], [640, 4], [800, 5], [960, 6], [1120, 7]]" > -->
    <carousel id="carousel" class="width-100" :value="10" :perPage="1">
      <slide v-for="idx of idxes" :key="idx" class="slide_item item" aria-hidden="true">
        <div class="movie-card">
          <div class="card h-100">
            <div class="card-img-box">
              <img :src="`https://image.tmdb.org/t/p/w500/${years[idx].poster_path}`" class="card-img" :alt="years[idx].year">
            </div>
            <div class="year-box">
              <p class="year"><strong>{{years[idx].year}}</strong></p>
            </div>
          </div>
        </div>
        <div v-if="idx + 1 < years.length" class="movie-card">
          <div class="card h-100">
            <div class="card-img-box">
              <img :src="`https://image.tmdb.org/t/p/w500/${years[idx + 1].poster_path}`" class="card-img" :alt="years[idx + 1].year">
            </div>
            <div class="year-box">
              <p class="year"><strong>{{years[idx + 1].year}}</strong></p>
            </div>
          </div>
        </div>
      </slide>
    </carousel>
  </div>
</template>

<script>
import axios from 'axios'
import {Carousel, Slide} from 'vue-carousel'


export default {
  name: 'ChronologyYear',
  components: {
    Carousel,
    Slide,
  },
  data: function() {
    return {
      years: [],
      index: 3,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/annually_poster/`,
    })
      .then(res => this.years = res.data.chronology_poster)
  },
  computed: {
    idxes: function() {
      const idxes = []
      let j = 0
      for (let i = 0; i < this.years.length; i+=2) {
        idxes.push(j)
        j+=2
      }
      return idxes
    },
    fuck: function() {
      return document.querySelector("#carousel > div.VueCarousel-wrapper")
    },
    changeFuck: function() {
      // this.fuck.style="padding: 0 100vw 0 0;"
      this.fuck.setAttribute("style", "padding: 0 100vw 0 0;")
      return this.fuck
    }
  },
}
</script>

<style scoped>
#carousel .VueCarousel-wrapper {
  padding: 10rem !important;
}
/* style="padding: 0 100vw 0 0;" */
.width-100 {
  width: 10rem;
}
.item {
  flex: 1 1 40%;
  visibility:visible;
}
.movie-card {
  cursor: pointer;
  width: 10rem;
  margin: 1rem 0.5rem;
}
.year-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.year {
  font-size: 4em;
  -webkit-text-stroke: 1.5px black;
  margin-bottom: 0;
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