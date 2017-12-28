# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ConvertVodFileRequest(Request):

    def __init__(self):
        super(ConvertVodFileRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ConvertVodFile', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_isScreenshot(self):
        return self.get_params().get('isScreenshot')

    def set_isScreenshot(self, isScreenshot):
        self.add_param('isScreenshot', isScreenshot)

    def get_isWatermark(self):
        return self.get_params().get('isWatermark')

    def set_isWatermark(self, isWatermark):
        self.add_param('isWatermark', isWatermark)

    def get_notifyUrl(self):
        return self.get_params().get('notifyUrl')

    def set_notifyUrl(self, notifyUrl):
        self.add_param('notifyUrl', notifyUrl)
