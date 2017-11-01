# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaHostInfoRequest(Request):

    def __init__(self):
        super(GetDsaHostInfoRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaHostInfo', 'dsa.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)
