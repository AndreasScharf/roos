<template id="">
  <div class="tank"
  v-bind:style="
  'width:' + box.width +
  'px; height:' + box.height +
  'px; top:' + box.top +
  'px; left:' + box.left +'px;'"
  >
    <div class="water" v-bind:style="'flex: 0 0 ' + level + '%;'">
      <a>
        {{level + '%'}}
      </a>
    </div>
    <p class="pipetext" v-bind:style="'height: ' + (100 - level) + '%;'">{{text}}</p>
  </div>

</template>
<script type="text/javascript">
import axios from 'axios'

export default{
  name: 'tank',
  props: [ 'text', 'box', 'data_id'],
  data(){
    return{
      pipe_filled: this.pipe_before_filled && this.ventil_before_open,
      box_top: this.box.top,
      box_left: this.box.left,
      box_weight: this.box.weight,
      box_height: this.box.height,


      level: 40.7
    }
  },
  created(){
    setInterval(() => {
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getvalue',
        data: {
          id: this.data_id
        }
      }).then((e) => {
        this.level = e.data.value;
      });
    }, 500)

  }
}
</script>
<style media="screen">
.tank{
  border: solid black 2pt;
  border-top: none;
  position: absolute;
  display: flex;
  flex-direction: column-reverse;

}
.tank .water{
  background-color: #00FFFF;
}
.tank .water a{
  background-color: white;
  font-weight: bold;
  margin-top: -14pt;
  margin-left: -14pt;
  position: absolute;
}
</style>
