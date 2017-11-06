# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaHttpsHostListRequest(Request):

    def __init__(self):
        super(GetDsaHttpsHostListRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaHttpsHostList', 'dsa.api.qcloud.com')

    def get_length(self):
        return self.get_params().get('length')

    def set_length(self, length):
        self.add_param('length', length)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
