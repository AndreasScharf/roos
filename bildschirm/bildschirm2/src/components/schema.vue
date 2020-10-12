<template id="">
  <div class="schema_panel"  v-on:click="click">

    <pipe v-bind:text="translate('intake')" v-bind:box="{'top':60, 'left':10, 'width':90, 'height': 10}" pipe_before_filled="true" ventil_before_open="true" color="#1E90FF"/>
    <ventil v-bind:box="{'top':10, 'left':55 }" control_box="unten" v-bind:handid="42" v-bind:handbetriebid="43" v-bind:betriebid="44"/>
    <pipe text="" v-bind:box="{'top':60, 'left':100, 'width':100, 'height': 10}" pipe_before_filled="true" ventil_before_open="true" color="#1E90FF"/>
    <datalabel name="" unit=" bar" v-bind:dataid="5" v-bind:box="{'top':45, 'left':140}"/>


    <!--<pipe text="" v-bind:box="{'top':50, 'left':200, 'width':35, 'height': 60}" pipe_before_filled="true" ventil_before_open="true" color="darkgrey"/>Cadrigde filter-->
    <canvas id="cadridgefilter" ref="cadrigefilter" height="60" width="35"></canvas>
    <datalabel name="dp: " unit=" bar" v-bind:dataid="16" v-bind:box="{'top':115, 'left':180}"/>

    <pipe text="" v-bind:box="{'top':60, 'left':260, 'width':10, 'height': 190}" pipe_before_filled="true" ventil_before_open="true" color="yellow"/><!--Antiskalant-->

    <pump v-bind:box="{'top':205, 'left':215 }" control_box="unten" class="zeige_nach_oben" v-bind:handid="36" v-bind:handbetriebid="38" v-bind:betriebid="37"/><!--Antiskalant-->

    <datalabel name="" unit=" bar" v-bind:dataid="6" v-bind:box="{'top':30, 'left':290}"/>
    <datalabel name="" unit=" l/min" v-bind:dataid="7" v-bind:box="{'top':45, 'left':290}"/>
    <pipe text="" v-bind:box="{'top':60, 'left':235, 'width':145, 'height': 10}" pipe_before_filled="true" ventil_before_open="true" color="#1E90FF"/>
    <pipe text="" v-bind:box="{'top':70, 'left':335, 'width':10, 'height': 100}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/><!--Zirkulation-->

    <pump v-bind:box="{'top':15, 'left':340 }" control_box="unten" v-bind:handid="48" v-bind:handbetriebid="49" v-bind:betriebid="50"/>

    <pipe text="" v-bind:box="{'top':60, 'left':355, 'width':80, 'height': 10}" pipe_before_filled="true" ventil_before_open="true" color="#1E90FF"/>
    <canvas id="ro_module" ref="romodule" top="45" left="435" width="170" height="40" style=""></canvas>
    <!--<pipe text="" v-bind:box="{'top':45, 'left':435, 'width':170, 'height': 40}" pipe_before_filled="true" ventil_before_open="true" color="green"/> RO Module-->

    <datalabel name="" unit=" uS" v-bind:dataid="12" v-bind:box="{'top':30, 'left':610}"/><!--Permate DF-->
    <datalabel name="" unit=" l/min" v-bind:dataid="8" v-bind:box="{'top':45, 'left':610}"/><!--Permate DF-->
    <pipe text="" v-bind:box="{'top':60, 'left':605, 'width':140, 'height':10}" pipe_before_filled="true" ventil_before_open="true" color="#00FFFF"/><!--Permate-->
    <pipe text="" v-bind:box="{'top':70, 'left': 735, 'width':10, 'height':30}" pipe_before_filled="true" ventil_before_open="true" color="#00FFFF"/><!--Permate-->
    <datalabel name="permate" unit="" v-bind:dataid="0" v-bind:box="{'top':70, 'left':630}"/><!--Permate label-->


    <datalabel name="" unit=" bar" v-bind:dataid="9" v-bind:box="{'top':130, 'left':430}"/><!--Zirkulation Pr-->
    <datalabel name="" unit=" l/min" v-bind:dataid="10" v-bind:box="{'top':145, 'left':430}"/><!--Zirkulation DF-->
    <pipe text="" v-bind:box="{'top':85, 'left':590, 'width':10, 'height':80}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/><!--Zirkulation-->
    <pipe text="" v-bind:box="{'top':160, 'left':335, 'width':265, 'height':10}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/><!--Zirkulation-->
    <svg style="left: 390px; top: 137.5px;" width="20" height="30" class="regelventil no2">
      <line x1="0" y1="0" x2="20" y2="0" style="stroke:black;stroke-width:2" />
      <line x1="10" y1="0" x2="10" y2="12" style="stroke:black;stroke-width:2" />
      <polygon points="2 12,10 28,18 12" style="fill:grey;stroke:black;stroke-width:2;" />
    </svg>
    <svg style="left: 595px; top: 190px;" width="30" height="20" class="regelventil no2">
      <line x1="28" y1="0" x2="28" y2="20" style="stroke:black;stroke-width:2" />
      <line x1="18" y1="10" x2="28" y2="10" style="stroke:black;stroke-width:2" />
      <polygon points="2 10,18 2,18 18" style="fill:grey;stroke:black;stroke-width:2;" />
    </svg>


    <pipe text="" v-bind:box="{'top':160, 'left':485, 'width':10, 'height':90}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/><!--Zirkulation-->
    <pipe text="" v-bind:box="{'top':250, 'left':485, 'width':105, 'height':10}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/><!--Zirkulation-->


    <ventil v-bind:box="{'top':155, 'left':446 }"  class="zeige_nach_unten" control_box="unten" v-bind:handid="45" v-bind:handbetriebid="46" v-bind:betriebid="47"/>
    <pipe text="" v-bind:box="{'top':170, 'left':590, 'width':10, 'height':130}" pipe_before_filled="true" ventil_before_open="true" color="#008080"/>
    <datalabel v-bind:name="('drain')" unit="" v-bind:dataid="0" v-bind:box="{'top':280, 'left':610}"/><!--drain label-->


    <tank v-bind:box="{'top':100, 'left':687.5, 'width':100, 'height':125}" data_id="22"/>

    <datalabel name="amount raw water: " unit=" m³" v-bind:dataid="18" v-bind:box="{'top':200, 'left':30}"/><!--Rohwasser label-->
    <datalabel name="amount permate: " unit=" m³" v-bind:dataid="19" v-bind:box="{'top':215, 'left':30}"/><!--Rohwasser label-->
    <datalabel name="amount circulation: " unit=" m³" v-bind:dataid="20" v-bind:box="{'top':230, 'left':30}"/><!--Rohwasser label-->
    <datalabel name="amount concentrade: " unit=" m³" v-bind:dataid="21" v-bind:box="{'top':245, 'left':30}"/><!--Rohwasser label-->
    <datalabel name="temperature: " unit=" 'C" v-bind:dataid="23" v-bind:box="{'top':260, 'left':30}"/><!--Rohwasser label-->

    <a class="status" top="300" left="30">{{this.current_status}}</a>


  <!--  <div class="border" v-for:="item in this.item" :id="item.id" v-bind:box="item.box"   v-bind:style="'width:' + item.box.width +
      'px; height:' + item.box.height +
      'px; top:' + item.box.top +
      'px; left:' + item.box.left +'px; position:absolute; background-color:black;'">

    </div>
