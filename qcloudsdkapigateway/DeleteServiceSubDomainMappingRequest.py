# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteServiceSubDomainMappingRequest(Request):

    def __init__(self):
        super(DeleteServiceSubDomainMappingRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DeleteServiceSubDomainMapping', 'apigateway.api.qcloud.com')

    def get_environment(self):
        return self.get_params().get('environment')

    def set_environment(self, environment):
        self.add_param('environment', environment)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_subDomain(self):
        return self.get_params().get('subDomain')

    def set_subDomain(self, subDomain):
        self.add_param('subDomain', subDomain)
