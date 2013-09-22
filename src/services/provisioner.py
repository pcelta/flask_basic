class Provisioner(object):

    def activate(self, json):
        for order in json['orders'] :
            if 'partner' is not order :
                continue
            
            
        return True
