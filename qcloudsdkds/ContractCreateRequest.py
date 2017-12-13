# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractCreateRequest(Request):

    def __init__(self):
        super(ContractCreateRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractCreate', 'ds.api.qcloud.com')

    def get_contractName(self):
        return self.get_params().get('contractName')

    def set_contractName(self, contractName):
        self.add_param('contractName', contractName)

    def get_contractTextValue(self):
        return self.get_params().get('contractTextValue')

    def set_contractTextValue(self, contractTextValue):
        self.add_param('contractTextValue', contractTextValue)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_signInfos(self):
        return self.get_params().get('signInfos')

    def set_signInfos(self, signInfos):
        self.add_param('signInfos', signInfos)

    def get_templateResId(self):
        return self.get_params().get('templateResId')

    def set_templateResId(self, templateResId):
        self.add_param('templateResId', templateResId)
