<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/dog.gif">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <div>
      <b-form-select v-model="selected" :options="options" multiple :select-size="4"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  jyp_m: '03',
  jyp_d: '26',

  data() {
      return {
        selected: ['1995'], // Array reference
        options: [
          { value: 'a', text: 'This is First option' },
          { value: 'b', text: 'Default Selected Option' },
          { value: 'c', text: 'This is another option' },
          { value: 'd', text: 'This one is disabled', disabled: true },
          { value: 'e', text: 'This is option e' },
          { value: 'f', text: 'This is option f' },
          { value: 'g', text: 'This is option g' }
        ]
      }
    }
}
</script>
