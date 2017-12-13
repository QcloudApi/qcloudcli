# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AccountUpdateAutoRenewRequest(Request):

    def __init__(self):
        super(AccountUpdateAutoRenewRequest, self).__init__(
            'ds', 'qcloudcliV1', 'AccountUpdateAutoRenew', 'ds.api.qcloud.com')

    def get_accountList(self):
        return self.get_params().get('accountList')

    def set_accountList(self, accountList):
        self.add_param('accountList', accountList)

    def get_isAutoRenew(self):
        return self.get_params().get('isAutoRenew')

    def set_isAutoRenew(self, isAutoRenew):
        self.add_param('isAutoRenew', isAutoRenew)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
