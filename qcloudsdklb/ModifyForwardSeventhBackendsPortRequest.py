# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyForwardSeventhBackendsPortRequest(Request):

    def __init__(self):
        super(ModifyForwardSeventhBackendsPortRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ModifyForwardSeventhBackendsPort', 'lb.api.qcloud.com')

    def get_backends(self):
        return self.get_params().get('backends')

    def set_backends(self, backends):
        self.add_param('backends', backends)

    def get_domain(self):
        return self.get_params().get('domain')

    def set_domain(self, domain):
        self.add_param('domain', domain)

    def get_listenerId(self):
        return self.get_params().get('listenerId')

    def set_listenerId(self, listenerId):
        self.add_param('listenerId', listenerId)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_locationIds(self):
        return self.get_params().get('locationIds')

    def set_locationIds(self, locationIds):
        self.add_param('locationIds', locationIds)

    def get_url(self):
        return self.get_params().get('url')

    def set_url(self, url):
        self.add_param('url', url)
