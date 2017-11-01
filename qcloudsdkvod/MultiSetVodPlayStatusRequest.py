# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class MultiSetVodPlayStatusRequest(Request):

    def __init__(self):
        super(MultiSetVodPlayStatusRequest, self).__init__(
            'vod', 'qcloudcliV1', 'MultiSetVodPlayStatus', 'vod.api.qcloud.com')

    def get_pullset(self):
        return self.get_params().get('pullset')

    def set_pullset(self, pullset):
        self.add_param('pullset', pullset)
