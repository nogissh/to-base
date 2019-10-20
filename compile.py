import os
import shutil

from jinja2 import Environment, FileSystemLoader
from csscompressor import compress as css_minifier
from jsmin import jsmin as js_minifier
from htmlmin import minify as html_minifier

from configs import compile_container
from configs.home import home_config_instance


class BaseCssCompiler:
  def __init__(self, file_path):
    self._file_path = file_path

  def get_file_path(self):
    return self._file_path
  
  def set_file_path(self, file_path):
    self._file_path = file_path

  def read_raw_css_text(self):
    with open(self.get_file_path()) as f:
      raw_css_text = f.read()
    return raw_css_text
  
  def minify(self):
    return css_minifier(self.read_raw_css_text())


class BaseMultiCssCompiler:
  def __init__(self, compiler_list):
    if type(compiler_list) is not list:
      raise TypeError('list型のみ代入可能です。')
    self._compiler_list = compiler_list

  def get_compiler_list(self):
    return self._compiler_list
  
  def stick(self):
    string = ''
    for compiler in self.get_compiler_list():
      string += compiler.minify()
    
    return string


class BaseJavaScriptCompile:
  def __init__(self, file_path):
    self._file_path = file_path

  def get_file_path(self):
    return self._file_path
  
  def set_file_path(self, file_path):
    self._file_path = file_path

  def read_raw_js_text(self):
    with open(self.get_file_path()) as f:
      raw_js_text = f.read()
    return raw_js_text
  
  def minify(self):
    return js_minifier(self.read_raw_js_text(), quote_chars="'\"`")


class BaseMultiJavaScriptCompiler:
  def __init__(self, compiler_list):
    if type(compiler_list) is not list:
      raise TypeError('list型のみ代入可能です。')
    self._compiler_list = compiler_list

  def get_compiler_list(self):
    return self._compiler_list
  
  def stick(self):
    script = ''
    for compiler in self.get_compiler_list():
      script += compiler.minify()
    
    return script


class BaseHtmlCompiler:
  def __init__(self, environment):
    self._env      = environment
  
  def get_file_path(self):
    return self._file_path
  
  def get_save_path(self):
    return self._save_path

  def get_template(self):
    return self._env.get_template(self.get_file_path())
  
  def get_params(self):
    return self._params

  def set_file_path(self, file_path):
    if type(file_path) is not str:
      raise TypeError('str型のみ代入可能です。')
    self._file_path = file_path

  def set_save_path(self, save_path):
    if type(save_path) is not str:
      raise TypeError('str型のみ代入可能です。')
    self._save_path = save_path

  def set_params(self, params):
    if type(params) is not dict:
      raise TypeError('dict型のみ代入可能です。')
    self._params = params
  
  def rendering(self):
    return (self.get_template()).render(self.get_params())
  
  def get_minified_html(self):
    minified = html_minifier(self.rendering())
    minified = minified.replace('> <', '><')

    return minified
  
  def dump_html(self):
    with open(self.get_save_path(), 'w', encoding='utf-8') as f:
      f.write(self.get_minified_html())

  def compile(self, container_path, save_path, params=None):
    self.set_file_path(container_path)
    self.set_save_path(save_path)

    if params is None:
      params = {}
    self.set_params(params)

    self.dump_html()


class BaseHtmlCssCompiler(BaseHtmlCompiler):
  def __init__(self, multi_css_compiler, environment):
    self.multi_css_compiler = multi_css_compiler
    self._env = environment

  def set_multi_css_compiler(self, multi_css_compiler):
    self.multi_css_compiler = multi_css_compiler

  def get_minified_css(self):
    return self.multi_css_compiler.stick()

  def combine_params_css(self, params, css):
    params['css'] = css
    return params

  def rendering(self):
    template = self.get_template()

    return template.render(
      self.combine_params_css(
        self.get_params(),
        self.get_minified_css()
      )
    )


class BaseHtmlJsCompiler(BaseHtmlCompiler):
  def __init__(self, multi_js_compiler, environment):
    self.multi_js_compiler = multi_js_compiler
    self._env = environment

  def set_multi_js_compiler(self, multi_js_compiler):
    self.multi_js_compiler = multi_js_compiler

  def get_minified_js(self):
    return self.multi_js_compiler.stick()

  def combine_params_js(self, params, js):
    params['js'] = js
    return params

  def rendering(self):
    template = self.get_template()

    return template.render(
      self.combine_params_js(
        self.get_params(),
        self.get_minified_js()
      )
    )


class BaseHtmlCssMultijsCompiler(BaseHtmlCssCompiler, BaseHtmlJsCompiler):
  def __init__(self, multi_css_compiler, multi_js_compiler, environment):
    self.multi_css_compiler = multi_css_compiler
    self.multi_js_compiler  = multi_js_compiler
    self._env = environment

  def combine_params_css_js(self, params, css, js):
    params = self.combine_params_css(params, css)
    params = self.combine_params_js(params, js)
    return params

  def rendering(self):
    template = self.get_template()

    return template.render(
      self.combine_params_css_js(
        self.get_params(),
        self.get_minified_css(),
        self.get_minified_js()
      )
    )


class StyleCssCompiler(BaseCssCompiler):
  pass


class MultiCssCompiler(BaseMultiCssCompiler):
  pass


class GoogleAnalyticsCompiler(BaseJavaScriptCompile):
  pass


class MultiJavaScriptCompiler(BaseMultiJavaScriptCompiler):
  pass


class HtmlCompiler(BaseHtmlCssMultijsCompiler):
  @classmethod
  def factory(
    cls,
    css_compiler_instance,
    js_compiler_instance,
    environment
  ):
    return cls(
      css_compiler_instance,
      js_compiler_instance,
      environment
    )


try:
  shutil.rmtree('./public')
except FileNotFoundError:
  print('No `./public` directory.')

os.mkdir('public')
os.system('cp -a static public/static')

html_compiler = HtmlCompiler.factory(
  MultiCssCompiler([StyleCssCompiler('static/css/style.css')]),
  MultiJavaScriptCompiler([GoogleAnalyticsCompiler('static/js/google_analytics.js')]),
  Environment(loader=FileSystemLoader('./templates'))
)

html_compiler.compile(
  compile_container.get_home_path(),
  'public/index.html',
  home_config_instance.get_params_as_dict()
)

os.mkdir('public/events')
html_compiler.compile(
  compile_container.get_tcu_workshop_oct_2019(),
  'public/events/tcu_workshop_oct_2019.html'
)
