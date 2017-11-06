# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeServiceUsagePlanRequest(Request):

    def __init__(self):
        super(DescribeServiceUsagePlanRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeServiceUsagePlan', 'apigateway.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_searchEnvironment(self):
        return self.get_params().get('searchEnvironment')

    def set_searchEnvironment(self, searchEnvironment):
        self.add_param('searchEnvironment', searchEnvironment)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
