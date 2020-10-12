import Vue from 'vue'
import App from './App.vue'
import { diconary } from './language.js'
Vue.use(require('vue-cookies'))
Vue.$cookies.config('7d')


Vue.$language = Vue.$cookies.get('language');
if(!Vue.$language){
  Vue.$language = 0; /* 0 = Englisch, 1 = Deutsch, 2 = Flämisch*/
  Vue.$cookies.set('language', 0);
}
Vue.$translate = (text)=>{
  if(!Vue.$language || Vue.$language == 0)
    return text;
  else{
    let add_on = ''
    if(text.includes(': '))
      add_on = ': '

    text = text.replace(': ', '')
    const word = diconary.find(e => e[0]==text);
    if(!word){
      console.log('no translation', text);
      return text + add_on;
    }else
      return word[Vue.$language] + add_on;
  }
}

const app = new Vue({
  render: h => h(App),
  components: {App},


}).$mount('#app')
app.uahl=0;
