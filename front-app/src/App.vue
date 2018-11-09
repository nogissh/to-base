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
  background-color: #E6E6FA;
}

#app {
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
}
#mainColumn {
  padding: 8px;
}

p {
  margin: 0;
  padding: 0;
}
a {
  color: #9370DB;
}
</style>
