# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeServiceEnvironmentReleaseHistoryRequest(Request):

    def __init__(self):
        super(DescribeServiceEnvironmentReleaseHistoryRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeServiceEnvironmentReleaseHistory', 'apigateway.api.qcloud.com')

    def get_environmentName(self):
        return self.get_params().get('environmentName')

    def set_environmentName(self, environmentName):
        self.add_param('environmentName', environmentName)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
