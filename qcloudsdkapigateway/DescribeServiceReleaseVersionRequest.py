# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeServiceReleaseVersionRequest(Request):

    def __init__(self):
        super(DescribeServiceReleaseVersionRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeServiceReleaseVersion', 'apigateway.api.qcloud.com')

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
