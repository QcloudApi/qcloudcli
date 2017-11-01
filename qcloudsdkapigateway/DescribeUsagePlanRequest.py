# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUsagePlanRequest(Request):

    def __init__(self):
        super(DescribeUsagePlanRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeUsagePlan', 'apigateway.api.qcloud.com')

    def get_usagePlanId(self):
        return self.get_params().get('usagePlanId')

    def set_usagePlanId(self, usagePlanId):
        self.add_param('usagePlanId', usagePlanId)
