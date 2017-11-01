# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class StartLVBChannelRequest(Request):

    def __init__(self):
        super(StartLVBChannelRequest, self).__init__(
            'live', 'qcloudcliV1', 'StartLVBChannel', 'live.api.qcloud.com')

    def get_channelIds(self):
        return self.get_params().get('channelIds')

    def set_channelIds(self, channelIds):
        self.add_param('channelIds', channelIds)
