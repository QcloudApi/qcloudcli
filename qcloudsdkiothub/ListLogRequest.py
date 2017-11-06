# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListLogRequest(Request):

    def __init__(self):
        super(ListLogRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'ListLog', 'iothub.api.qcloud.com')

    def get_keywords(self):
        return self.get_params().get('keywords')

    def set_keywords(self, keywords):
        self.add_param('keywords', keywords)

    def get_keywordsOp(self):
        return self.get_params().get('keywordsOp')

    def set_keywordsOp(self, keywordsOp):
        self.add_param('keywordsOp', keywordsOp)

    def get_maxTime(self):
        return self.get_params().get('maxTime')

    def set_maxTime(self, maxTime):
        self.add_param('maxTime', maxTime)

    def get_minTime(self):
        return self.get_params().get('minTime')

    def set_minTime(self, minTime):
        self.add_param('minTime', minTime)

    def get_pageNum(self):
        return self.get_params().get('pageNum')

    def set_pageNum(self, pageNum):
        self.add_param('pageNum', pageNum)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)

    def get_timeOrder(self):
        return self.get_params().get('timeOrder')

    def set_timeOrder(self, timeOrder):
        self.add_param('timeOrder', timeOrder)

    def get_uin(self):
        return self.get_params().get('uin')

    def set_uin(self, uin):
        self.add_param('uin', uin)
