# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class VcodeCheckRequest(Request):

    def __init__(self):
        super(VcodeCheckRequest, self).__init__(
            'ds', 'qcloudcliV1', 'VcodeCheck', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_userId(self):
        return self.get_params().get('userId')

    def set_userId(self, userId):
        self.add_param('userId', userId)

    def get_verifyCode(self):
        return self.get_params().get('verifyCode')

    def set_verifyCode(self, verifyCode):
        self.add_param('verifyCode', verifyCode)
