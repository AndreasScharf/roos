<template id="">
  <div class="">
    <div class="header" >
      <p>{{translate('adminpanel')}}</p>
    </div>

    <div class="" v-bind:class="{'hide': !(panel==0)}">

      <div class="buttonwrapper">
        <div class="placeholder"></div>
        <button type="button" name="button" v-on:click="open_constants">{{translate('constants')}}</button>
        <div class="placeholder middle"></div>
        <button type="button" name="button" v-on:click="open_sensors">{{translate('sensors')}}</button>
        <div class="placeholder"></div>
      </div>
      <div class="btn logout" v-on:click="logout"></div>
      <checkbox class="manual font-20pt" v-bind:text="translate('plant manual')" v-bind:value="anlage_manuel" v-on:input="manuel"/>
      <div class="language">
        <p>{{translate('language' + ': ')}}</p>
        <button type="button" name="button" v-on:click="set_language(0)">{{translate('english')}}</button>
        <button type="button" name="button" v-on:click="set_language(1)">{{translate('german')}}</button>
        <button type="button" name="button" v-on:click="set_language(2)">{{translate('flemish')}}</button>

      </div>
    </div>
    <adminconstants v-bind:class="{'hide':!(panel==1)}" v-on:back="panel = 0" ref="adminconst"/>
    <adminsensors v-bind:class="{'hide':!(panel==2)}" v-on:back="panel = 0" ref="adminsensors"/>
  </div>
</template>
<script type="text/javascript">
import vue from 'vue'
import checkbox from './VueComponents/checkbox.vue'
import adminconstants from './adminconstants.vue'
import axios from 'axios'
import adminsensors from './adminsensoren.vue'

//import { v4 as uuidv4 } from 'uuid'


export default{
  name: 'adminpanel',
  components:{
    checkbox,
    adminsensors,
    adminconstants
  },
  methods:{
    set_language(to){
      vue.$language = to;
      vue.$cookies.set('language', to);
      this.$forceUpdate();
    },
    translate(text){
      return vue.$translate(text);
    },
    request_data(){
      this.$refs.adminconst.request_data()
    },
    logout(){
      vue.$admintoken = '';
    },
    open_constants(){
      this.panel = 1;
      this.$refs.adminconst.request_data()
    },
    open_sensors(){
      this.panel = 2
      this.$refs.adminsensors.open()
    },
    manuel(e){
      console.log('change');
      this.anlage_manuel = e;
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: 24,
          value: e
        }
      }).then(() => {console.log('acc')})
    }

  },
  show(){
    this.methods.request_data()
  },
  data(){
    return{
      panel: 0 /*0: uebersicht, 1:Konstanten, 2:Sensoren*/,
      anlage_manuel: false
    }
  },
  created(){
    axios({
      method: 'post',
      url: 'http://192.168.14.109:8000/getvalue',
      data: {
        id: 24,
      }
    }).then((e) => {this.anlage_manuel = e.data.value==1})
  }
}
</script>
<style media="screen">
  .header{
    display: flex;
    flex-direction: row;

  }
  .manual{
    flex: 1 0 0;
  }
  .btn{
    flex: 0 0 40pt;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    margin: 2pt;
  }
  .btn.refresh{
    background-image: url('./images/sync-solid.svg');
  }
  .btn.logout{
    background-image: url('./images/sign-out-alt-solid.svg');

  }
  .tablewrapper{
    overflow-y: scroll;
    height: 232pt;
  }
  .buttonwrapper{
    display: flex;
    flex-direction: row;
  }
  .buttonwrapper .placeholder{
    flex: 2 0 0;
  }
  .buttonwrapper .placeholder.middle{
    flex: 1 0 0;
  }
  .buttonwrapper button{
    flex: 0 0 auto;
  }
  .header p{
    font-size: 20pt;
  }
  .language button{
    margin: 0 10pt;
  }
</style>
