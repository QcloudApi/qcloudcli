# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SealQueryRequest(Request):

    def __init__(self):
        super(SealQueryRequest, self).__init__(
            'ds', 'qcloudcliV1', 'SealQuery', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_sealId(self):
        return self.get_params().get('sealId')

    def set_sealId(self, sealId):
        self.add_param('sealId', sealId)

    def get_userId(self):
        return self.get_params().get('userId')

    def set_userId(self, userId):
        self.add_param('userId', userId)
