import axios from 'axios'

var url = 'https://api.toshikiohnogi.net/'
// var url = 'http://localhost:8000/'

export default axios.create({
  baseURL: url
})
