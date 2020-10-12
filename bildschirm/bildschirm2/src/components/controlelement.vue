<template id="">
  <div class="control wrapper" v-bind:class="[[{'hide':!this.controls_visible}, this.control_box]]" >
    <div class="auto" v-on:click="$emit('set-value', 2)">
      <p>{{translate('auto')}}</p>
    </div>
    <div class="placeholder"></div>
    <div class="manuel wrapper">
      <div class="left" v-on:click="$emit('set-value', 1)">
        <p>{{translate('on')}}</p>
      </div>
      <div class="placeholder"></div>
      <div class="right" v-on:click="$emit('set-value', 0)">
        <p>{{translate('off')}}</p>
      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
import vue from 'vue'

export default{
  name: 'controlelement',
  props:['controls_visible', 'control_box'],
  methods:{
    translate(text){
      return vue.$translate(text)
    },
    log(e){
      console.log(e);
    }
  },
  data(){
    return{

    }
  }
}
</script>
<style media="screen" scoped>
.hide{
  display: none !important;
}
.left{
}
.right{
  outline-offset: 0;
}
.placeholder{
  background-color: #2c3e50;
  flex: 0 0 2px !important;
}
.control{
  height: 100px;
  width: 100px;

  outline: solid #2c3e50 2.5px;

  background-color: #ccc;
}
.control div{
}
.control.oben{
  margin-top: -145px;
  margin-left: 0px;
}
.control.unten{
  margin-top: 75px;
  margin-left: 0px;
}

.pumpcontrol.control.oben{
  margin-top: -80px;
  margin-left: 0;
}
.pumpcontrol.control.unten{
  margin-top: 80px;
  margin-left: 0;
}
.wrapper{
  display: flex;
}
.wrapper > div{
  flex: 1 0 0;
}
.control{
  flex-direction: column;
}
.manuel{
  flex-direction: row;
}

</style>
