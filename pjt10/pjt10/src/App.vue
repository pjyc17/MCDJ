<template>
  <div id="app">
    <div id="nav" class="navbar navbar-light bg-light py-1">
      <div class="container-fluid navbar-container">
        <a class="navbar-brand p-0" href="https://edu.ssafy.com/">
          <img src="https://edu.ssafy.com/asset/images/logo.png" alt="SSAFY" height="24" class="d-inline-block align-text-top">
        </a>
        <div class="box">
          <router-link to="/">Home</router-link> |
          <router-link to="/random">Random</router-link> |
          <router-link to="/my-movie-list">MyMovieList</router-link>
        </div>
      </div>
    </div>
    <div class="box2"></div>
    <router-view/>
  </div>
</template>
<script>
export default {
  // smart하게 만들었음, refresh 최적화
  created() {
    this.$store.dispatch('loadTopRatedMovies')
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* #nav {
  padding: 30px;
} */

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}
.navbar-container{
  display: flex;
  justify-content: space-between;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.box {
  display: inline-block;
}
.box2 {
  height: 2.5rem;
}
</style>
