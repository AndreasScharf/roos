<template id="">
  <div class="row" v-bind:class="{'head': header}">
    <div class="id">
      {{data.id}}
    </div>
    <div class="seperator"></div>
    <div class="name">
      {{translate(data.name)}}
    </div>
    <div class="seperator"></div>

    <div class="value" >
      <a v-bind:class="{'hide':this.edit}"  v-on:click="go_edit">{{this.data_value}}</a>
      <input :class="{'hide':!this.edit}"
        :value="input"
        type="text"
        ref="input"
        v-on:keyup.enter="enter"
        >
    </div>
    <div class="seperator"></div>

    <div class="comment">
      {{translate(data.comment)}}
    </div>

  </div>
</template>
<script type="text/javascript">
import axios from 'axios'
import vue from 'vue'


  export default{
    name: 'valuerow', components: {  },
    props:{data:Object, header:Boolean},
    methods:{
      translate(text){
        return vue.$translate(text)
      },
      go_edit(){
        this.edit = !this.header;
        this.$emit('edit', this.edit)
        this.input = this.data_value
        this.$forceUpdate()

        vue.$openkeyboard()
        vue.$keyboardenter = () =>{
          vue.$closekeyboard();
          this.edit = true;
          this.enter()
        }
        vue.$keyboardinput = (input)=>{
          this.input = input
        }
      },
      enter(){
        this.data_value = this.input;
        this.edit = false
        this.$emit('edit', this.edit)

        this.$forceUpdate()

        axios({
          method: 'post',
          url: 'http://192.168.14.109:8000/setvalue',
          data: {
            id: this.data.id,
            value: this.data_value
          }
        }).then(() => {console.log('acc', this.edit)})


      }
    },
    data(){
      return{
        edit: false,
        data_value: '',
        input: ''
      }
    },
    created(){
      this.data_value = this.data.value


    },
    updated(){
      this.$nextTick(()=> {
        if(this.edit)
          this.$refs.input.focus()
      });
    }
  }

</script>
<style media="screen">
  .row{
    display: flex;
    flex-direction: row;

    font-size: 20pt;
  }
  .row.head{
    font-weight: bold;
  }
  .row .id{
    flex: 1 0 0;
  }
  .row .name{
    flex: 3 0 0
  }
  .row .value{
    flex: 2 0 0;
    display: flex;

  }
  .row .value a{
    margin: auto;
    width: 130pt;

  }
  .row .value input{
    flex: 1 0 0;
    margin: 0 2pt;
  }
  .row .comment{
    flex: 3 0 0 ;
  }
  .seperator{
    flex: 0 0 2pt;
    background-color: #293133;

  }
  .keyboard{
    position: fixed;
    bottom: 0;
    z-index: 10;
    left: 0;
  }
</style>
