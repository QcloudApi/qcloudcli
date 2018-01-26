# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BindSubDomainRequest(Request):

    def __init__(self):
        super(BindSubDomainRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'BindSubDomain', 'apigateway.api.qcloud.com')

    def get_certificateId(self):
        return self.get_params().get('certificateId')

    def set_certificateId(self, certificateId):
        self.add_param('certificateId', certificateId)

    def get_isDefaultMapping(self):
        return self.get_params().get('isDefaultMapping')

    def set_isDefaultMapping(self, isDefaultMapping):
        self.add_param('isDefaultMapping', isDefaultMapping)

    def get_pathMappingSet(self):
        return self.get_params().get('pathMappingSet')

    def set_pathMappingSet(self, pathMappingSet):
        self.add_param('pathMappingSet', pathMappingSet)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_subDomain(self):
        return self.get_params().get('subDomain')

    def set_subDomain(self, subDomain):
        self.add_param('subDomain', subDomain)
