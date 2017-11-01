# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLBWeightRequest(Request):

    def __init__(self):
        super(ModifyLBWeightRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ModifyLBWeight', 'lb.api.qcloud.com')

    def get_loadBalanceId(self):
        return self.get_params().get('loadBalanceId')

    def set_loadBalanceId(self, loadBalanceId):
        self.add_param('loadBalanceId', loadBalanceId)

    def get_weight(self):
        return self.get_params().get('weight')

    def set_weight(self, weight):
        self.add_param('weight', weight)
