<template>
  <div id="footerComponent" class="uk-margin-top">
    <router-link to="/">
      <p id="footerBackToHome">ホームへ戻る</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'footerComponent',
}
</script>

<style>
#footerComponent {
  text-align: center;
  height: 80px;
}
</style>
