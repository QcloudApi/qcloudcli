# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractCountQueryRequest(Request):

    def __init__(self):
        super(ContractCountQueryRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractCountQuery', 'ds.api.qcloud.com')

    def get_beginTime(self):
        return self.get_params().get('beginTime')

    def set_beginTime(self, beginTime):
        self.add_param('beginTime', beginTime)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
