# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CancelDealsRequest(Request):

    def __init__(self):
        super(CancelDealsRequest, self).__init__(
            'trade', 'qcloudcliV1', 'CancelDeals', 'trade.api.qcloud.com')

    def get_dealIds(self):
        return self.get_params().get('dealIds')

    def set_dealIds(self, dealIds):
        self.add_param('dealIds', dealIds)
