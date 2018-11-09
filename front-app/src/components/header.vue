<template>
  <div id="headerComponent">
    <div id="headerTitle">
      <h1 id="headerH1">{{ title }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'headerComponent',
  data () {
    return {
      title: 'Undifined'
    }
  }
}
</script>

<style>
#headerComponent {
  position: fixed;
  background-color: white;
  width: 100%;
  height: 50px;
  margin: 0;
  padding: 0;
  top: 0;
  left: 0;
  right: 0;
  border-bottom: 1px lightgray solid;
  box-sizing: border-box;
}
#headerTitle {
  margin: 8px;
}

#headerH1 {
  font-size: 22px;
  margin: 0;
  padding: 0;
}
</style>
