# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingLimitRequest(Request):

    def __init__(self):
        super(DescribeScalingLimitRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingLimit', 'scaling.api.qcloud.com')

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
