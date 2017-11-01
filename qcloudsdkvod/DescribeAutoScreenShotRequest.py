# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAutoScreenShotRequest(Request):

    def __init__(self):
        super(DescribeAutoScreenShotRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeAutoScreenShot', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)
