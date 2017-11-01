# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CommitUploadRequest(Request):

    def __init__(self):
        super(CommitUploadRequest, self).__init__(
            'vod', 'qcloudcliV1', 'CommitUpload', 'vod.api.qcloud.com')

    def get_vodSessionKey(self):
        return self.get_params().get('vodSessionKey')

    def set_vodSessionKey(self, vodSessionKey):
        self.add_param('vodSessionKey', vodSessionKey)
