# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GenerateLogListRequest(Request):

    def __init__(self):
        super(GenerateLogListRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GenerateLogList', 'cdn.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
