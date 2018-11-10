<template>
  <div id="app">
    <header>
      <header-component />
    </header>
    <div id="container">
      <div id="mainColumn">
        <router-view/>
      </div>
    </div>
    <footer>
      <footer-component />
    </footer>
  </div>
</template>

<script>
import headerComponent from '@/components/header'
import footerComponent from '@/components/footer'

export default {
  name: 'app',
  components: {
    headerComponent: headerComponent,
    footerComponent: footerComponent
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  background-color: #f5f5f5;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: black;
  font-size: 16px;
  width: 100%;
  margin: 0;
  padding: 0;
}
#container {
  background-color: white;
  width: 100%;
  max-width: 720px;
  max-block-size: 960px;
  margin: 0 auto;
  margin-top: 60px;
  padding: 0;
  border: 0;
  border-radius: 3px;
  box-shadow: 0 2px 2px 1px lightgray;
}
#mainColumn {
  padding: 1% 3%;
}

p {
  margin: 0;
  padding: 0;
}
a {
  color: #9370DB;
}
ul {
  padding-inline-start: 30px;
}
</style>
