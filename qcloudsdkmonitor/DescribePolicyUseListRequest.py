# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePolicyUseListRequest(Request):

    def __init__(self):
        super(DescribePolicyUseListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePolicyUseList', 'monitor.api.qcloud.com')

    def get_dimensions(self):
        return self.get_params().get('dimensions')

    def set_dimensions(self, dimensions):
        self.add_param('dimensions', dimensions)

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
