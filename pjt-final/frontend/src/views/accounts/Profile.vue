<template>
  <div id="app"> 
    <h1>{{ $store.state.user.username }}의 프로필</h1>
    <h3>나이 : {{ 2022 - $store.state.user.birthday.year }}</h3>
    <h3>본것 : {{ }}</h3>
    <h3>장르선택 비율 : {{  }}</h3>
    <h3>별자리 : </h3>

    <input type="text">
  </div>
</template>
<script>
//   const app = new Vue({
//     el: '#app',
//     data: {
//       year: 2022,
//     },
//     computed: {
//       howOld: function () {
//         return this.year
//       } 
//     }
// })
export default {
  name: 'profile'
}
</script>

<style>

</style>