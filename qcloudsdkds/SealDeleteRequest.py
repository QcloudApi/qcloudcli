# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SealDeleteRequest(Request):

    def __init__(self):
        super(SealDeleteRequest, self).__init__(
            'ds', 'qcloudcliV1', 'SealDelete', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_resid(self):
        return self.get_params().get('resid')

    def set_resid(self, resid):
        self.add_param('resid', resid)

    def get_sealId(self):
        return self.get_params().get('sealId')

    def set_sealId(self, sealId):
        self.add_param('sealId', sealId)
