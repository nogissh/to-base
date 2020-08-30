from .profile import PROFILE as profile_list


class HomeConfig:
  profile_list = profile_list

  def get_profile_list(self):
    return self.profile_list

  def get_params_as_dict(self):
    return {
      'profile_list' : self.get_profile_list()
    }


home_config_instance = HomeConfig()
