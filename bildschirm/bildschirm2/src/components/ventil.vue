<template id="">
  <div class="ventil"
  v-bind:style="'top:' + box.top + 'px; left:' + box.left +'px;'"
  v-on:click="open"
  v-bind:class="{'hide':invisible, 'hand_off':this.status==0, 'hand_on':this.status==1, 'auto_off': this.status==2, 'auto_on': this.status==3}"
  >
  <controlelement
  v-bind:controls_visible="controls_visible"
  v-on:set-value="this.set_value"
  v-bind:control_box="control_box"

  />
  </div>

</template>
<script type="text/javascript">
import controlelement from './controlelement.vue'
import axios from 'axios'

export default {
  name: 'ventil',
  components:{
    controlelement
  },
  props: {
    msg: String, box: Object, invisible:Boolean, control_box:String, handid: Number, handbetriebid:Number, betriebid:Number
  },
  methods: {
    open(){

      this.controls_visible = !this.controls_visible;
    },
    set_value(e){
      this.status = e
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: this.handid,
          value: e && !(e==2)
        }
      }).then(() => console.log('acc'))
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: this.handbetriebid,
          value: !(e==2)
        }
      }).then(() => {console.log('acc')})
    }
  }, data(){
    return{
      controls_visible: false,
      status: 2
    }
  }, created(){

    setInterval(()=> {

      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getvalue',
        data: {
          id: this.betriebid
        }
      }).then((e) => {
        if(this.status == 2 || this.status == 3){
          this.status = 2 + e.data.value
        }
      });

    }, 500)
  }
}

</script>
<style media="screen">
.hide{
  display: none;
}
.ventil{
  position: absolute;
  background-size: contain;
  background-position: center;

  height: 100px;
  width: 100px;


  z-index: 10;
}
.ventil.auto_off{
  background-image: url('images/Ventil_Vektor-02.svg');
}
.ventil.auto_on{
  background-image: url('images/Ventil_Vektor-04.svg');
}
.ventil.hand_off{
  background-image: url('images/Ventil_Vektor-01.svg');
}
.ventil.hand_on{
  background-image: url('images/Ventil_Vektor-03.svg');
}
</style>
