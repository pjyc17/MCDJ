<template>
  <div @mousemove="startCarousel">
    <br>
    <div @mouseover="startCarousel" @click="goToChronology" class="btn btn-lg btn-success">{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}펴서 보기{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</div>
    <!-- <carousel class="width-100" :value="10" :perPageCustom="[[320, 2], [480, 3], [640, 4], [800, 5], [960, 6], [1120, 7]]" > -->
    <carousel @mouseover="startCarousel" id="carousel" class="width-100" v-model="index" :perPage="1" :paginationSize="0" :loop="true">
      <slide v-for="idx of idxes" :key="idx" class="slide_item item" aria-hidden="true">
        <div @click="goToYear(years[idx].year)" class="movie-card">
          <div class="card h-100">
            <div class="card-img-box">
              <img :src="`https://image.tmdb.org/t/p/w500/${years[idx].poster_path}`" class="card-img" :alt="years[idx].year">
            </div>
            <div class="year-box">
              <p class="year"><strong>{{years[idx].year}}</strong></p>
            </div>
          </div>
        </div>
        <div @click="goToYear(years[idx + 1].year)" v-if="idx + 1 < years.length" class="movie-card">
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
    <div @mouseover="startCarousel" class="big-opac-box"></div>
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
      index: -1,
      keep: -1,
      flag: true,
      flag2: true,
      time: 0,
    }
  },
  methods: {
    startCarousel: function() {
      if (this.flag2) {
        this.index = this.keep
        this.flag2 = false
      }
      this.fuck.setAttribute("style", "padding: 0 100vw 0 0;")
    },
    goToYear: function(year) {
      this.$router.push({name: "Year", params: {year: year}})
    },
    mouseMove: function(m) {
      var X = m.clientX
      var Y = m.clientY
      if (this.index >= 0 && this.index <= this.years.length) {
        if (Y > 150 && Y < 650) {
          if (X > window.innerWidth * 0.66 && this.index < this.years.length) {this.time+=1} else {
            if (X < window.innerWidth * 0.33 && this.index > 0) {this.time-=1}
          }
        }
      }
      if (this.time > 30) {this.index+=1;this.time-=30} else {
        if (this.time < -30) {this.index-=1;this.time+=30}
      }
    },
    goToChronology: function() {
      this.$router.push({name: 'Chronology'})
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/annually_poster/`,
    })
      .then(res => {
        this.years = res.data.chronology_poster
      })
    window.addEventListener('mousemove', this.mouseMove)
  },
  destroyed() {
    window.removeEventListener('mousemove', this.mouseMove)
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
      return window.document.querySelector("#carousel > div.VueCarousel-wrapper")
    },
    // changeFuck: function() {
    //   // this.fuck.style="padding: 0 100vw 0 0;"
    //   this.fuck.setAttribute("style", "padding: 0 100vw 0 0;")
    //   return this.fuck
    // }
  },
  updated() {
    if (this.flag) {
      this.keep = parseInt(this.years.length / 2) - parseInt((this.years[this.years.length - 1].year - this.$route.params.year + 1) / 2)
      if (this.keep !== -1) {this.flag = false}
    }
    if (this.index === -1) {
      this.index = this.keep
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
.big-opac-box {
  position: fixed;
  width: 100%;
  height: 100%;
  opacity: 100;
}
</style>