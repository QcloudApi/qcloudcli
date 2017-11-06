# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BindSecretIdsRequest(Request):

    def __init__(self):
        super(BindSecretIdsRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'BindSecretIds', 'apigateway.api.qcloud.com')

    def get_secretIds(self):
        return self.get_params().get('secretIds')

    def set_secretIds(self, secretIds):
        self.add_param('secretIds', secretIds)

    def get_usagePlanId(self):
        return self.get_params().get('usagePlanId')

    def set_usagePlanId(self, usagePlanId):
        self.add_param('usagePlanId', usagePlanId)
