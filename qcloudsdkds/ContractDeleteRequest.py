# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractDeleteRequest(Request):

    def __init__(self):
        super(ContractDeleteRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractDelete', 'ds.api.qcloud.com')

    def get_contractNo(self):
        return self.get_params().get('contractNo')

    def set_contractNo(self, contractNo):
        self.add_param('contractNo', contractNo)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
