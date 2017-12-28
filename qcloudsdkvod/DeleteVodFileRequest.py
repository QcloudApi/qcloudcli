# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteVodFileRequest(Request):

    def __init__(self):
        super(DeleteVodFileRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DeleteVodFile', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_isFlushCdn(self):
        return self.get_params().get('isFlushCdn')

    def set_isFlushCdn(self, isFlushCdn):
        self.add_param('isFlushCdn', isFlushCdn)

    def get_priority(self):
        return self.get_params().get('priority')

    def set_priority(self, priority):
        self.add_param('priority', priority)
