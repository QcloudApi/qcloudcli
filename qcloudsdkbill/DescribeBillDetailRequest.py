# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBillDetailRequest(Request):

    def __init__(self):
        super(DescribeBillDetailRequest, self).__init__(
            'bill', 'qcloudcliV1', 'DescribeBillDetail', 'bill.api.qcloud.com')

    def get_billId(self):
        return self.get_params().get('billId')

    def set_billId(self, billId):
        self.add_param('billId', billId)

    def get_billType(self):
        return self.get_params().get('billType')

    def set_billType(self, billType):
        self.add_param('billType', billType)

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
