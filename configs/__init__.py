class CompileContainer:
  compile_dict = {
    'home'            : 'containers/home.html'
  }

  def get_home_path(self):
    return self.compile_dict['home']


compile_container = CompileContainer()
