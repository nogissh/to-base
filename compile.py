import os
from jinja2 import Environment, FileSystemLoader
from csscompressor import compress
from htmlmin import minify

PROFILE = [
  {
    'title': 'Name',
    'content': 'Toshiki Ohnogi'
  },
  {
    'title': 'Born',
    'content': 'Apr 19, 1994, Yokohama, Japan'
  },
  {
    'title': 'Title of Research',
    'content': 'DJの選曲方法に基づくプレイリスト生成に関する研究'
  },
  {
    'title': 'Programming Languages',
    'content': 'Python, Nim, JavaScript'
  },
  {
    'title': 'Tools',
    'content': 'Django, Vue, Docker'
  },
  {
    'title': 'Hobbies',
    'content': 'DJ, Horse Racing, Programming, Society'
  }
]

with open('static/css/style.css') as f:
  raw_css = f.read()
css = compress(raw_css)

env = Environment(loader=FileSystemLoader('./templates'))

template = env.get_template('containers/home.html')
html = template.render({
  'css'    : css,
  'profile': PROFILE
})

os.system('mkdir public')
os.system('cp -a static public/static')
with open('public/index.html', 'w', encoding='utf-8') as f:
  f.write(minify(html))
