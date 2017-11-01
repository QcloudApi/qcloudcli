# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class StopLVBChannelRequest(Request):

    def __init__(self):
        super(StopLVBChannelRequest, self).__init__(
            'live', 'qcloudcliV1', 'StopLVBChannel', 'live.api.qcloud.com')

    def get_channelIds(self):
        return self.get_params().get('channelIds')

    def set_channelIds(self, channelIds):
        self.add_param('channelIds', channelIds)
