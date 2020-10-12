<template id="">
 <div class="adminsensors">
   <button type="button" name="button" v-on:click="$emit('back')">{{translate('back')}}</button>
   <p>Grundfos Sensors</p>
   <div v-for="sensor in this.sensors"  :key="sensor.id" class="sensors">
     <div class="one">{{sensor.id}}</div>
     <div class="one" v-on:click="go_input(sensor, 4)">
       <a v-bind:class="{'hide':sensor.input==4}" >{{sensor.type}}</a>
       <input type="text" name="" v-model="sensor.type" v-bind:class="{'hide':sensor.input!=4}" v-on:keyup-enter="sensor.input=0"></div>
     <div class="four" v-on:click="go_input(sensor, 1)">
       <a v-bind:class="{'hide':sensor.input==1}" >{{sensor.barcode}}</a>
       <input type="text" name="" v-model="sensor.barcode" v-bind:class="{'hide':sensor.input!=1}" v-on:keyup-enter="sensor.input=0">
     </div>
     <div class="two" v-on:click="go_input(sensor, 2)">
       <a v-bind:class="{'hide':sensor.input==2}">{{sensor.name}}</a>
       <input type="text" name="" v-model="sensor.name" v-bind:class="{'hide':sensor.input!=2}">
     </div>
     <div class="one" v-on:click="go_input(sensor, 3)">
       <a v-bind:class="{'hide':sensor.input!=3}">{{sensor.number}}</a>
       <input type="text" name="" v-model="sensor.number" v-bind:class="{'hide':sensor.input!=3}">
     </div>
   </div>
 </div>
</template>
<script type="text/javascript">
import axios from 'axios'
import vue from 'vue'

export default{
  name: 'adminsensors',
  methods:{
    translate(text){
      return vue.$translate(text);
    },
    go_input(sensor, number){
      sensor.input = number

      if(number == 1)
        vue.$openkeyboard(sensor.barcode, (input) => sensor.barcode=input, () => this.close_input(sensor))
      else if (number == 2)
        vue.$openkeyboard(sensor.name, (input) => sensor.name=input, () => this.close_input(sensor))
      else if (number == 3)
        vue.$openkeyboard(sensor.number, (input) => sensor.number=input, () => this.close_input(sensor))
      else if (number == 4)
        vue.$openkeyboard(sensor.number, (input) => sensor.type=input, () => this.close_input(sensor))
    },
    close_input(sensor){
      sensor.input = 0

      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setsensors',
        data: {
          token: vue.$admintoken,
          sensors: this.sensors
        }
      }).then(e => console.log(e)
      ).catch(e => console.log(e));
    },
    open(){
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getsensors',
        data: {
          token: vue.$admintoken
        }
      }).then((e) => {
        if(e.data.sensors){
          for (const sensor of e.data.sensors) {
            sensor.input = 0;
          }
          this.sensors = e.data.sensors
        }
      }).catch(e => console.log(e));
    }
  },
  data(){
    return{
      sensors:[
        {id: 1, type: 'MFS', barcode: '99455941-01-850-00079', name: 'MFS 2-40', number:1, input:0},
        {id: 2, type: 'RPS', barcode: '99455941-01-850-00079', name: 'MFS 0-16', number:1, input:0},
        {id: 3, type: 'VFS', barcode: '99455941-01-850-00079', name: 'MFS 2-40', number:1, input:0},

      ]

    }
  },

}
</script>
<style media="screen">
.adminsensors p{
  font-size: 20pt;
}
.sensors{
  display: flex;
  flex-direction: row;
}
.sensors div.one{
  flex: 1 0 0;
}
.sensors div.two{
  flex: 2 0 0;
}
.sensors div.four{
  flex: 4 0 0;
}
</style>
