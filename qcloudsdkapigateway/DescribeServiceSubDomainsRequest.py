# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeServiceSubDomainsRequest(Request):

    def __init__(self):
        super(DescribeServiceSubDomainsRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeServiceSubDomains', 'apigateway.api.qcloud.com')

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
