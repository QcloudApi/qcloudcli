# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateRecordRequest(Request):

    def __init__(self):
        super(CreateRecordRequest, self).__init__(
            'live', 'qcloudcliV1', 'CreateRecord', 'live.api.qcloud.com')

    def get_channelId(self):
        return self.get_params().get('channelId')

    def set_channelId(self, channelId):
        self.add_param('channelId', channelId)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_tapeType(self):
        return self.get_params().get('tapeType')

    def set_tapeType(self, tapeType):
        self.add_param('tapeType', tapeType)
