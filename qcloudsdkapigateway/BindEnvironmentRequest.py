# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BindEnvironmentRequest(Request):

    def __init__(self):
        super(BindEnvironmentRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'BindEnvironment', 'apigateway.api.qcloud.com')

    def get_environment(self):
        return self.get_params().get('environment')

    def set_environment(self, environment):
        self.add_param('environment', environment)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_usagePlanIds(self):
        return self.get_params().get('usagePlanIds')

    def set_usagePlanIds(self, usagePlanIds):
        self.add_param('usagePlanIds', usagePlanIds)
