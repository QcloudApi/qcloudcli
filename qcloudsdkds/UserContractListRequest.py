# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UserContractListRequest(Request):

    def __init__(self):
        super(UserContractListRequest, self).__init__(
            'ds', 'qcloudcliV1', 'UserContractList', 'ds.api.qcloud.com')

    def get_contractState(self):
        return self.get_params().get('contractState')

    def set_contractState(self, contractState):
        self.add_param('contractState', contractState)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_pageIndex(self):
        return self.get_params().get('pageIndex')

    def set_pageIndex(self, pageIndex):
        self.add_param('pageIndex', pageIndex)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)

    def get_userId(self):
        return self.get_params().get('userId')

    def set_userId(self, userId):
        self.add_param('userId', userId)
