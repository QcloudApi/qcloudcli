# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLVBOnlineUsersRequest(Request):

    def __init__(self):
        super(DescribeLVBOnlineUsersRequest, self).__init__(
            'live', 'qcloudcliV1', 'DescribeLVBOnlineUsers', 'live.api.qcloud.com')

    def get_channelIds(self):
        return self.get_params().get('channelIds')

    def set_channelIds(self, channelIds):
        self.add_param('channelIds', channelIds)
