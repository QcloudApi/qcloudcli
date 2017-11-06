# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryVpnPriceRequest(Request):

    def __init__(self):
        super(InquiryVpnPriceRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'InquiryVpnPrice', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)
