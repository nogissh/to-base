<template>
  <div id="home">
    <div class="uk-container">
      <div class="org-container">
        <div id="homeProfile" class="uk-card uk-card-default uk-card-body uk-margin-top">
          <h2>Maegaki</h2>
          <p>ここは大野木俊樹のプロファイルや活動実績等をまとめた個人ページです。面白いものは特にありませんので、隠しコマンドを探すなどはしないでください。エラーによる鯖落ちの元です。</p>
        </div>
        <div id="homeUpdate" class="uk-card uk-card-default uk-card-body uk-margin-top">
          <h2>What's New</h2>
          <ul>
            <li><router-link to="/documents/master/experiment">修士研究の実験ページをアップしました。</router-link></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
}
</script>

<style>
#tableProfile {
  width: 100%;
}
</style>
