# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeApiRequest(Request):

    def __init__(self):
        super(DescribeApiRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeApi', 'apigateway.api.qcloud.com')

    def get_apiId(self):
        return self.get_params().get('apiId')

    def set_apiId(self, apiId):
        self.add_param('apiId', apiId)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
