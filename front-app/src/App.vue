<template>
  <div id="app">
    <header>
      <header-component />
    </header>
    <div id="body">
      <router-view/>
    </div>
  </div>
</template>

<script>
import headerComponent from '@/components/header'

export default {
  name: 'app',
  components: {
    headerComponent: headerComponent
  }
}
</script>

<style>
body {
  background-color: #E6E6FA;
}

#app {
  color: black;
  font-size: 16px;
  width: 100%;
  margin: 0;
  padding: 0;
}
#body {
  background-color: white;
  width: 100%;
  max-width: 1180px;
  max-block-size: 960px;
  margin: 0 auto;
  margin-top: 60px;
  padding: 0;
  border: 0;
  border-radius: 3px;
}

a {
  color: #9370DB;
}
</style>
