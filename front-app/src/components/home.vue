<template>
  <div id="home">
    <div id="homeProfile">
      <h2>Maegaki</h2>
      <p>`to-base`は大野木俊樹のプロファイルや活動実績等をまとめた個人ページです。面白いものは特にありませんので、隠しコマンドを探すなどはしないでください。エラーによる鯖落ちの元です。</p>
    </div>
    <div id="homeUpdate">
      <h2>What's New</h2>
      <ul>
        <li><router-link to="/documents/sigmus/2018/wajima"><p>2018年11月の21日から22日にかけて行われる第121回SIGMUSポスターセッションのページをアップしました</p></router-link></li>
      </ul>
    </div>
    <div>
      <h2>Profile</h2>
      <table id="tableProfile">
        <col width="128"/>
        <tbody>
          <tr>
            <th>名前</th>
            <td>大野木 俊樹, Toshiki Ohnogi</td>
          </tr>
          <tr>
            <th>所属</th>
            <td>東京都市大学大学院環境情報学研究科2年<br />来年度より株式会社i-plugで新卒エンジニア</td>
          </tr>
          <tr>
            <th>研究</th>
            <td>DJの選曲方法に基づくプレイリスト生成に関する研究</td>
          </tr>
          <tr>
            <th>言語</th>
            <td>Python, Nim, JavaScript</td>
          </tr>
          <tr>
            <th>ツール等</th>
            <td>Django, ML-Library, Vue, React, Docker, MySQL, MongoDB</td>
          </tr>
          <tr>
            <th>趣味</th>
            <td>DJ, 競馬, プログラミング, 社会</td>
          </tr>
        </tbody>
      </table>
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
#tableProfile {
  width: 100%;
}
</style>
