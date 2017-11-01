# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetVodPlayStatusRequest(Request):

    def __init__(self):
        super(SetVodPlayStatusRequest, self).__init__(
            'vod', 'qcloudcliV1', 'SetVodPlayStatus', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_playStatus(self):
        return self.get_params().get('playStatus')

    def set_playStatus(self, playStatus):
        self.add_param('playStatus', playStatus)
