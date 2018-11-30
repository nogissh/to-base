<template>
  <div id="masterExperiment">
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
  name: 'masterExperiment',
  components: {
    anotherHtml: anotherHtml
  },
  data () {
    return {
      afterBaseUrl: 'extention/html/documents/master/experiment/'
    }
  }
}
</script>

<style>

</style>
