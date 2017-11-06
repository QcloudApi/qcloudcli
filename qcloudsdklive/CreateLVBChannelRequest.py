# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateLVBChannelRequest(Request):

    def __init__(self):
        super(CreateLVBChannelRequest, self).__init__(
            'live', 'qcloudcliV1', 'CreateLVBChannel', 'live.api.qcloud.com')

    def get_channelDescribe(self):
        return self.get_params().get('channelDescribe')

    def set_channelDescribe(self, channelDescribe):
        self.add_param('channelDescribe', channelDescribe)

    def get_channelName(self):
        return self.get_params().get('channelName')

    def set_channelName(self, channelName):
        self.add_param('channelName', channelName)

    def get_outputRate(self):
        return self.get_params().get('outputRate')

    def set_outputRate(self, outputRate):
        self.add_param('outputRate', outputRate)

    def get_outputSourceType(self):
        return self.get_params().get('outputSourceType')

    def set_outputSourceType(self, outputSourceType):
        self.add_param('outputSourceType', outputSourceType)

    def get_playerPassword(self):
        return self.get_params().get('playerPassword')

    def set_playerPassword(self, playerPassword):
        self.add_param('playerPassword', playerPassword)

    def get_sourceList(self):
        return self.get_params().get('sourceList')

    def set_sourceList(self, sourceList):
        self.add_param('sourceList', sourceList)

    def get_watermarkId(self):
        return self.get_params().get('watermarkId')

    def set_watermarkId(self, watermarkId):
        self.add_param('watermarkId', watermarkId)
