# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaHostListRequest(Request):

    def __init__(self):
        super(GetDsaHostListRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaHostList', 'dsa.api.qcloud.com')

    def get_includeDeleted(self):
        return self.get_params().get('includeDeleted')

    def set_includeDeleted(self, includeDeleted):
        self.add_param('includeDeleted', includeDeleted)

    def get_length(self):
        return self.get_params().get('length')

    def set_length(self, length):
        self.add_param('length', length)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
