# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBillsRequest(Request):

    def __init__(self):
        super(DescribeBillsRequest, self).__init__(
            'bill', 'qcloudcliV1', 'DescribeBills', 'bill.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderType(self):
        return self.get_params().get('orderType')

    def set_orderType(self, orderType):
        self.add_param('orderType', orderType)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
