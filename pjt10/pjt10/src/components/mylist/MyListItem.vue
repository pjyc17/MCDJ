<template>
  <div>
    {{myMovie.title}}
  </div>
</template>

<script>
export default {
  name: 'MyListItem',
  props: {
    myMovie: {
      type: Object,
    }
  }
}
</script>

<style>

</style>