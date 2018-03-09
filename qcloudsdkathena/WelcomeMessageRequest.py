# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class WelcomeMessageRequest(Request):

    def __init__(self):
        super(WelcomeMessageRequest, self).__init__(
            'athena', 'qcloudcliV1', 'WelcomeMessage', 'athena.api.qcloud.com')

    def get_AccessChannelCode(self):
        return self.get_params().get('AccessChannelCode')

    def set_AccessChannelCode(self, AccessChannelCode):
        self.add_param('AccessChannelCode', AccessChannelCode)

    def get_InstanceId(self):
        return self.get_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_param('InstanceId', InstanceId)
