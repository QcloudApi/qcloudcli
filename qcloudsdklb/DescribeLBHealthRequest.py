# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLBHealthRequest(Request):

    def __init__(self):
        super(DescribeLBHealthRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DescribeLBHealth', 'lb.api.qcloud.com')

    def get_loadBalanceId(self):
        return self.get_params().get('loadBalanceId')

    def set_loadBalanceId(self, loadBalanceId):
        self.add_param('loadBalanceId', loadBalanceId)
