# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class MultiPullVodFileRequest(Request):

    def __init__(self):
        super(MultiPullVodFileRequest, self).__init__(
            'vod', 'qcloudcliV1', 'MultiPullVodFile', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_pullset(self):
        return self.get_params().get('pullset')

    def set_pullset(self, pullset):
        self.add_param('pullset', pullset)
