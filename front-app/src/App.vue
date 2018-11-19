<template>
  <div id="app">
    <header>
      <header-component />
    </header>
    <content>
      <router-view/>
    </content>
    <footer>
      <footer-component />
    </footer>
  </div>
</template>

<script>
import headerComponent from '@/components/header'
import footerComponent from '@/components/footer'
import contentComponent from '@/components/content'

export default {
  name: 'app',
  components: {
    headerComponent: headerComponent,
    footerComponent: footerComponent,
    contentComponent: contentComponent,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

html {
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
