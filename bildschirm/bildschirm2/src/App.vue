<template>
  <div id="app">
    <schema ref="schema" v-bind:class="{'hide':!show_schema}"/>
    <adminpanel ref="adminpanel" v-bind:class="{'hide':!show_admin}"/>
    <menubar ref="menu" v-on:change-setting="change_setting"/>
    <loginpage :class="{'hide':!show_login}" open_at_start="true" hide_register="true" v-on:login="login" v-on:abort="close_login"/>
    <Keyboard :visible="this.needkeyboard" :input="input" @on-keypress="keypress" @on-change="inputchange" ref="keyboard"/>

  </div>
</template>

<script>
import schema from './components/schema.vue'
import menubar from './components/menubar.vue'
import adminpanel from './components/adminpanel.vue'
import loginpage from './components/loginpage.vue'
import Keyboard  from './components/SimpleKeyboard.vue'
import axios from 'axios'
import vue from 'vue'


export default {
  name: 'App',
  components: {
    schema,
    menubar,
    adminpanel,
     Keyboard, loginpage
  }, methods:{
    change_setting(value){
      console.log('change setting');
      this.$refs['schema'].$forceUpdate();
      this.$refs['adminpanel'].$forceUpdate();
      this.$refs['menu'].$forceUpdate();

      if (value) {
        this.show_schema = true;
        this.show_login = false;
        this.show_admin = false;
        return
      }else{
        this.show_schema = false;
        this.show_login = true;
        this.show_admin = false;
      }

      axios({
        method: 'post',
        url: 'http://192.168.14.109:8000/login',
        data: {
          email: vue.$user.email,
          password: vue.$user.password
        }
      }).then((e) => {
        if(e.data.token){
          this.show_schema = false;
          this.show_login = false;
          this.show_admin = true;
        }
        else{
          alert('Login Failed')
        }
      }).catch(e => alert(e));

      if(this.show_admin)
        this.$refs.adminpanel.request_data()
    },
    close_login(){
      this.$refs.menu.change_setting()
    },
    login(data){
      console.log(data);
      vue.$user = {email: data.email, password:data.password}
      this.change_setting(0)
    },
    keypress(e){
      if( e== '{enter}') vue.$closekeyboard()
    },
    inputchange(input){
      console.log('in app', input);
      vue.$keyboardinput(input)
    }
  },
  data(){
    return{
      show_schema: true,
      show_admin: false,
      show_login: false,
      needkeyboard: false,
      input: ''
    }
  }, created(){
    vue.$user = {email:'', password:''}

    vue.$openkeyboard = (my_input, my_input_cb, my_input_enter)=>{
      this.needkeyboard = true;

      if(my_input){
        this.$refs.keyboard.keyboard.setInput(my_input)
        this.inputchange = my_input_cb;
        vue.$keyboardenter = my_input_enter;
      }
        //this.$refs.keyboard.keyboard.onChange = (input) => {

    }
    vue.$closekeyboard = ()=>{
      this.needkeyboard = false;
      this.$refs.keyboard.keyboard.setInput('')
    }

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  position: absolute;
  top: 0;
  left: 0 ;
  width:100%;
  height: 100%;
}
.keyboardpadding{
  height: 250pt
}
.hide{
  display: none !important;
}
.button, button{
    background-color: #42b983;
    color: white;
    border: 0;
    border-radius: 20pt;
    height: 40pt;
    padding: 10pt;
    width: auto;
    cursor: pointer;
    font-size: 20pt;
}
</style>
