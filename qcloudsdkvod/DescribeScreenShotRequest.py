# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScreenShotRequest(Request):

    def __init__(self):
        super(DescribeScreenShotRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeScreenShot', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_height(self):
        return self.get_params().get('height')

    def set_height(self, height):
        self.add_param('height', height)

    def get_width(self):
        return self.get_params().get('width')

    def set_width(self, width):
        self.add_param('width', width)
