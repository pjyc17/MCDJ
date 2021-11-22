<template>
  <div>
    <!-- <h1>Chronology</h1> -->
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
      years: [],
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
  }
}
</script>

<style>
.flex {
  display: flex;
  flex-wrap: wrap;
}
</style>