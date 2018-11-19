<template>
  <div id="sigmusWajima">
    <div class="uk-container">
      <div class="org-container">
        <another-html
          :afterBaseUrl="afterBaseUrl"
        />
      </div>
    </div>
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
