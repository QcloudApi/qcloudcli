# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateServiceRequest(Request):

    def __init__(self):
        super(UpdateServiceRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'UpdateService', 'apigateway.api.qcloud.com')

    def get_environmentName(self):
        return self.get_params().get('environmentName')

    def set_environmentName(self, environmentName):
        self.add_param('environmentName', environmentName)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_updateDesc(self):
        return self.get_params().get('updateDesc')

    def set_updateDesc(self, updateDesc):
        self.add_param('updateDesc', updateDesc)

    def get_versionName(self):
        return self.get_params().get('versionName')

    def set_versionName(self, versionName):
        self.add_param('versionName', versionName)
