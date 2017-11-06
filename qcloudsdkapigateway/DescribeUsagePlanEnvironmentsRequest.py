# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUsagePlanEnvironmentsRequest(Request):

    def __init__(self):
        super(DescribeUsagePlanEnvironmentsRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeUsagePlanEnvironments', 'apigateway.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_usagePlanId(self):
        return self.get_params().get('usagePlanId')

    def set_usagePlanId(self, usagePlanId):
        self.add_param('usagePlanId', usagePlanId)
