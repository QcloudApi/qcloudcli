# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRecordListRequest(Request):

    def __init__(self):
        super(DescribeRecordListRequest, self).__init__(
            'live', 'qcloudcliV1', 'DescribeRecordList', 'live.api.qcloud.com')

    def get_channelId(self):
        return self.get_params().get('channelId')

    def set_channelId(self, channelId):
        self.add_param('channelId', channelId)

    def get_pageNo(self):
        return self.get_params().get('pageNo')

    def set_pageNo(self, pageNo):
        self.add_param('pageNo', pageNo)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
