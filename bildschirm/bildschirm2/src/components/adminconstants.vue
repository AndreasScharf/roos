<template id="">
  <div class="">
    <button class="back" v-on:click="$emit('back')">{{translate('back')}}</button>

    <valuerow v-bind:header="true" v-bind:data="{id: 'ID', name: 'name', value: translate('value'), comment: 'comment'}"/>
    <div class="tablewrapper">
      <valuerow v-for="row in this.table" :key="row.id" v-bind:data="row" v-on:edit="edit"/>
      <div class="keyboardpadding" v-bind:class="{'hide':!show_keyboard}"></div>
    </div>
  </div>

</template>
<script type="text/javascript">
import valuerow from './valuerow.vue'
import axios from 'axios'
import vue from 'vue'

export default{
  name: 'adminconstants',
  components:{
    valuerow
  },methods:{
    translate(text){
      return vue.$translate(text)
    },
    request_data(){
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getfixedvalue',
        data: {
          token: vue.$admintoken
        }
      }).then((e) => {
        if(e.data.table){
          this.table = e.data.table
        }else{
          this.$emit('show-login')
        }
      });
    },
    edit(e){
      this.show_keyboard = e
    }

  }, data(){
    return{
      table: [],
      show_keyboard:false
    }
  }, show(){
    this.methods.request_data()
  },
}
</script>
<style media="screen">

</style>
