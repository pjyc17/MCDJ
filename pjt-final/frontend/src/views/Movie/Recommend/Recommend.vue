<template>
  <div :genres="getRecommendedGenres">
    <div class="text-center loading-center" v-if="isLoading">
      <label for="spinner"><img src="@/assets/dog.gif" alt="두리번.. 두리번.."></label>
      <div>
        <b-spinner id="spinner" style="color: grey;">     
        </b-spinner>
      </div>
    </div>
    <br>
    <div v-if="!isLoading">
      <recommend-genre
        v-for="genre in shownGenres" :key="genre.id"
        :genre="genre"
      />
    </div>
  </div>
</template>

<script>
import RecommendGenre from '@/views/Movie/Recommend/RecommendGenre.vue'
import {mapGetters} from 'vuex'

export default {
  name: 'Recommend',
  components: {
    RecommendGenre,
  },
  data: function() {
    return {
      genres: [],
      shownGenres: [],
      cnt: 3,
      flag: true,
      isLoading: true,
    }
  },
  methods: {
    listenScroll: function() {
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) <= 2 * clientHeight) {
        this.shownGenres.push(...this.genres.splice(0, this.cnt))
      }
    }
  },
  computed: {
      ...mapGetters(['getRecommendedGenres',]),
  },
  created() {
    window.scrollTo(0, 0)
    window.addEventListener('scroll', this.listenScroll);
    this.flag = true
    if (this.flag && this.getRecommendedGenres.length) {
      this.genres = [...this.getRecommendedGenres]
      this.isLoading = false
      this.shownGenres.push(...this.genres.splice(0, this.cnt))
      this.flag = false
    }
  },
  updated() {
    if (this.flag && this.getRecommendedGenres.length) {
      this.genres = [...this.getRecommendedGenres]
      this.isLoading = false
      this.shownGenres.push(...this.genres.splice(0, this.cnt))
      this.flag = false
    }
  },
  destroyed() {
    window.scrollTo(0, 0)
    window.removeEventListener('scroll', this.listenScroll);
  },
}
</script>

<style>

</style>