<template>
  <div id="headerComponent">
    <nav class="uk-navbar" uk-navbar>
      <div class="uk-navbar-center">
        <ul class="uk-navbar-nav uk-hidden-small">
          <li class="uk-parent"><router-link to="/">Home</router-link></li>
          <li class="uk-parent" style="margin-right: 17px;"><router-link to="/profile">Profile</router-link></li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'headerComponent',
  data () {
    return {
      title: 'to-base'
    }
  }
}
</script>

<style>
#headerComponent {
  text-align: center;
  background-color: white;
  width: 100%;
  margin: 0;
  padding: 0;
  top: 0;
  left: 0;
  right: 0;
  border-bottom: 1px lightgray solid;
  box-sizing: border-box;
}
#headerTitle {
  padding: 8px;
}

#headerH1 {
  font-size: 22px;
  margin: 0;
  padding: 0;
}
</style>
