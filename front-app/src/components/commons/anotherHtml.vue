<template>
  <div class="anotherHtml" v-html="html"></div>
</template>

<script>
import axios from '@/api'

export default {
  name: 'anotherHtml',
  props: [
    'afterBaseUrl'
  ],
  data () {
    return {
      html: null
    }
  },
  mounted () {
    axios
      .get(this.afterBaseUrl)
      .then((response) => {
        this.html = response.data
      })
      .catch((e) => {
        alert(e)
      })
  }
}
</script>

<style>
h1 {
  font-size: 22px;
}
h2 {
  font-size: 20px;
}
h3 {
  font-size: 18px;
}
</style>
