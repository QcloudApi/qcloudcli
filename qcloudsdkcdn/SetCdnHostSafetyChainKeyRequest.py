# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetCdnHostSafetyChainKeyRequest(Request):

    def __init__(self):
        super(SetCdnHostSafetyChainKeyRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'SetCdnHostSafetyChainKey', 'cdn.api.qcloud.com')

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_key(self):
        return self.get_params().get('key')

    def set_key(self, key):
        self.add_param('key', key)

    def get_tmplName(self):
        return self.get_params().get('tmplName')

    def set_tmplName(self, tmplName):
        self.add_param('tmplName', tmplName)
