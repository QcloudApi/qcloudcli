# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class WxPublishRequest(Request):

    def __init__(self):
        super(WxPublishRequest, self).__init__(
            'vod', 'qcloudcliV1', 'WxPublish', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_fileUrl(self):
        return self.get_params().get('fileUrl')

    def set_fileUrl(self, fileUrl):
        self.add_param('fileUrl', fileUrl)

    def get_videoUin(self):
        return self.get_params().get('videoUin')

    def set_videoUin(self, videoUin):
        self.add_param('videoUin', videoUin)
