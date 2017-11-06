# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeDealsByCondRequest(Request):

    def __init__(self):
        super(DescribeDealsByCondRequest, self).__init__(
            'trade', 'qcloudcliV1', 'DescribeDealsByCond', 'trade.api.qcloud.com')

    def get_dealId(self):
        return self.get_params().get('dealId')

    def set_dealId(self, dealId):
        self.add_param('dealId', dealId)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)
