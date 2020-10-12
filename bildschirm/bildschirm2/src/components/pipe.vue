<template id="">
  <div class="pipe"
  v-bind:class="{'filled':pipe_filled}"
  v-bind:style="'background-color:' + color +
  '; width:' + box.width +
  'px; height:' + box.height +
  'px; top:' + box.top +
  'px; left:' + box.left +'px;'"
  >

  <p class="pipetext">{{text}}</p>
  </div>
</template>
<script type="text/javascript">
export default{
  name: 'pipe',
  props: [ 'text', 'box', 'color', 'pipe_before_filled', 'ventil_before_open'],
  data(){
    return{
      pipe_filled: this.pipe_before_filled && this.ventil_before_open,
      box_top: this.box.top,
      box_left: this.box.left,
      box_weight: this.box.weight,
      box_height: this.box.height

    }
  }
}
</script>
<style media="screen">
.pipe{
  position: absolute;
}
.pipetext{
  font-size: 10pt;
  margin-top: -12pt;
}
</style>
