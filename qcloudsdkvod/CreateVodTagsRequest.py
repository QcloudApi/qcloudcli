# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateVodTagsRequest(Request):

    def __init__(self):
        super(CreateVodTagsRequest, self).__init__(
            'vod', 'qcloudcliV1', 'CreateVodTags', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_tags(self):
        return self.get_params().get('tags')

    def set_tags(self, tags):
        self.add_param('tags', tags)
