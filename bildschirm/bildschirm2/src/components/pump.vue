<template id="">
  <div class="pump"
  v-bind:style="'top:' + box.top + 'px; left:' + box.left +'px;'"
  v-on:click="open"
  v-bind:class="{'hide':invisible, 'hand_off':this.status==0, 'hand_on':this.status==1, 'auto_off': this.status==2, 'auto_on': this.status==3}"
  >
  <controlelement
  v-bind:controls_visible="controls_visible"
  v-on:set-value="this.set_value"
  v-bind:control_box="control_box"
  class="pumpcontrol"
  />
  </div>

</template>
<script type="text/javascript">
import controlelement from './controlelement.vue'
import axios from 'axios'

export default {
  name: 'pump',
  components:{
    controlelement
  },
  props: {
    box: Object, invisible:Boolean, control_box:String, handid: Number, handbetriebid:Number, betriebid:Number
  },
  methods: {
    open(){

      this.controls_visible = !this.controls_visible;
    },
    set_value(status){
      this.status = status
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: this.handid,
          value: status && !(status==2)
        }
      }).then(() => {this.status = status})
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: this.handbetriebid,
          value: !(status==2)
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
.pump{
  position: absolute;

  background-image: url('images/Pumpe_Vektor-02.svg');
  background-size: contain;
  background-position: center;


  height: 100px;
  width: 100px;

  z-index: 20;
}
.pump.hand_off{
  background-image: url('images/Pumpe_Vektor-01.svg');
}
.pump.hand_on{
  background-image: url('images/Pumpe_Vektor-03.svg');
}
.pump.auto_on{
  background-image: url('images/Pumpe_Vektor-04.svg');

}
.pump.auto_off{
  background-image: url('images/Pumpe_Vektor-02.svg');
}
.zeige_nach_oben{
  transform: rotate(-90deg);
}
.zeige_nach_oben .pumpcontrol{
  transform: rotate(90deg);
}
.zeige_nach_unten{
  transform: rotate(90deg);

}
.zeige_nach_unten .pumpcontrol{
  transform: rotate(-90deg);
}
.zeige_nach_unten .control{
  transform: rotate(-90deg);
}
</style>
