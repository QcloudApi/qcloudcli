# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmHistoryRequest(Request):

    def __init__(self):
        super(DescribeAlarmHistoryRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmHistory', 'monitor.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
