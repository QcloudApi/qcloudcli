# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeServiceSubDomainMappingsRequest(Request):

    def __init__(self):
        super(DescribeServiceSubDomainMappingsRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeServiceSubDomainMappings', 'apigateway.api.qcloud.com')

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_subDomain(self):
        return self.get_params().get('subDomain')

    def set_subDomain(self, subDomain):
        self.add_param('subDomain', subDomain)
