<template>
  <div class="home">
    <div class="ball">
      <img alt="MCDJ logo" src="../../../public/favicon/android-chrome-384x384.png">
    </div>
    <span>C</span><span>S</span><span>S</span><span>&nbsp;</span><span>S</span><span>m</span><span>o</span><span>k</span><span>y</span><span>&nbsp;</span><span>T</span><span>e</span><span>x</span><span>t</span><span>&nbsp;</span><span>E</span><span>f</span><span>f</span><span>e</span><span>c</span><span>t</span>

    <!-- <div v-if="$store.state.user.id === 0 || ($store.state.user.birthday.year === $store.state.today.year && $store.state.user.birthday.month === $store.state.today.month && $store.state.user.birthday.date === $store.state.today.date)"> -->
      <div>
        <b-form-select v-model="y_selected" :options="y_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="m_selected" :options="m_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="d_selected" :options="d_options" multiple :select-size="1"></b-form-select>
        <button class="btn-3d green" @click="getBirthday">입력</button>
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

span {
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 3s both;
          animation: smoky 5s 3s both;
}

span:nth-child(even) {
  -webkit-animation-name: smoky-mirror;
          animation-name: smoky-mirror;
}

@-webkit-keyframes smoky {
  60% {
    text-shadow: 0 0 40px whitesmoke;
  }
  to {
    transform: translate3d(15rem, -8rem, 0) rotate(-40deg) skewX(70deg) scale(1.5);
    text-shadow: 0 0 20px whitesmoke;
    opacity: 0;
  }
}

@keyframes smoky {
  60% {
    text-shadow: 0 0 40px whitesmoke;
  }
  to {
    transform: translate3d(15rem, -8rem, 0) rotate(-40deg) skewX(70deg) scale(1.5);
    text-shadow: 0 0 20px whitesmoke;
    opacity: 0;
  }
}
@-webkit-keyframes smoky-mirror {
  60% {
    text-shadow: 0 0 40px whitesmoke;
  }
  to {
    transform: translate3d(18rem, -8rem, 0) rotate(-40deg) skewX(-70deg) scale(2);
    text-shadow: 0 0 20px whitesmoke;
    opacity: 0;
  }
}
@keyframes smoky-mirror {
  60% {
    text-shadow: 0 0 40px whitesmoke;
  }
  to {
    transform: translate3d(18rem, -8rem, 0) rotate(-40deg) skewX(-70deg) scale(2);
    text-shadow: 0 0 20px whitesmoke;
    opacity: 0;
  }
}
span:nth-of-type(1) {
  -webkit-animation-delay: 3.1s;
          animation-delay: 3.1s;
}

span:nth-of-type(2) {
  -webkit-animation-delay: 3.2s;
          animation-delay: 3.2s;
}

span:nth-of-type(3) {
  -webkit-animation-delay: 3.3s;
          animation-delay: 3.3s;
}

span:nth-of-type(4) {
  -webkit-animation-delay: 3.4s;
          animation-delay: 3.4s;
}

span:nth-of-type(5) {
  -webkit-animation-delay: 3.5s;
          animation-delay: 3.5s;
}

span:nth-of-type(6) {
  -webkit-animation-delay: 3.6s;
          animation-delay: 3.6s;
}

span:nth-of-type(7) {
  -webkit-animation-delay: 3.7s;
          animation-delay: 3.7s;
}

span:nth-of-type(8) {
  -webkit-animation-delay: 3.8s;
          animation-delay: 3.8s;
}

span:nth-of-type(9) {
  -webkit-animation-delay: 3.9s;
          animation-delay: 3.9s;
}

span:nth-of-type(10) {
  -webkit-animation-delay: 4s;
          animation-delay: 4s;
}

span:nth-of-type(11) {
  -webkit-animation-delay: 4.1s;
          animation-delay: 4.1s;
}

span:nth-of-type(12) {
  -webkit-animation-delay: 4.2s;
          animation-delay: 4.2s;
}

span:nth-of-type(13) {
  -webkit-animation-delay: 4.3s;
          animation-delay: 4.3s;
}

span:nth-of-type(14) {
  -webkit-animation-delay: 4.4s;
          animation-delay: 4.4s;
}

span:nth-of-type(15) {
  -webkit-animation-delay: 4.5s;
          animation-delay: 4.5s;
}

span:nth-of-type(16) {
  -webkit-animation-delay: 4.6s;
          animation-delay: 4.6s;
}

span:nth-of-type(17) {
  -webkit-animation-delay: 4.7s;
          animation-delay: 4.7s;
}

span:nth-of-type(18) {
  -webkit-animation-delay: 4.8s;
          animation-delay: 4.8s;
}

span:nth-of-type(19) {
  -webkit-animation-delay: 4.9s;
          animation-delay: 4.9s;
}

span:nth-of-type(20) {
  -webkit-animation-delay: 5s;
          animation-delay: 5s;
}

span:nth-of-type(21) {
  -webkit-animation-delay: 5.1s;
          animation-delay: 5.1s;
}

</style>