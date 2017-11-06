# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ReleaseServiceRequest(Request):

    def __init__(self):
        super(ReleaseServiceRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'ReleaseService', 'apigateway.api.qcloud.com')

    def get_environmentName(self):
        return self.get_params().get('environmentName')

    def set_environmentName(self, environmentName):
        self.add_param('environmentName', environmentName)

    def get_releaseDesc(self):
        return self.get_params().get('releaseDesc')

    def set_releaseDesc(self, releaseDesc):
        self.add_param('releaseDesc', releaseDesc)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
