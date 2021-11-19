<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/dog.gif">
    <div>
      <b-form-select v-model="y_selected" :options="y_options" multiple :select-size="1"></b-form-select>
      <b-form-select v-model="m_selected" :options="m_options" multiple :select-size="1"></b-form-select>
      <b-form-select v-model="d_selected" :options="d_options" multiple :select-size="1"></b-form-select>
      <div class="mt-3"> 
        <strong v-if="y_selected">{{ y_selected[0] }}년 </strong> 
        <strong v-if="m_selected">{{ m_selected[0] }}월 </strong> 
        <strong v-if="d_selected">{{ d_selected[0] }}일 </strong>
      </div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },

  data() {
<<<<<<< HEAD
      const options = []
      for (let index = 1; index < 13; index++) {
        options.push({value: index, text: index})
      }
      return {
        selected: ['1995'], // Array reference
        options
      }
    },
=======
      
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
        y_selected: [1995], // Array reference
        m_selected: [3], // Array reference
        d_selected: [26], // Array reference
        y_options,
        m_options,
        d_options
      }
    }
>>>>>>> 6ccd18cf59526a095234fce031e67b99d4273641
}
</script>