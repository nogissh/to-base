<template>
  <div id="home">
    <div id="homeProfile">
      <h2>まえがき</h2>
      <p>`to-base`は大野木俊樹のプロファイルや活動実績等をまとめた個人ページです。面白いものは特にありませんので、隠しコマンドを探すなどはしないでください。エラーによる鯖落ちの元です。</p>
    </div>
    <div id="homeUpdate">
      <h2>What's New</h2>
      <ul>
        <li><router-link to="/documents/sigmus/2018/wajima"><p>2018年11月の21日から22日にかけて行われる第121回SIGMUSポスターセッションのページをアップしました</p></router-link></li>
      </ul>
    </div>
    <div>
      <h2>Links</h2>
      <ul>
        <li
          v-for="link in links"
          :key="link.name"
        ><a :href="link.url" target="_blank">{{ link.name }}</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      links: [
        {
          name: 'Twitter',
          url : 'https://twitter.com/toshikiohnogi'
        },
        {
          name: 'GitHub',
          url : 'https://github.com/toshikiohnogi'
        }
      ]
    }
  }
}
</script>

<style>

</style>
