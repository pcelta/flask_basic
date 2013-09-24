
import config

class Loader(object):

    @staticmethod
    def get_by_main_key(key):
        if key in config.get_configs().keys():
            return config.get_configs()[key]
        return False
        
    @staticmethod
    def get_partner_settings(partner_name):
        partner_name = partner_name.upper()
        if partner_name in config.get_configs()['partners'] :
            return config.get_configs()['partners'][partner_name]
        pass
