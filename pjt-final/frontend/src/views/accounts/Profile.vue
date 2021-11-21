<template>
  <div id="app"> 
    <h1>{{ $store.state.user.username }}의 프로필</h1>
    <h3>나이 : {{ 2022 - $store.state.user.birthday.year }}</h3>
    <h3>본것 : {{ /*본 영화를 체크한 것 db저장 후 제목 출력*/ }}</h3>
    <h3>장르선택 비율 : {{ /*위의 본 영화 선택한 정보들 db에 저장 후 개인의 전체 비율을 고려해 %로 나타내기*/ }}</h3>
    <h3 v-if="($store.state.user.birthday.month == 1 && $store.state.user.birthday.day >= 20) || ($store.state.user.birthday.month == 2 && $store.state.user.birthday.day <= 18) ">별자리 : 물병자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 2 && $store.state.user.birthday.day >= 19) || ($store.state.user.birthday.month == 3 && $store.state.user.birthday.day <= 20)">별자리 : 물고기자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 3 && $store.state.user.birthday.day >= 21) || ($store.state.user.birthday.month == 4 && $store.state.user.birthday.day <= 19)">별자리 : 양자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 4 && $store.state.user.birthday.day >= 20) || ($store.state.user.birthday.month == 5 && $store.state.user.birthday.day <= 20)">별자리 : 황소자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 5 && $store.state.user.birthday.day >= 21) || ($store.state.user.birthday.month == 6 && $store.state.user.birthday.day <= 21)">별자리 : 쌍둥이자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 6 && $store.state.user.birthday.day >= 22) || ($store.state.user.birthday.month == 7 && $store.state.user.birthday.day <= 22)">별자리 : 게자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 7 && $store.state.user.birthday.day >= 23) || ($store.state.user.birthday.month == 8 && $store.state.user.birthday.day <= 22)">별자리 : 사자자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 8 && $store.state.user.birthday.day >= 23) || ($store.state.user.birthday.month == 9 && $store.state.user.birthday.day <= 23)">별자리 : 처녀자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 9 && $store.state.user.birthday.day >= 24) || ($store.state.user.birthday.month == 10 && $store.state.user.birthday.day <= 22)">별자리 : 천칭자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 10 && $store.state.user.birthday.day >= 23) || ($store.state.user.birthday.month == 11 && $store.state.user.birthday.day <= 22)">별자리 : 전갈자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 11 && $store.state.user.birthday.day >= 23) || ($store.state.user.birthday.month == 12 && $store.state.user.birthday.day <= 21)">별자리 : 사수자리 </h3>
    <h3 v-if="($store.state.user.birthday.month == 12 && $store.state.user.birthday.day >= 22) || ($store.state.user.birthday.month == 1 && $store.state.user.birthday.day <= 19)">별자리 : 염소자리 </h3>
    <h3>좋아요 한 게시글 : {{  }}</h3>
    <h3>작성글 : {{  }}</h3>
  </div>
</template>
<script>

export default {
  name: 'profile'
}
</script>

<style>

</style>