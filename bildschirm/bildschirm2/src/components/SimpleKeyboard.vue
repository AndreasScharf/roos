<template>
  <div :class="{'hide':!visible}" class="keyboardwrapper">
    <div class="simple-keyboard"></div>
  </div>
</template>

<script>
import Keyboard from "simple-keyboard";
import "simple-keyboard/build/css/index.css";
import vue from 'vue'

export default {
  name: "SimpleKeyboard",
  props: {
    keyboardClass: {
      default: "keyboard",
      type: String
    },
    input: {
      type: String
    },
    visible: Boolean
  },
  data: () => ({
    keyboard: null
  }),
  mounted() {
    this.keyboard = new Keyboard({
      onChange: this.onChange,
      onKeyPress: this.onKeyPress
    });
  },
  methods: {
    onChange(input) {
      this.$emit("on-change", input);
      
    },
    onKeyPress(button) {
      this.$emit("on-keypress", button);
      if (button == '{enter}')   vue.$keyboardenter();
      /**
       * If you want to handle the shift and caps lock buttons
       */
      if (button === "{shift}" || button === "{lock}") this.handleShift();
    },
    handleShift() {
      let currentLayout = this.keyboard.options.layoutName;
      let shiftToggle = currentLayout === "default" ? "shift" : "default";

      this.keyboard.setOptions({
        layoutName: shiftToggle
      });
    }
  },
  watch: {
    input(input) {
      this.keyboard.setInput(input);
    },
    visible(visible){
      if (!visible)
        this.keyboard.setInput('');

    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simple-keyboard{
  position: fixed;
  bottom: 0;
  z-index: 10;
  left: 0;
}
.hide{
  display: none !important;
}
</style>
