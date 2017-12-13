# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AccountDeleteRequest(Request):

    def __init__(self):
        super(AccountDeleteRequest, self).__init__(
            'ds', 'qcloudcliV1', 'AccountDelete', 'ds.api.qcloud.com')

    def get_accountList(self):
        return self.get_params().get('accountList')

    def set_accountList(self, accountList):
        self.add_param('accountList', accountList)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
