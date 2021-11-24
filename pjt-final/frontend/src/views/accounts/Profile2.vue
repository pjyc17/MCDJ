<template>
  <div></div>
</template>

<script>
export default {
  name: 'Profile2',
  created() {
    this.$router.push({name: 'Profile', params: {userId: this.$route.params.userId}})
  }
}
</script>

<style>

</style>