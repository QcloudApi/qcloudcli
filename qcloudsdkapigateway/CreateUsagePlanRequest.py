# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateUsagePlanRequest(Request):

    def __init__(self):
        super(CreateUsagePlanRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'CreateUsagePlan', 'apigateway.api.qcloud.com')

    def get_bindSecretIds(self):
        return self.get_params().get('bindSecretIds')

    def set_bindSecretIds(self, bindSecretIds):
        self.add_param('bindSecretIds', bindSecretIds)

    def get_maxRequestNumPreSec(self):
        return self.get_params().get('maxRequestNumPreSec')

    def set_maxRequestNumPreSec(self, maxRequestNumPreSec):
        self.add_param('maxRequestNumPreSec', maxRequestNumPreSec)

    def get_usagePlanDesc(self):
        return self.get_params().get('usagePlanDesc')

    def set_usagePlanDesc(self, usagePlanDesc):
        self.add_param('usagePlanDesc', usagePlanDesc)

    def get_usagePlanName(self):
        return self.get_params().get('usagePlanName')

    def set_usagePlanName(self, usagePlanName):
        self.add_param('usagePlanName', usagePlanName)