-->
  </div>
</template>
<script type="text/javascript">
import pipe from './pipe.vue'
import ventil from './ventil.vue'
import pump from './pump.vue'
import tank from './tank.vue'
import datalabel from './datalabel.vue'
import vue from 'vue'

import { v4 as uuidv4 } from 'uuid'
import axios from 'axios'

export default{
  name: 'schema',
  components: {
    pipe,
    ventil,
    pump,
    tank,
    datalabel
  }, methods:{
    translate(text){
      return vue.$translate(text)
    },
    click(){

    },

  },
  data(){
    return{
      item:[
        {id:uuidv4(), box:{left:10, top:58, width:90, height:2}},
        {id:uuidv4(), box:{left:10, top:70, width:90, height:2}},

        {id:uuidv4(), box:{left:100, top:58, width:100, height:2}},
        {id:uuidv4(), box:{left:100, top:70, width:100, height:2}},

        {id:uuidv4(), box:{left:235, top:58, width:140, height:2}},
        {id:uuidv4(), box:{left:235, top:70, width:25, height:2}},
        {id:uuidv4(), box:{left:270, top:70, width:65, height:2}},
        {id:uuidv4(), box:{left:345, top:70, width:30, height:2}},

        {id:uuidv4(), box:{left:385, top:58, width:50, height:2}},
        {id:uuidv4(), box:{left:385, top:70, width:50, height:2}},

        {id:uuidv4(), box:{left:258, top:70, width:2, height:190}},//Antiskalant
        {id:uuidv4(), box:{left:270, top:70, width:2, height:190}},//Antiskalant

        {id:uuidv4(), box:{left:332.5, top:70, width:2, height:212}},//Zirkulation
        {id:uuidv4(), box:{left:344.4, top:70, width:2, height:198}},//Zirkulation

        {id:uuidv4(), box:{left:332.5, top:280, width:312.5, height:2}},//Zirkulation
        {id:uuidv4(), box:{left:344.4, top:268, width:275.5, height:2}},//Zirkulation

        {id:uuidv4(), box:{left:618, top:70, width:2, height:198}},//Zirkulation
        {id:uuidv4(), box:{left:630, top:70, width:2, height:200}},//Zirkulation
        {id:uuidv4(), box:{left:630, top:268, width:20, height:2}},//Zirkulation

        {id:uuidv4(), box:{left:665, top:268, width:90, height:2}},//Ablauf
        {id:uuidv4(), box:{left:665, top:280, width:90, height:2}},//Ablauf


        {id:uuidv4(), box:{left:605, top:58, width:140, height:2}},//Permate
        {id:uuidv4(), box:{left:605, top:70, width:15, height:2}},//Permate
        {id:uuidv4(), box:{left:630, top:70, width:105, height:2}},//Permate

        {id:uuidv4(), box:{left:745, top:58, width:2, height:42}},//Permate
        {id:uuidv4(), box:{left:733, top:70, width:2, height:30}},//Permate


      ],
      line_gemalt: false,
      current_status: ''
    }
  },
  updated (){
  /*  if(this.line_gemalt)
      return;
*/


    console.log('gemalt');
    this.line_gemalt = true;
  },
  created(){
    vue.nextTick(() => {
      let ctx = this.$refs.romodule.getContext("2d");
      ctx.moveTo(0,0);
      ctx.lineTo(170,40);
      ctx.stroke();


      let ctx1 = this.$refs.cadrigefilter.getContext("2d");
      ctx1.moveTo(0,20);
      ctx1.lineTo(10,20);
      ctx1.lineTo(10, 40);
      ctx1.lineTo(25, 40);
      ctx1.lineTo(25, 20);
      ctx1.lineTo(35, 20);
      ctx1.stroke();
       });

    setInterval(()=>{
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/getcurrentstatus',
        data: {

        }
      }).then((e) => {
        this.current_status = e.data.status;
      });
    }, 500);
  }
}
</script>
<style media="screen">
a.status{
  font-size: 12pt;
  color: #292929;
  position: absolute;

  top: 300px;
  left: 30px;
}
.schema_panel{
  height: 80%;
  width: 100%;
}
.regelventil{
  position: absolute;
  z-index: 10;
}
#ro_module{
  position: absolute;
  top: 45px;
  left: 435px;
  outline:2pt solid black;
}
#cadridgefilter{
  position: absolute;

  background-color: darkgrey;
  top: 50px;
  left: 200px;
  width: 35px;
  height: 60px;
}
</style>
