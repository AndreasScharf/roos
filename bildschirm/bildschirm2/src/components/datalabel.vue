<template id="">
  <div class="label"
  v-bind:style="'top:' + box.top + 'px; left:' + box.left +'px;'">
    {{translate(name)}}
    <a>{{this.value}}</a>
    {{unit}}
  </div>
</template>
<script type="text/javascript">
import vue from 'vue'
import axios from 'axios'

export default{
  name:'datalabel',
  props:{name: String, dataid:Number, box:Object, unit:String},
  methods:{
    translate(text){
      return vue.$translate(text);
    }
  },
  data(){
    return{
      value: 0
    }
  },
  created(){
    if(!this.dataid){
      this.value = ''
      return;
    }
    setInterval(()=>{
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getvalue',
        data: {
          id: this.dataid
        }
      }).then((e) => {
        this.value = Math.round(e.data.value*100)/100;
      });
    }, 500)
  }
}
</script>
<style media="screen">
.label{
  position: absolute;
  font-size: 10pt;
}
</style>
