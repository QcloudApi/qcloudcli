# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRecordRequest(Request):

    def __init__(self):
        super(DescribeRecordRequest, self).__init__(
            'live', 'qcloudcliV1', 'DescribeRecord', 'live.api.qcloud.com')

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

    def get_taskId(self):
        return self.get_params().get('taskId')

    def set_taskId(self, taskId):
        self.add_param('taskId', taskId)
