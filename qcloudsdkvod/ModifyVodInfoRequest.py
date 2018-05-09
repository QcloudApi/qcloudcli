# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyVodInfoRequest(Request):

    def __init__(self):
        super(ModifyVodInfoRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ModifyVodInfo', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_classId(self):
        return self.get_params().get('classId')

    def set_classId(self, classId):
        self.add_param('classId', classId)

    def get_className(self):
        return self.get_params().get('className')

    def set_className(self, className):
        self.add_param('className', className)

    def get_expireTime(self):
        return self.get_params().get('expireTime')

    def set_expireTime(self, expireTime):
        self.add_param('expireTime', expireTime)

    def get_expireTimeStamp(self):
        return self.get_params().get('expireTimeStamp')

    def set_expireTimeStamp(self, expireTimeStamp):
        self.add_param('expireTimeStamp', expireTimeStamp)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_fileIntro(self):
        return self.get_params().get('fileIntro')

    def set_fileIntro(self, fileIntro):
        self.add_param('fileIntro', fileIntro)

    def get_fileName(self):
        return self.get_params().get('fileName')

    def set_fileName(self, fileName):
        self.add_param('fileName', fileName)
