# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePolicyInfoRequest(Request):

    def __init__(self):
        super(DescribePolicyInfoRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePolicyInfo', 'monitor.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
