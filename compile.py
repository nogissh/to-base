import os
import shutil
from jinja2 import Environment, FileSystemLoader
from csscompressor import compress
from htmlmin import minify

from configs.profile import PROFILE as PROFILE_CONFIG
from configs.head import TEXT as TEXT_CONFIG

try:
  shutil.rmtree('./public')
except FileNotFoundError:
  print('No `./public` directory.')

with open('static/css/style.css') as f:
  raw_css = f.read()
css = compress(raw_css)

env = Environment(loader=FileSystemLoader('./templates'))

template = env.get_template('containers/home.html')
html = template.render({
  'css'       : css,
  'profile'   : PROFILE_CONFIG,
  'head_text' : TEXT_CONFIG
})

os.system('mkdir public')
os.system('cp -a static public/static')
with open('public/index.html', 'w', encoding='utf-8') as f:
  f.write(minify(html))
