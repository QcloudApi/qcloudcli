# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class WxPublishRequest(Request):

    def __init__(self):
        super(WxPublishRequest, self).__init__(
            'vod', 'qcloudcliV1', 'WxPublish', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_fileUrl(self):
        return self.get_params().get('fileUrl')

    def set_fileUrl(self, fileUrl):
        self.add_param('fileUrl', fileUrl)
