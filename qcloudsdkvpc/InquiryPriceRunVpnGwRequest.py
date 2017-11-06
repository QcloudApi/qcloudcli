# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryPriceRunVpnGwRequest(Request):

    def __init__(self):
        super(InquiryPriceRunVpnGwRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'InquiryPriceRunVpnGw', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_chargePrepaid(self):
        return self.get_params().get('chargePrepaid')

    def set_chargePrepaid(self, chargePrepaid):
        self.add_param('chargePrepaid', chargePrepaid)

    def get_chargeType(self):
        return self.get_params().get('chargeType')

    def set_chargeType(self, chargeType):
        self.add_param('chargeType', chargeType)
