# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListInstanceRequest(Request):

    def __init__(self):
        super(ListInstanceRequest, self).__init__(
            'mqiot', 'qcloudcliV1', 'ListInstance', 'mqiot.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_searchWord(self):
        return self.get_params().get('searchWord')

    def set_searchWord(self, searchWord):
        self.add_param('searchWord', searchWord)
