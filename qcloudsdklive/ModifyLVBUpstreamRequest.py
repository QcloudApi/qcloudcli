# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLVBUpstreamRequest(Request):

    def __init__(self):
        super(ModifyLVBUpstreamRequest, self).__init__(
            'live', 'qcloudcliV1', 'ModifyLVBUpstream', 'live.api.qcloud.com')

    def get_channelId(self):
        return self.get_params().get('channelId')

    def set_channelId(self, channelId):
        self.add_param('channelId', channelId)

    def get_sourceAddress(self):
        return self.get_params().get('sourceAddress')

    def set_sourceAddress(self, sourceAddress):
        self.add_param('sourceAddress', sourceAddress)

    def get_sourceId(self):
        return self.get_params().get('sourceId')

    def set_sourceId(self, sourceId):
        self.add_param('sourceId', sourceId)

    def get_sourceName(self):
        return self.get_params().get('sourceName')

    def set_sourceName(self, sourceName):
        self.add_param('sourceName', sourceName)

    def get_sourceType(self):
        return self.get_params().get('sourceType')

    def set_sourceType(self, sourceType):
        self.add_param('sourceType', sourceType)
