<template>
  <div id="app"> 
    <h1>나의 프로필</h1>
    <h3>나이 : {{ 2022 }}</h3>
    <h3>본것 : {{}}</h3>
    <h3>장르 취향</h3>
    <h3>별자리</h3>

    
    <input type="text">
  </div>
</template>
// <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
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