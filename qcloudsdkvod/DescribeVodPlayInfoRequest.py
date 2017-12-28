# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVodPlayInfoRequest(Request):

    def __init__(self):
        super(DescribeVodPlayInfoRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeVodPlayInfo', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_fileName(self):
        return self.get_params().get('fileName')

    def set_fileName(self, fileName):
        self.add_param('fileName', fileName)

    def get_pageNo(self):
        return self.get_params().get('pageNo')

    def set_pageNo(self, pageNo):
        self.add_param('pageNo', pageNo)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
