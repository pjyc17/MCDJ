<template>
  <div>
    {{myMovie}}
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'MyMovieDetail',
  computed: {
    ...mapState(['myMovie',]),
  }
}
</script>

<style>

</style>