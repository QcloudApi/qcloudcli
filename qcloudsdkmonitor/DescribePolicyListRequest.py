# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePolicyListRequest(Request):

    def __init__(self):
        super(DescribePolicyListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePolicyList', 'monitor.api.qcloud.com')

    def get_like(self):
        return self.get_params().get('like')

    def set_like(self, like):
        self.add_param('like', like)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_updateTimeOrder(self):
        return self.get_params().get('updateTimeOrder')

    def set_updateTimeOrder(self, updateTimeOrder):
        self.add_param('updateTimeOrder', updateTimeOrder)

    def get_viewNames(self):
        return self.get_params().get('viewNames')

    def set_viewNames(self, viewNames):
        self.add_param('viewNames', viewNames)
