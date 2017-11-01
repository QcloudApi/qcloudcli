# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateScreenShotRequest(Request):

    def __init__(self):
        super(CreateScreenShotRequest, self).__init__(
            'vod', 'qcloudcliV1', 'CreateScreenShot', 'vod.api.qcloud.com')

    def get_pullset(self):
        return self.get_params().get('pullset')

    def set_pullset(self, pullset):
        self.add_param('pullset', pullset)
