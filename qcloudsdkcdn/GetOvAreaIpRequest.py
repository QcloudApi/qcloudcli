# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetOvAreaIpRequest(Request):

    def __init__(self):
        super(GetOvAreaIpRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetOvAreaIp', 'cdn.api.qcloud.com')

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)
