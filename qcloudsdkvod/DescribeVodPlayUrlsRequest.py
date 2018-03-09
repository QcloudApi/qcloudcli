# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVodPlayUrlsRequest(Request):

    def __init__(self):
        super(DescribeVodPlayUrlsRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeVodPlayUrls', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)
