# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RecordListRequest(Request):

    def __init__(self):
        super(RecordListRequest, self).__init__(
            'cns', 'qcloudcliV1', 'RecordList', 'cns.api.qcloud.com')

    def get_domain(self):
        return self.get_params().get('domain')

    def set_domain(self, domain):
        self.add_param('domain', domain)

    def get_length(self):
        return self.get_params().get('length')

    def set_length(self, length):
        self.add_param('length', length)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
