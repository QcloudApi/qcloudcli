# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateLVBShotRequest(Request):

    def __init__(self):
        super(CreateLVBShotRequest, self).__init__(
            'live', 'qcloudcliV1', 'CreateLVBShot', 'live.api.qcloud.com')

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
