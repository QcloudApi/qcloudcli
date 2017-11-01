# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UnBindSubDomainRequest(Request):

    def __init__(self):
        super(UnBindSubDomainRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'UnBindSubDomain', 'apigateway.api.qcloud.com')

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_subDomain(self):
        return self.get_params().get('subDomain')

    def set_subDomain(self, subDomain):
        self.add_param('subDomain', subDomain)
