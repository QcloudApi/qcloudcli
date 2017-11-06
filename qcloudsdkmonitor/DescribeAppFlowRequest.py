# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAppFlowRequest(Request):

    def __init__(self):
        super(DescribeAppFlowRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAppFlow', 'monitor.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
