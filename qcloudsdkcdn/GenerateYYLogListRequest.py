# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GenerateYYLogListRequest(Request):

    def __init__(self):
        super(GenerateYYLogListRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GenerateYYLogList', 'cdn.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
