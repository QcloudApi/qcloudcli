# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class VcodeSendRequest(Request):

    def __init__(self):
        super(VcodeSendRequest, self).__init__(
            'ds', 'qcloudcliV1', 'VcodeSend', 'ds.api.qcloud.com')

    def get_contractResId(self):
        return self.get_params().get('contractResId')

    def set_contractResId(self, contractResId):
        self.add_param('contractResId', contractResId)

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
