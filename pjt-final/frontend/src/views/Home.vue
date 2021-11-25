<template>
  <div class="home">
      <img alt="MCDJ logo" class="logo class" src="../../public/favicon/android-chrome-384x384.png">


<header v-if="$store.state.user.birthday.year === $store.state.today.year && $store.state.user.birthday.month === $store.state.today.month && $store.state.user.birthday.date === $store.state.today.date">
<!-- <header> -->
  <h1>Go <span>to</span> <h2>the</h2><h3>{{ y_selected[0] }}<h4 style="text-align:right">{{ m_selected[0] }} / {{ d_selected[0] }} </h4></h3></h1>
  <!-- <img src="mountain-range-front.png"> -->
</header>
<header v-else>
  <h1>Go <span>to</span> <h2>the</h2><h3>{{ $store.state.user.birthday.year }}<h4 style="text-align:right">{{ $store.state.user.birthday.month }} / {{ $store.state.user.birthday.date }} </h4></h3></h1>
</header>

    <div class="imgbtf" v-if="$store.state.user.id === 0 || ($store.state.user.birthday.year === $store.state.today.year && $store.state.user.birthday.month === $store.state.today.month && $store.state.user.birthday.date === $store.state.today.date)">
      <div>
        <b-form-select v-model="y_selected" :options="y_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="m_selected" :options="m_options" multiple :select-size="1"></b-form-select>
        <b-form-select v-model="d_selected" :options="d_options" multiple :select-size="1"></b-form-select>
        <div class="bounce">
          <button @click="getBirthday">입력</button>
        </div>
      </div>
        <!-- <img src="../assets/그림5.png" alt="pointer"> -->
      <!-- <div>
        <div class="mt-3"> 
          <strong v-if="y_selected">{{ y_selected[0] }}년 </strong> 
          <strong v-if="m_selected">{{ m_selected[0] }}월 </strong> 
          <strong v-if="d_selected">{{ d_selected[0] }}일 </strong>
          <br>
        </div>
      </div> -->
    </div>
  </div>
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
/* .logo {
  position: fixed;
  display: flex;
  justify-content: center;
  top: 7rem;
} */
.home {
  position: fixed;
  top: 0px;
  /* background-image: url(../assets/그림1.png) no-repeat;
  background-size:cover; */
  /* position: relative; */
  /* top: -1rem; */
  /* bottom: 0px; */
  width: 100vw;
  height: 100vw;
  font-family: 'Sucrose Bold Two';
  background: url(../assets/그림5.png) center 0  no-repeat;
  background-size: contain;
  padding-top:14%;
}
/* .imgbtf {
  position: relative;
} */
/* .imgbtf .imgtxt {
  position: absolute;
  top:50;
  left: 50;
} */
/* .logo {
  position: relative;
  top: 100px;
  
}
.timeline {
  position: relative;
  top: 100px;

} */
header h1 { 
  position: fixed;
  top: 7rem;
  left: 2rem;
  font-size: 12vw;
  line-height: .5;
  margin-top: 0;
  text-align: left;
}
header h1 span {
  position: fixed;
  top: 7rem;
  right: 2rem;
  font-size: 8.75vw;
}
header h2 {
  position: fixed;
  bottom: 7rem;
  /* right: 2rem; */
  font-size: 8vw;

}
header h3 {
  position: fixed;
  bottom: 10rem;
  right: 2rem;
  font-size: 8vw;

}
header h3 h4 {
  position: fixed;
  font-size: 4vw;
  /* bottom: 7rem; */
  right: 2rem;
  text-align:right

}
.bounce { 
  position: relative; 
/* 파폭 */ 
  /* -moz-animation: bounce 0.7s infinite linear;  */
/* 크롬 */ 
  /* -webkit-animation: bounce 0.7s infinite linear;  */
  /* -o-animation: bounce 0.7s infinite linear;  */
  animation: bounce 2s infinite linear; 
  animation-delay: 2.1s;
  /* animation-iteration-count: 5; */
}
/* @-webkit-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-moz-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-o-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-ms-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } }  */
@keyframes bounce { 0% { top: 0; } 5% { top: -5px; } 15% { top: -50px; } 20% { top: 0; } }


/* @font-face {
    font-family: 'IM Fell French Canon Pro';
    src: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/im-fell-french-canon-pro.woff2') format('woff2');
} */
/* header { 
  background: url(../assets/gorhf.png) no-repeat;
  padding-top: 51.93333333%;
  background-size: cover;
  font-family: 'Sucrose Bold Two';
}
header img {
  position: absolute;
  top: 0;
  right: 0;
  width: 45.8%;
}
header h1 { 
  position: fixed;
  top: 2rem;
  right: 2rem;
  font-size: 12vw;
  line-height: .8;
  margin-top: 0;
  text-align: center;
}
header h1 span {
  display: block;
  font-size: 8.75vw;
}
main { 
  background: #000;
  position: relative;
  border: 1px solid #fff;
  font-family: 'IM Fell French Canon Pro';
  font-size: 1.4rem;
  padding: 2rem 25%;
  line-height: 1.6;
  
}
@media all and (max-width: 400px) {
  main { padding: 2rem; }
} */
.class{
	animation-name:out;
	animation-duration:1s;
	/* Safari and Chrome: */
	-webkit-animation-name:out;
	-webkit-animation-duration:1s;
}

.class:hover{
animation-name:in;
animation-duration:1s;
animation-iteration-count:infinite;
animation-direction:normal;
/* Safari and Chrome: */
-webkit-animation-name:in;
-webkit-animation-duration:1s;
-webkit-animation-iteration-count:infinite;
-webkit-animation-direction:alternate;
}

@keyframes in
{
from {transform: rotate(50deg);}
to   {transform: rotate(360deg);}
}
@-webkit-keyframes in /* Safari and Chrome */
{
from {transform: rotate(50deg);}
to   {-webkit-transform: rotate(360deg);}
}
@keyframes out
{
from {transform: rotate(360deg);}
to   {transform: rotate(0deg);}
}
@-webkit-keyframes out /* Safari and Chrome */
{
from {transform: rotate(360deg);}
to   {-webkit-transform: rotate(0deg);}
}
</style>