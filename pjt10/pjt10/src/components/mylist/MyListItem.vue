<template>
  <div class="item">
    <p @click="showMyMovie(myMovie)" class="mb-0 reduce-content hover-button" :class="{'is-completed': myMovie.isCompleted}">{{myMovie.title}}</p>
    <div class="btn-box">
      <button @click="completeMyMovie(myMovie)" class="button_base">V</button>
      <button @click="removeMyMovie" class="button_base">X</button>
    </div>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'

export default {
  name: 'MyListItem',
  props: {
    myMovie: {
      type: Object,
    }
  },
  methods: {
    ...mapMutations({
      completeMyMovie: "COMPLETE_MYMOVIE",
      showMyMovie: "SHOW_MYMOVIE",
    }),
    removeMyMovie: function() {
      if (confirm(`선택하신 "${this.myMovie.title}"를\n정말 삭제하시겠습니까?`)) {
        this.$store.commit("REMOVE_MYMOVIE", this.myMovie)
      }
    },
  },
}
</script>

<style scoped>
.item {
  display: flex;
  justify-content: space-between;
  text-decoration: none;
}
.item-content {
  display: inline-block;
}
.btn-box {
  display: inline-block;
  width: 3.5rem;
}
.reduce-content {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  width: calc(100% - 56px);
  /* display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient:vertical; */
}
.is-completed {
  text-decoration: line-through;
}
.button_base {
    margin: 0;
    border: 0;
    background-color: transparent;
}
.hover-button{
  background: transparent;
  color:black;
  border:none;
  position:relative;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
}
/* .hover-button:hover{
  background: #1AAB8A;
  color: #fff;
} */
/* .hover-button:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
} */
.hover-button:before,.hover-button:after{
  content:'';
  position:absolute;
  bottom:0;
  left:0;
  height:2px;
  width:0;
  background: khaki;
  transition:400ms ease all;
}
.hover-button:hover:before,.hover-button:hover:after{
  width:100%;
  transition:800ms ease all;
}
</style>