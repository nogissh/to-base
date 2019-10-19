from .head import TEXT as head_text
from .note import TEXT as note_text
from .profile import PROFILE as profile_list


class HomeConfig:
  head_text = head_text
  note_text = note_text
  
  profile_list = profile_list

  def get_head_text(self):
    return self.head_text

  def get_note_text(self):
    return self.note_text

  def get_profile_list(self):
    return self.profile_list

  def get_params_as_dict(self):
    return {
      'head_text'    : self.get_head_text(),
      'note_text'    : self.get_note_text(),
      'profile_list' : self.get_profile_list()
    }


home_config_instance = HomeConfig()
