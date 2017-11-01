# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class PersonalAccountReactiveRequest(Request):

    def __init__(self):
        super(PersonalAccountReactiveRequest, self).__init__(
            'ds', 'qcloudcliV1', 'PersonalAccountReactive', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_userId(self):
        return self.get_params().get('userId')

    def set_userId(self, userId):
        self.add_param('userId', userId)
