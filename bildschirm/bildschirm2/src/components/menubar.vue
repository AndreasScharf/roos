<template id="">
  <div class="menubar">
    <div class="wrapper">
      <div class="">
          <checkbox class="anlage_ein_aus font-20pt" v-bind:text="translate('plant running')" v-bind:value="anlage_ein_aus" color="white" v-on:input="anlage"/>
          <button type="button" name="button" v-on:click="reset">{{translate('reset')}}</button>
      </div>

    </div>

    <div class="enwat">
      <div class="logo">

      </div>
    </div>

    <div class="wrapper">
      <div class="placeholder"></div>
      <div class="change_setting " v-bind:class="{'to_settings': this.setting_schema, 'to_schema':!this.setting_schema}" v-on:click="change_setting">

      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
import vue from 'vue'
import axios from 'axios'
import checkbox from './VueComponents/checkbox.vue'

export default{
  name: 'menubar',
  components:{
    checkbox
  },
  methods:{
    translate(text){
      return vue.$translate(text);
    },
    reset(){
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/reset',
        data: {}
      }).then(() => {console.log('acc')})
    },
    click(e){
      this.status = e;
    },
    change_setting(){
      this.$forceUpdate();
      this.setting_schema = !this.setting_schema
      this.$emit('change-setting', this.setting_schema)
    },
    anlage(e){

      this.anlage_ein_aus = e;
      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/setvalue',
        data: {
          id: 1,
          value: e
        }
      }).then(() => {console.log('acc')})
    }

  },
  data(){
    return {
      status: 1,
      setting_schema: true,
      anlage_ein_aus: false
    }
  },created(){
    axios({
      method: 'post',
      url: 'http://192.168.14.109:8000/getvalue',
      data: {
        id: 1,
      }
    }).then((e) => {this.anlage_ein_aus = e.data.value==1})
  }
}
</script>
<style media="screen" >
  .menubar{
    display: flex;
    flex-direction: row;
    height: 20%;
    width: 100%;
    position: fixed;
    background-color: #293133;
    border-top: solid #293133 2pt;
    margin-top: -2pt;
    bottom: 0;
  }
  .enwat{
    flex: 1 0 0;
    background-color: white;
    padding: 4pt;
    display: flex;
  }
  .enwat .logo{
    flex: 1 0 0;
    margin: 2%;

    background-image: url('./images/logo_Enwat_small.png');
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
  }
  .wrapper{
    flex: 1 0 0;
    display: flex;
    flex-direction: row;
    margin-right: 10pt;
  }
  .anlage_ein_aus{
    margin: 4pt 0 ;
  }
  .anlage_ein_aus p{
    font-size: 20pt;
    margin: auto;
    color: white;
  }
  .placeholder{
    flex: 1 0 0;

  }
  .change_setting{
    flex: 1 0 0;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    margin: 10pt;
  }

  .change_setting.to_settings{
    background-image: url('./images/cog-solid.svg');


  }
  .change_setting.to_schema{
    background-image: url('./images/eye-regular.svg');

  }
</style>
