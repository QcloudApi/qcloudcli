# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBillsRequest(Request):

    def __init__(self):
        super(DescribeBillsRequest, self).__init__(
            'feecenter', 'qcloudcliV1', 'DescribeBills', 'feecenter.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_order(self):
        return self.get_params().get('order')

    def set_order(self, order):
        self.add_param('order', order)

    def get_payType(self):
        return self.get_params().get('payType')

    def set_payType(self, payType):
        self.add_param('payType', payType)

    def get_payerUin(self):
        return self.get_params().get('payerUin')

    def set_payerUin(self, payerUin):
        self.add_param('payerUin', payerUin)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
