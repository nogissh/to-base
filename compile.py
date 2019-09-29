import os
import shutil
from jinja2 import Environment, FileSystemLoader
from csscompressor import compress
from htmlmin import minify

from configs.profile import PROFILE as PROFILE_CONFIG
from configs.head import TEXT as HEAD_TEXT
from configs.note import TEXT as NOTE_TEXT

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
  'head_text' : HEAD_TEXT,
  'note_text' : NOTE_TEXT
})

os.system('mkdir public')
os.system('cp -a static public/static')
with open('public/index.html', 'w', encoding='utf-8') as f:
  html = minify(html)
  html = html.replace('> <', '><')
  f.write(html)
