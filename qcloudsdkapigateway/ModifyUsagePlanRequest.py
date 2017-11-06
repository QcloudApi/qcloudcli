# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyUsagePlanRequest(Request):

    def __init__(self):
        super(ModifyUsagePlanRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'ModifyUsagePlan', 'apigateway.api.qcloud.com')

    def get_maxRequestNumPreSec(self):
        return self.get_params().get('maxRequestNumPreSec')

    def set_maxRequestNumPreSec(self, maxRequestNumPreSec):
        self.add_param('maxRequestNumPreSec', maxRequestNumPreSec)

    def get_usagePlanDesc(self):
        return self.get_params().get('usagePlanDesc')

    def set_usagePlanDesc(self, usagePlanDesc):
        self.add_param('usagePlanDesc', usagePlanDesc)

    def get_usagePlanId(self):
        return self.get_params().get('usagePlanId')

    def set_usagePlanId(self, usagePlanId):
        self.add_param('usagePlanId', usagePlanId)

    def get_usagePlanName(self):
        return self.get_params().get('usagePlanName')

    def set_usagePlanName(self, usagePlanName):
        self.add_param('usagePlanName', usagePlanName)
