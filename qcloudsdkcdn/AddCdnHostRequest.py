# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddCdnHostRequest(Request):

    def __init__(self):
        super(AddCdnHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'AddCdnHost', 'cdn.api.qcloud.com')

    def get_advancedCache(self):
        return self.get_params().get('advancedCache')

    def set_advancedCache(self, advancedCache):
        self.add_param('advancedCache', advancedCache)

    def get_cache(self):
        return self.get_params().get('cache')

    def set_cache(self, cache):
        self.add_param('cache', cache)

    def get_cacheMode(self):
        return self.get_params().get('cacheMode')

    def set_cacheMode(self, cacheMode):
        self.add_param('cacheMode', cacheMode)

    def get_cnameHost(self):
        return self.get_params().get('cnameHost')

    def set_cnameHost(self, cnameHost):
        self.add_param('cnameHost', cnameHost)

    def get_fwdHost(self):
        return self.get_params().get('fwdHost')

    def set_fwdHost(self, fwdHost):
        self.add_param('fwdHost', fwdHost)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_hostType(self):
        return self.get_params().get('hostType')

    def set_hostType(self, hostType):
        self.add_param('hostType', hostType)

    def get_origin(self):
        return self.get_params().get('origin')

    def set_origin(self, origin):
        self.add_param('origin', origin)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_serviceType(self):
        return self.get_params().get('serviceType')

    def set_serviceType(self, serviceType):
        self.add_param('serviceType', serviceType)
