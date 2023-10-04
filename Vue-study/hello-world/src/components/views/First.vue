<template>
    <div class="first-app">
        {{msg}}
        <confirm text="注册" @message="getMessage"></confirm>
    </div>
</template>

<script>
import Confirm from '../sub/Confirm.vue'
export default {
  components: { Confirm },
  name: 'First',
  data () {
    return {
      msg: 'Welcome to First!       皮皮橙'
    }
  },
  methods: {
    getMessage (val) {
      alert(val)
    }
  }
}
</script>
<style>

</style>
