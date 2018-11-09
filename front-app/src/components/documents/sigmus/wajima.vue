<template>
  <div id="sigmusWajima">
    <another-html
      :afterBaseUrl="afterBaseUrl"
    />
  </div>
</template>

<script>
import anotherHtml from '@/components/commons/anotherHtml'

export default {
  name: 'sigmusWajima',
  components: {
    anotherHtml: anotherHtml
  },
  data () {
    return {
      afterBaseUrl: 'extention/html/documents/sigmus/2018/wajima/'
    }
  }
}
</script>

<style>

</style>
