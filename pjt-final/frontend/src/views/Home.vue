<template>
  <div class="home">
    <img alt="MCDJ logo" class="logo" src="../../public/favicon/android-chrome-384x384.png">
    <!-- <br>
    <img src="@/assets/그림5.png" alt=""> -->

    <header v-if="$store.state.user.birthday.year === $store.state.today.year && $store.state.user.birthday.month === $store.state.today.month && $store.state.user.birthday.date === $store.state.today.date">
    <!-- <header> -->
      <h1>Go <span>to</span> <span><h2>the</h2></span><h3>{{ y_selected[0] }}<h4 style="text-align:right">{{ m_selected[0] }} / {{ d_selected[0] }} </h4></h3></h1>
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
        <div class="bounce inline-block">
          <button @click="getBirthday" class="btn-3d green">저장</button>
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
    <div>
      <span>M</span><span>O</span><span>V</span><span>I</span><span>E</span><span>&nbsp;</span><span>C</span><span>H</span><span>R</span><span>O</span><span>N</span><span>O</span><span>L</span><span>O</span><span>G</span><span>Y</span>
    </div>
    <div>
      <span>d</span><span>o</span><span>n</span><span>g</span><span>&nbsp;</span><span>y</span><span>u</span><span>&nbsp;</span><span>&</span><span>&nbsp;</span><span>j</span><span>u</span><span>&nbsp;</span><span>y</span><span>o</span><span>o</span><span>n</span>
    </div>
    <div>
      <h1 v-if="$store.state.user.id" @click="goToChronologyYear" class="blinking cursor hover-btn" >Ok!! Let's Go {{$store.state.user.birthday.year}}.{{$store.state.user.birthday.month}}.{{$store.state.user.birthday.date}}!!!</h1>
      <h1 v-else @click="goToChronologyYear" class="blinking cursor hover-btn" >Ok!! Let's Go {{y_selected[0]}}.{{m_selected[0]}}.{{d_selected[0]}}!!!</h1>
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
      y_selected: [this.$store.state.user.birthday.year], // Array reference
      m_selected: [this.$store.state.user.birthday.month], // Array reference
      d_selected: [this.$store.state.user.birthday.date], // Array reference
      y_options,
      m_options,
      d_options,
      isUser: false,
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
    goToChronologyYear: function() {
      if (this.$store.state.user.id) {this.$router.push({name: 'ChronologyYear', params: {year: this.$store.state.user.birthday.year}})}
      else {this.$router.push({name: 'ChronologyYear', params: {year: this.y_selected[0]}})}
    }
  },
}

</script>
<style scoped>
.MCDJ {
  position: fixed;
  bottom: 2rem;

}
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
  height: 100%;
  font-family: 'Sucrose Bold Two';
  background: url(../assets/그림5.png) center 0  no-repeat;
  background-size: cover;
  padding-top:14%;
  /* opacity: 0.4; */
}
.blinking{ -webkit-animation:blink 0.5s ease-in-out infinite alternate; -moz-animation:blink 1.5s ease-in-out infinite alternate; animation:blink 0.5s ease-in-out infinite alternate;
animation-delay: 3s; } 
@-webkit-keyframes blink{ 0% {opacity:0;} 100% {opacity:1;} } 
@-moz-keyframes blink{ 0% {opacity:0;} 100% {opacity:1;} } 
@keyframes blink{ 0% {opacity:0;} 100% {opacity:1;} }

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
  top: 30rem;
  left: 12rem;
  font-size: 12vw;
  line-height: .5;
  margin-top: 0;
  color: whitesmoke;
  text-align: left;
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 3.5s both;
          animation: smoky 5s 3.5s both;
}
header h1 span {
  position: fixed;
  top: -10rem;
  right: -60rem;
  font-size: 8.75vw;
  color: whitesmoke;
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 3s both;
          animation: smoky 5s 3s both;
}
header h2 {
  position: fixed;
  bottom: -20rem;
  /* right: 2rem; */
  font-size: 8vw;
  color: whitesmoke;
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 1s both;
          animation: smoky 5s 1s both;

}
header h3 {
  position: fixed;
  bottom: -20rem;
  right: -50rem;
  font-size: 8vw;
  color: whitesmoke ;
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 2s both;
          animation: smoky 5s 2s both;

}
header h3 h4 {
  position: fixed;
  font-size: 4vw;
  /* bottom: 7rem; */
  right: -20rem;
  text-align:right;
  display: inline-block;
  text-shadow: 0 0 0 whitesmoke;
  -webkit-animation: smoky 5s 3s both;
          animation: smoky 5s 3s both;
  

}
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

.bounce { 
  position: relative; 
/* 파폭 */ 
  -moz-animation: bounce 0.7s infinite linear; 
/* 크롬 */ 
  -webkit-animation: bounce 0.7s; 
  -o-animation: bounce 0.7s infinite linear; 
  animation: bounce 2s; 
  animation-delay: 0.5s;
  animation-iteration-count: 5;
}
@-webkit-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-moz-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-o-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
@-ms-keyframes bounce { 0% { top: 0; } 50% { top: -5px; } 70% { top: -50px; } 100% { top: 0; } } 
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
* {
	box-sizing: border-box;
}
body {
	margin: 0;
	background: #eaedf1;
	font-family: 'Lato', sans-serif;
}
.header {
	background: white;
	padding: 30px;
	text-align: center;
}
.header h1 {
	font-weight: 300;
	display: inline;
}
h2 {
	color: #89867e;
	text-align: center;
	font-weight: 300;
}
.color {
	width: 350px;
	margin: 0 auto;
}
.color li {
	margin: 0 15px 0 0;
	width: 30px;
	height: 30px;
	display: inline-block;
	border-radius: 100%;
}
.color .red    {background: #fa5a5a;}
.color .yellow {background: #f0d264;}
.color .green  {background: #82c8a0;}
.color .cyan   {background: #7fccde;}
.color .blue   {background: #6698cb;}
.color .purple {background: #cb99c5;}

.content, 
.content-gradient, 
.content-3d {
  margin: 40px auto;
}
.content {
  width: 80%;
  max-width: 700px;
}
.content-3d {
  width: 50%;
  max-width: 300px;
}
pre {
	width: 100%;
	padding: 30px;
	background-color: rgba(0, 0, 0, 0.72);
	color: #f8f8f2;
	border-radius: 0 0 4px 4px;
	margin-top: 20px;
  white-space: pre-wrap; /* css-3 */
  white-space: -moz-pre-wrap; /* Mozilla, since 1999 */
  white-space: -pre-wrap; /* Opera 4-6 */
  white-space: -o-pre-wrap; /* Opera 7 */
  word-wrap: break-word; /* Internet Explorer 5.5+ */
}
pre .bt  {color: #f8f8f2;} /* <> */
pre .anc {color: #f92672;} /* anchor tag */
pre .att {color: #a6a926;} /* attribute */
pre .val {color: #e6db74;} /* value */

.btn-container, .container {
	background-color: white;
	border-radius: 4px;
	text-align: center;
	margin-bottom: 40px;
}
.container h2 {
	padding-top: 30px;
	font-weight: 300;
}
.hover-btn {
  color: white;
}
.hover-btn:hover {
  color: #eddc5a;
}



</style>