<template>
  <div id="profile">
    <div class="uk-container">
      <div class="org-container">
        <div class="uk-card uk-card-default uk-card-body uk-margin-top">
          <h2>Profile</h2>
          <table id="tableProfile">
            <col width="96"/>
            <tbody>
              <tr>
                <th>名前</th>
                <td>大野木 俊樹, Toshiki Ohnogi</td>
              </tr>
              <tr>
                <th>生年月日</th>
                <td>1994年4月19日</td>
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
        <div class="uk-card uk-card-default uk-card-body uk-margin-top">
          <h2>Links</h2>
          <ul>
            <li><a href="https://twitter.com/toshikiohnogi" target="_blank">Twitter</a></li>
            <li><a href="https://github.com/toshikiohnogi" target="_blank">GitHub</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'profile'
}
</script>

<style>
th {
  text-align: left;
}
</style>
