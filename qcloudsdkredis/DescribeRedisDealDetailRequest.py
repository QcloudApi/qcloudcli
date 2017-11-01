# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRedisDealDetailRequest(Request):

    def __init__(self):
        super(DescribeRedisDealDetailRequest, self).__init__(
            'redis', 'qcloudcliV1', 'DescribeRedisDealDetail', 'redis.api.qcloud.com')

    def get_dealIds(self):
        return self.get_params().get('dealIds')

    def set_dealIds(self, dealIds):
        self.add_param('dealIds', dealIds)
