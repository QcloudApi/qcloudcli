# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UnReleaseServiceRequest(Request):

    def __init__(self):
        super(UnReleaseServiceRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'UnReleaseService', 'apigateway.api.qcloud.com')

    def get_environmentName(self):
        return self.get_params().get('environmentName')

    def set_environmentName(self, environmentName):
        self.add_param('environmentName', environmentName)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_unReleaseDesc(self):
        return self.get_params().get('unReleaseDesc')

    def set_unReleaseDesc(self, unReleaseDesc):
        self.add_param('unReleaseDesc', unReleaseDesc)
