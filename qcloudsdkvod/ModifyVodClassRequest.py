# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyVodClassRequest(Request):

    def __init__(self):
        super(ModifyVodClassRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ModifyVodClass', 'vod.api.qcloud.com')

    def get_classId(self):
        return self.get_params().get('classId')

    def set_classId(self, classId):
        self.add_param('classId', classId)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)
