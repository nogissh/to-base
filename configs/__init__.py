class CompileContainer:
  compile_dict = {
    'home'            : 'containers/home.html',
    'tcu_ws_oct_2019' : 'containers/tcu_workshop_oct_2019.html'
  }

  def get_home_path(self):
    return self.compile_dict['home']
  
  def get_tcu_workshop_oct_2019(self):
    return self.compile_dict['tcu_ws_oct_2019']


compile_container = CompileContainer()
