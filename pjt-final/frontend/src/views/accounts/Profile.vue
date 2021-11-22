<template>
  <div id="app"> 
    <header>
      <!-- <h3 v-if="($store.state.user.birthday.month == 1 && $store.state.user.birthday.date >= 20) || ($store.state.user.birthday.month == 2 && $store.state.user.birthday.date <= 18) "><img height="40" src="@/assets/별자리/물병자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 2 && $store.state.user.birthday.date >= 19) || ($store.state.user.birthday.month == 3 && $store.state.user.birthday.date <= 20)"><img height="40" src="@/assets/별자리/물고기자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 3 && $store.state.user.birthday.date >= 21) || ($store.state.user.birthday.month == 4 && $store.state.user.birthday.date <= 19)"><img height="40" src="@/assets/별자리/양자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 4 && $store.state.user.birthday.date >= 20) || ($store.state.user.birthday.month == 5 && $store.state.user.birthday.date <= 20)"><img height="40" src="@/assets/별자리/황소자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 5 && $store.state.user.birthday.date >= 21) || ($store.state.user.birthday.month == 6 && $store.state.user.birthday.date <= 21)"><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 6 && $store.state.user.birthday.date >= 22) || ($store.state.user.birthday.month == 7 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/게자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 7 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 8 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/사자자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 8 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 9 && $store.state.user.birthday.date <= 23)"><img height="40" src="@/assets/별자리/처녀자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 9 && $store.state.user.birthday.date >= 24) || ($store.state.user.birthday.month == 10 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/천칭자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 10 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 11 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/전갈자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 11 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 12 && $store.state.user.birthday.date <= 21)"><img height="40" src="@/assets/별자리/사수자리.png" alt=""></h3>
      <h3 v-if="($store.state.user.birthday.month == 12 && $store.state.user.birthday.date >= 22) || ($store.state.user.birthday.month == 1 && $store.state.user.birthday.date <= 19)"><img height="40" src="@/assets/별자리/염소자리.png" alt=""></h3> -->
      
      <h1>{{ $store.state.user.username }}'s Profile</h1>
      <h3>age : {{ 2022 - $store.state.user.birthday.year }}</h3>
      <h3 v-if="True">watched : {{ /*본 영화를 체크한 것 db저장 후 제목 출력*/ }}</h3>
      
      <h3>genre : {{ /*위의 본 영화 선택한 정보들 db에 저장 후 개인의 전체 비율을 고려해 %로 나타내기*/ }}</h3>
      <h3 v-if="($store.state.user.birthday.month == 1 && $store.state.user.birthday.date >= 20) || ($store.state.user.birthday.month == 2 && $store.state.user.birthday.date <= 18) "><img height="40" src="@/assets/별자리/물병자리.png" alt="">star : Aquarius </h3>
      <h3 v-if="($store.state.user.birthday.month == 2 && $store.state.user.birthday.date >= 19) || ($store.state.user.birthday.month == 3 && $store.state.user.birthday.date <= 20)"><img height="40" src="@/assets/별자리/물고기자리.png" alt="">star : Prisces </h3>
      <h3 v-if="($store.state.user.birthday.month == 3 && $store.state.user.birthday.date >= 21) || ($store.state.user.birthday.month == 4 && $store.state.user.birthday.date <= 19)"><img height="40" src="@/assets/별자리/양자리.png" alt=""> star : Aries </h3>
      <h3 v-if="($store.state.user.birthday.month == 4 && $store.state.user.birthday.date >= 20) || ($store.state.user.birthday.month == 5 && $store.state.user.birthday.date <= 20)"><img height="40" src="@/assets/별자리/황소자리.png" alt="">star : Taurus </h3>
      <h3 v-if="($store.state.user.birthday.month == 5 && $store.state.user.birthday.date >= 21) || ($store.state.user.birthday.month == 6 && $store.state.user.birthday.date <= 21)"><img height="40" src="@/assets/별자리/쌍둥이자리.png" alt="">star : Gemini </h3>
      <h3 v-if="($store.state.user.birthday.month == 6 && $store.state.user.birthday.date >= 22) || ($store.state.user.birthday.month == 7 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/게자리.png" alt="">star : Cancer </h3>
      <h3 v-if="($store.state.user.birthday.month == 7 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 8 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/사자자리.png" alt="">star : Leo </h3>
      <h3 v-if="($store.state.user.birthday.month == 8 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 9 && $store.state.user.birthday.date <= 23)"><img height="40" src="@/assets/별자리/처녀자리.png" alt="">star : Virgo </h3>
      <h3 v-if="($store.state.user.birthday.month == 9 && $store.state.user.birthday.date >= 24) || ($store.state.user.birthday.month == 10 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/천칭자리.png" alt="">star : Libra </h3>
      <h3 v-if="($store.state.user.birthday.month == 10 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 11 && $store.state.user.birthday.date <= 22)"><img height="40" src="@/assets/별자리/전갈자리.png" alt="">star : Scorpio </h3>
      <h3 v-if="($store.state.user.birthday.month == 11 && $store.state.user.birthday.date >= 23) || ($store.state.user.birthday.month == 12 && $store.state.user.birthday.date <= 21)"><img height="40" src="@/assets/별자리/사수자리.png" alt="">star : Sagittarius </h3>
      <h3 v-if="($store.state.user.birthday.month == 12 && $store.state.user.birthday.date >= 22) || ($store.state.user.birthday.month == 1 && $store.state.user.birthday.date <= 19)"><img height="40" src="@/assets/별자리/염소자리.png" alt="">star : Capricorn </h3>
      <h3>likes article : {{  }}</h3>
      <h3>written review : {{  }}</h3>
      <!-- <img height="30" v-if="($store.state.user.birthday.month == 3 && $store.state.user.birthday.date >= 21) || ($store.state.user.birthday.month == 4 && $store.state.user.birthday.date <= 19)" src="@/assets/양자리.png" alt=""> -->
    </header>
  </div>
</template>
<script>

export default {
  name: 'profile'
}
</script>

<style scoped>
header {
  /* width: 100%; */
  /* height: 100%; */
  /* text-align: center; */
  position: relative;
  font-family: 'Sucrose Bold Two';
  background: url(../../assets/gorhf.png) no-repeat;
  background-size: cover;
  padding-top:30.93333333%;
  opacity: 0.3;
  /* z-index: 1; */
}
/* header::after {
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: "";
  position: absolute;
  z-index: -1;
  
} */

</style>