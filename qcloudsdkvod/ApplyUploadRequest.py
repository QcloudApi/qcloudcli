# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ApplyUploadRequest(Request):

    def __init__(self):
        super(ApplyUploadRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ApplyUpload', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_classId(self):
        return self.get_params().get('classId')

    def set_classId(self, classId):
        self.add_param('classId', classId)

    def get_coverName(self):
        return self.get_params().get('coverName')

    def set_coverName(self, coverName):
        self.add_param('coverName', coverName)

    def get_coverSize(self):
        return self.get_params().get('coverSize')

    def set_coverSize(self, coverSize):
        self.add_param('coverSize', coverSize)

    def get_coverType(self):
        return self.get_params().get('coverType')

    def set_coverType(self, coverType):
        self.add_param('coverType', coverType)

    def get_expireTime(self):
        return self.get_params().get('expireTime')

    def set_expireTime(self, expireTime):
        self.add_param('expireTime', expireTime)

    def get_isCdnPusher(self):
        return self.get_params().get('isCdnPusher')

    def set_isCdnPusher(self, isCdnPusher):
        self.add_param('isCdnPusher', isCdnPusher)

    def get_isScreenshot(self):
        return self.get_params().get('isScreenshot')

    def set_isScreenshot(self, isScreenshot):
        self.add_param('isScreenshot', isScreenshot)

    def get_isTranscode(self):
        return self.get_params().get('isTranscode')

    def set_isTranscode(self, isTranscode):
        self.add_param('isTranscode', isTranscode)

    def get_isWatermark(self):
        return self.get_params().get('isWatermark')

    def set_isWatermark(self, isWatermark):
        self.add_param('isWatermark', isWatermark)

    def get_procedure(self):
        return self.get_params().get('procedure')

    def set_procedure(self, procedure):
        self.add_param('procedure', procedure)

    def get_procedure(self):
        return self.get_params().get('procedure')

    def set_procedure(self, procedure):
        self.add_param('procedure', procedure)

    def get_sourceContext(self):
        return self.get_params().get('sourceContext')

    def set_sourceContext(self, sourceContext):
        self.add_param('sourceContext', sourceContext)

    def get_storageRegion(self):
        return self.get_params().get('storageRegion')

    def set_storageRegion(self, storageRegion):
        self.add_param('storageRegion', storageRegion)

    def get_videoFileId(self):
        return self.get_params().get('videoFileId')

    def set_videoFileId(self, videoFileId):
        self.add_param('videoFileId', videoFileId)

    def get_videoName(self):
        return self.get_params().get('videoName')

    def set_videoName(self, videoName):
        self.add_param('videoName', videoName)

    def get_videoSize(self):
        return self.get_params().get('videoSize')

    def set_videoSize(self, videoSize):
        self.add_param('videoSize', videoSize)

    def get_videoStoragePath(self):
        return self.get_params().get('videoStoragePath')

    def set_videoStoragePath(self, videoStoragePath):
        self.add_param('videoStoragePath', videoStoragePath)

    def get_videoType(self):
        return self.get_params().get('videoType')

    def set_videoType(self, videoType):
        self.add_param('videoType', videoType)

    def get_vodSessionKey(self):
        return self.get_params().get('vodSessionKey')

    def set_vodSessionKey(self, vodSessionKey):
        self.add_param('vodSessionKey', vodSessionKey)
