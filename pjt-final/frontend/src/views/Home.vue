<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/dog.gif">
    <div>
      <b-form-select v-model="selected" :options="options" multiple :select-size="4"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  jyp_m: '03',
  jyp_d: '26',

  data() {
      const options = []
      for (let index = 1; index < 13; index++) {
        options.push({value: index, text: index})
      }
      return {
        selected: ['1995'], // Array reference
        options
      }
    },
}
</script>
