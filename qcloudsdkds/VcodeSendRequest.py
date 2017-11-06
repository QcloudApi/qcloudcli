# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class VcodeSendRequest(Request):

    def __init__(self):
        super(VcodeSendRequest, self).__init__(
            'ds', 'qcloudcliV1', 'VcodeSend', 'ds.api.qcloud.com')

    def get_isSendVoice(self):
        return self.get_params().get('isSendVoice')

    def set_isSendVoice(self, isSendVoice):
        self.add_param('isSendVoice', isSendVoice)

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
