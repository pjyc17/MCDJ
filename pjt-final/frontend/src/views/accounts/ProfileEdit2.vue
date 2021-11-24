<template>
  <div class="home">
    <!-- <img alt="MCDJ logo" src="../../public/favicon/android-chrome-384x384.png"> -->

    
    <!-- <div v-if="$store.state.user.id === 0 || ($store.state.user.birthday.year === $store.state.today.year && $store.state.user.birthday.month === $store.state.today.month && $store.state.user.birthday.date === $store.state.today.date)"> -->
      <div>
        <b-form-select v-model="y_selected" :options="y_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="m_selected" :options="m_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="d_selected" :options="d_options" multiple :select-size="1"></b-form-select>
        <button @click="getBirthday">입력</button>
      </div>
      <div>
        <div class="mt-3"> 
          <strong v-if="y_selected">{{ y_selected[0] }}년 </strong> 
          <strong v-if="m_selected">{{ m_selected[0] }}월 </strong> 
          <strong v-if="d_selected">{{ d_selected[0] }}일 </strong>
          <br>
          <!-- <strong v-if="y_selected">{{ 2022 - y_selected[0] }}</strong> -->
        </div>
      </div>
    </div>
  <!-- </div> -->
  
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  components: {
  },
  data() {
    const y_options = []
    const m_options = []
    const d_options = []
    for (let y_index = 1938; y_index < 2022; y_index++) {
      y_options.push({value: y_index, text: y_index})
    }
    for (let m_index = 1; m_index < 13; m_index++) {
      m_options.push({value: m_index, text: m_index})
    }
    for (let d_index = 1; d_index < 32; d_index++) {
      d_options.push({value: d_index, text: d_index})
    }
    return {
      y_selected: [this.$store.state.today.year], // Array reference
      m_selected: [this.$store.state.today.month], // Array reference
      d_selected: [this.$store.state.today.date], // Array reference
      y_options,
      m_options,
      d_options
    }
  },
  methods: {
    notFound: function() {
      this.$router.push({name: 'NotFound'})
    },
    setToken: function() {
      return {Authorization: `JWT ${localStorage.getItem('MCDJ_jwt')}`}
    },
    getBirthday: function () {
      const birthday = {
        year: this.y_selected[0],
        month: this.m_selected[0],
        date: this.d_selected[0],
      }
      if (this.$store.state.user.id !== 0) {
        axios({
          headers: this.setToken(),
          method: 'put',
          url: `${this.$store.state.domain}/accounts/birthday/`,
          data: {birthday: `${birthday.year}-${birthday.month}-${birthday.date}`},
        })
          .catch(() => this.notFound())
      }
      this.$store.commit('GET_BIRTHDAY', birthday)
      this.$router.push({name: 'ChronologyYear', params: {year: birthday.year}})
    },
  }
}

</script>
<style scoped>

</style>