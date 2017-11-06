# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLVBChannelListRequest(Request):

    def __init__(self):
        super(DescribeLVBChannelListRequest, self).__init__(
            'live', 'qcloudcliV1', 'DescribeLVBChannelList', 'live.api.qcloud.com')

    def get_ascDesc(self):
        return self.get_params().get('ascDesc')

    def set_ascDesc(self, ascDesc):
        self.add_param('ascDesc', ascDesc)

    def get_channelStatus(self):
        return self.get_params().get('channelStatus')

    def set_channelStatus(self, channelStatus):
        self.add_param('channelStatus', channelStatus)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_pageNo(self):
        return self.get_params().get('pageNo')

    def set_pageNo(self, pageNo):
        self.add_param('pageNo', pageNo)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
