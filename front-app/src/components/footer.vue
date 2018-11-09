<template>
  <div id="footerComponent">
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
