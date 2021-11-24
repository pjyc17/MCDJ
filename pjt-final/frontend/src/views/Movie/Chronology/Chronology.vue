<template>
  <div class="container">
    <div class="text-center" v-if="isLoading">
      <br><br><br><br>
      <label for="spinner"><img src="@/assets/dog.gif" alt="두리번.. 두리번.."></label>
      <div>
        <b-spinner id="spinner" style="color: grey;">     
        </b-spinner>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      </div>
    </div>
    <br>
    <div @click="goToChronologyYear" class="btn btn-lg btn-success">{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}슬라이드 보기{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</div>
    <div class="flex">
      <each-year 
        v-for="(eachYear, idx) in years" :key="idx"
        :eachYear="eachYear"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import EachYear from '@/views/Movie/Chronology/EachYear.vue'

export default {
  name: 'Chronology',
  components: {
    EachYear
  },
  data: function() {
    return {
      isLoading: true,
      years: [],
    }
  },
  methods: {
    goToChronologyYear: function() {
      this.$router.push({name: 'ChronologyYear', params: {year: this.$store.state.user.birthday.year}})
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.domain}/movies/annually_poster/`,
    })
      .then(res => {
        while (res.data.chronology_poster.length) {
          this.years.push(...res.data.chronology_poster.splice(res.data.chronology_poster.length - 1, 1))
        }
      })
  },
  updated() {
    if (this.years.length) {
      this.isLoading = false
    }
  },
}
</script>

<style>
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
</style>